import atexit
import os
import signal
import subprocess
import sys
import threading
import time
from collections import deque
from flask import Flask, Response, jsonify, render_template_string, request

LOG_FILE = sys.argv[1] if len(sys.argv) > 1 else "filename.log"
DEFAULT_FREQ = 8439500000
INTERVAL = 0.2        # Sub-second sample interval: 5 updates per second (200ms)
AVG_SAMPLES = 10      # Rolling average over the last 10 samples (2 seconds)
WINDOW_SECONDS = 300  # Keep 5 minutes of history visible in one window
MAX_POINTS = int(WINDOW_SECONDS / INTERVAL)

app = Flask(__name__)
latest_avg_rate = 0.0

proc_lock = threading.Lock()
current_proc = None
current_freq = DEFAULT_FREQ


def stop_picam_process():
    global current_proc
    if current_proc is not None and current_proc.poll() is None:
        try:
            # Send SIGINT (equivalent to Ctrl-C) to the process group
            os.killpg(os.getpgid(current_proc.pid), signal.SIGINT)
            current_proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            os.killpg(os.getpgid(current_proc.pid), signal.SIGKILL)
            current_proc.wait()
        except ProcessLookupError:
            pass
    current_proc = None


def launch_picam_process(freq: int):
    global current_proc, current_freq
    with proc_lock:
        if current_proc is not None and current_proc.poll() is None and current_freq == freq:
            return
        stop_picam_process()
        current_freq = freq
        print(f"[Tuner] Launching: python3 variance_picam.py {freq}")
        current_proc = subprocess.Popen(
            ["python3", "variance_picam.py", str(freq)],
            start_new_session=True
        )


atexit.register(stop_picam_process)


def watch_file_lines():
    global latest_avg_rate
    recent_rates = deque(maxlen=AVG_SAMPLES)
    f = None
    last_inode = None

    while True:
        time.sleep(INTERVAL)
        if not os.path.exists(LOG_FILE):
            recent_rates.append(0.0)
            latest_avg_rate = 0.0
            if f:
                f.close()
                f = None
            continue

        try:
            stat = os.stat(LOG_FILE)
            if f is None or stat.st_ino != last_inode:
                if f:
                    f.close()
                f = open(LOG_FILE, "r", encoding="utf-8", errors="ignore")
                f.seek(0, os.SEEK_END)
                last_inode = stat.st_ino
            elif stat.st_size < f.tell():
                f.seek(0, os.SEEK_SET)

            new_lines = 0
            while f.readline():
                new_lines += 1

            instant_rate = new_lines / INTERVAL
            recent_rates.append(instant_rate)
            latest_avg_rate = sum(recent_rates) / len(recent_rates)
            latest_avg_rate = latest_avg_rate*16*10

        except OSError:
            recent_rates.append(0.0)
            latest_avg_rate = sum(recent_rates) / len(recent_rates)
            latest_avg_rate = latest_avg_rate*16*10


threading.Thread(target=watch_file_lines, daemon=True).start()

HTML_PAGE = f"""
<!DOCTYPE html>
<html>
<head>
  <title>Live Averaged Line Rate</title>
  <style>
    body {{ font-family: sans-serif; margin: 0; padding: 20px; background: #111; color: #eee; box-sizing: border-box; height: 100vh; display: flex; flex-direction: column; }}
    .header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; flex-wrap: wrap; gap: 12px; }}
    h2 {{ margin: 0; font-size: 1.3rem; }}
    .controls {{ display: flex; align-items: center; gap: 10px; font-size: 0.9rem; flex-wrap: wrap; }}
    .control-group {{ display: flex; align-items: center; gap: 6px; }}
    input {{ background: #222; color: #eee; border: 1px solid #555; padding: 5px 8px; border-radius: 4px; }}
    #freqInput {{ width: 130px; font-family: monospace; }}
    #yMaxInput {{ width: 80px; }}
    button {{ background: #2563eb; color: #fff; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-weight: 600; }}
    button:hover {{ background: #1d4ed8; }}
    button.secondary {{ background: #333; color: #eee; border: 1px solid #555; font-weight: normal; }}
    button.secondary:hover {{ background: #444; }}
    #tuneStatus {{ color: #9ca3af; font-size: 0.85rem; }}
    canvas {{ width: 100%; flex: 1; border: 1px solid #444; background: #1e1e1e; display: block; }}
  </style>
</head>
<body>
  <div class="header">
    <h2>Live Rate: <span id="val" style="color: #4ade80;">0.0</span> baud</h2>
    <div class="controls">
      <div class="control-group">
        <label for="freqInput">Tuning Freq (Hz):</label>
        <input type="number" id="freqInput" value="{DEFAULT_FREQ}" step="1">
        <button onclick="setFrequency()">Tune</button>
        <span id="tuneStatus">Active: {DEFAULT_FREQ} Hz</span>
      </div>
      <div class="control-group">
        <label for="yMaxInput">Y-Axis Max:</label>
        <input type="number" id="yMaxInput" placeholder="Auto" min="1" step="any">
        <button class="secondary" onclick="document.getElementById('yMaxInput').value=''; draw();">Auto</button>
      </div>
    </div>
  </div>
  <canvas id="c"></canvas>
  <script>
    const canvas = document.getElementById('c');
    const ctx = canvas.getContext('2d');
    const yMaxInput = document.getElementById('yMaxInput');
    const freqInput = document.getElementById('freqInput');
    const tuneStatus = document.getElementById('tuneStatus');
    const points = new Array();
    const MAX_POINTS = {MAX_POINTS};
    const PAD_LEFT = 55;
    const PAD_RIGHT = 15;
    const PAD_TOP = 15;
    const PAD_BOTTOM = 15;

    yMaxInput.addEventListener('input', draw);
    freqInput.addEventListener('keydown', (e) => {{
      if (e.key === 'Enter') setFrequency();
    }});

    async function setFrequency() {{
      const freq = parseInt(freqInput.value, 10);
      if (isNaN(freq) || freq <= 0) {{
        tuneStatus.innerText = 'Invalid frequency';
        return;
      }}
      tuneStatus.innerText = 'Respawning...';
      try {{
        const res = await fetch('/tune', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{ freq }})
        }});
        const data = await res.json();
        if (res.ok) {{
          tuneStatus.innerText = `Active: ${{data.freq}} Hz`;
        }} else {{
          tuneStatus.innerText = data.error || 'Error';
        }}
      }} catch (err) {{
        tuneStatus.innerText = 'Request failed';
      }}
    }}

    function resize() {{
      canvas.width = canvas.clientWidth;
      canvas.height = canvas.clientHeight;
      draw();
    }}
    window.addEventListener('resize', resize);
    resize();

    function draw() {{
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const plotW = canvas.width - PAD_LEFT - PAD_RIGHT;
      const plotH = canvas.height - PAD_TOP - PAD_BOTTOM;

      const customMax = parseFloat(yMaxInput.value);
      const max = (!isNaN(customMax) && customMax > 0)
        ? customMax
        : Math.max(5, ...points);

      ctx.font = '12px monospace';
      ctx.textAlign = 'right';
      ctx.textBaseline = 'middle';
      const ticks = 4;
      for (let i = 0; i <= ticks; i++) {{
        const ratio = i / ticks;
        const val = max * ratio;
        const y = PAD_TOP + plotH - (ratio * plotH);

        ctx.strokeStyle = '#333';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(PAD_LEFT, y);
        ctx.lineTo(PAD_LEFT + plotW, y);
        ctx.stroke();

        ctx.fillStyle = '#999';
        const label = val >= 100 ? Math.round(val) : val.toFixed(1);
        ctx.fillText(label, PAD_LEFT - 8, y);
      }}

      if (points.length < 2) return;

      const divisor = Math.max(points.length - 1, 1);

      ctx.beginPath();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 1.5;

      points.forEach((v, i) => {{
        const x = PAD_LEFT + (i / divisor) * plotW;
        const clamped = Math.min(v, max);
        const y = PAD_TOP + plotH - (clamped / max) * plotH;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }});
      ctx.stroke();
    }}

    const source = new EventSource('/stream');
    source.onmessage = function(e) {{
      const rate = parseFloat(e.data);
      document.getElementById('val').innerText = rate.toFixed(1);
      points.push(rate);
      if (points.length > MAX_POINTS) points.shift();
      draw();
    }};
  </script>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(HTML_PAGE.replace(f"Active: {DEFAULT_FREQ} Hz", f"Active: {current_freq} Hz").replace(f'value="{DEFAULT_FREQ}"', f'value="{current_freq}"'))


@app.route('/tune', methods=['POST'])
def tune():
    data = request.get_json(silent=True) or {}
    try:
        freq = int(data.get('freq'))
        if freq <= 0:
            raise ValueError
    except (TypeError, ValueError):
        return jsonify({"error": "Frequency must be a positive integer"}), 400

    launch_picam_process(freq)
    return jsonify({"status": "ok", "freq": current_freq})


@app.route('/stream')
def stream():
    def generate():
        while True:
            yield f"data: {latest_avg_rate:.2f}\n\n"
            time.sleep(INTERVAL)
    return Response(generate(), mimetype='text/event-stream')


if __name__ == '__main__':
    launch_picam_process(DEFAULT_FREQ)
    print(f"Monitoring {LOG_FILE} -> Open http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, threaded=True)
