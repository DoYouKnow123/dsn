import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
from scipy import signal
from scipy.ndimage import uniform_filter
import matplotlib.patheffects as path_effects

def make_naval_sonar_colormap():
    """High-visibility naval CIC sonar palette:
    - Floor (0.00 - 0.24): Abyssal black -> Deep sonar navy
    - Faint signals (0.24 - 0.48): Luminous cyan-aqua (makes weak traces pop immediately)
    - Moderate signals (0.48 - 0.75): Bright sonar emerald -> Phosphor green
    - Strong/Peak (0.75 - 1.00): Electric lime -> White-hot phosphor core
    """
def make_naval_sonar_colormap():
    """Deep naval CIC sonar palette with darker, richer emerald/forest greens:
    - Floor (0.00 - 0.25): Pitch black -> Deep abyssal navy
    - Faint signals (0.25 - 0.50): Deep oceanic cyan -> Dark pine-teal
    - Moderate signals (0.50 - 0.80): Rich dark emerald -> Deep tactical forest green
    - Strong/Peak (0.80 - 1.00): Medium phosphor green -> Bright peak highlight
    """
    colors = [
        (0.00, "#000205"),  # Abyssal pitch black
        (0.20, "#020B18"),  # Thermal noise floor (very dark navy)
        (0.32, "#064E66"),  # Faintest signal emergence (deep ocean cyan)
        (0.46, "#064E3B"),  # Weak telemetry trace (dark pine green)
        (0.62, "#047857"),  # Moderate signal body (deep emerald)
        (0.78, "#15803D"),  # Strong signal (rich dark forest green)
        (0.91, "#22C55E"),  # Very strong carrier (medium phosphor green)
        (1.00, "#DCFCE7"),  # Peak saturation (soft phosphor white-green)
    ]
    return LinearSegmentedColormap.from_list("naval_cic_deep_green", colors)

def plot_tracks_with_nyquist_split(
    iq, sample_rate, all_locks, main_png="multi_baud_lock.png", is_real_audio=False
):
    interior_locks, edge_locks = split_nyquist_edge_locks(
        all_locks, sample_rate, edge_margin_ratio=0.15, is_real_audio=is_real_audio
    )

    print(f"Interior passband locks: {len(interior_locks)} | Nyquist-edge locks: {len(edge_locks)}")

    has_edge = len(edge_locks) > 0
    n_panes = 2 if has_edge else 1
    fig_height = 11.5 if has_edge else 7.0

    fig, axes = plt.subplots(n_panes, 1, figsize=(16, fig_height), dpi=180, sharex=True)
    fig.patch.set_facecolor("#0A0A0A")

    if not has_edge:
        axes = [axes]

    # Top Pane: Primary Interior Passband Track
    axes[0].set_facecolor("#020605")
#    _render_waterfall_pane(
#        axes[0],
#        fig,
#        iq,
#        sample_rate,
#        interior_locks,
#        title_text=f"Track 1: Interior Passband | Locked Regions: {len(interior_locks)}",
#        skip_dc_bootstrap=False,
#    )
# Hide the top axis and expand axes[1] across the entire subplot grid
    axes[0].set_visible(False)
    axes[1].set_subplotspec(axes[0].get_subplotspec().get_gridspec()[:])

    # Bottom Pane: Unwrapped Nyquist-Edge Track (both -Fs/2 and +Fs/2 meet at 0 Hz)
    if has_edge:
        t = np.arange(len(iq), dtype=np.float32) / sample_rate
        # Multiplying by e^(-j*pi*Fs*t) shifts BOTH -Fs/2 and +Fs/2 directly to 0 Hz
        iq_edge_centered = iq * np.exp(-1j * np.pi * sample_rate * t).astype(np.complex64)

        nyq = sample_rate / 2.0
        remapped_edge_locks = []
        for t0, t1, f_min, f_max, mean_snr, baud in edge_locks:
            f_center = 0.5 * (f_min + f_max)
            half_span = 0.5 * (f_max - f_min)

            # Shift relative to -Nyq (lower edge) or +Nyq (upper edge) without modulo wrapping
            if f_center < 0:
                new_center = f_center + nyq   # e.g., -11800 Hz + 12000 Hz = +200 Hz
            else:
                new_center = f_center - nyq   # e.g., +11800 Hz - 12000 Hz = -200 Hz

            remapped_edge_locks.append(
                (t0, t1, new_center - half_span, new_center + half_span, mean_snr, baud)
            )

        axes[1].set_facecolor("#020605")
        _render_waterfall_pane(
            axes[1],
            fig,
            iq_edge_centered,
            sample_rate,
            remapped_edge_locks,
            title_text=f"Unwrapped Nyquist Edges (±{nyq/1000:.1f} kHz Seam Centered at 0 Hz) | Locked Regions: {len(remapped_edge_locks)}",
            skip_dc_bootstrap=True,
        )

    axes[-1].set_xlabel("Time (seconds)", color="#E2E8F0", fontsize=10)
    plt.tight_layout()
    plt.savefig(main_png, dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved multi-pane spectrogram to {main_png}")

def _render_waterfall_pane(ax, fig, iq, sample_rate, locks, title_text, skip_dc_bootstrap=False, is_real_audio=False):
    """Renders a single high-contrast naval sonar waterfall pane with fluid HUD reticles."""
    import matplotlib.patheffects as path_effects

    nperseg = max(1024, 1 << int(np.round(np.log2(sample_rate / 6.0))))
    duration_sec = len(iq) / sample_rate
    overlap_ratio = 0.50 if duration_sec > 180.0 else 0.75
    noverlap = int(nperseg * overlap_ratio)

    f, t, Sxx = signal.spectrogram(
        iq,
        fs=sample_rate,
        window=("kaiser", 7.0),
        nperseg=nperseg,
        noverlap=noverlap,
        return_onesided=False,
        mode="psd",
    )

    f = np.fft.fftshift(f)
    Sxx = np.fft.fftshift(Sxx, axes=0)

    if is_real_audio:
        pos_rows = f >= 0.0
        f = f[pos_rows]
        Sxx = Sxx[pos_rows, :]

    # Max-pool time columns so brief bursts never disappear
    max_cols = 4000
    if Sxx.shape[1] > max_cols:
        step = int(np.ceil(Sxx.shape[1] / max_cols))
        pad_len = (step - (Sxx.shape[1] % step)) % step
        if pad_len > 0:
            Sxx = np.pad(Sxx, ((0, 0), (0, pad_len)), mode="edge")
            t = np.pad(t, (0, pad_len), mode="edge")
        Sxx = Sxx.reshape(Sxx.shape[0], -1, step).max(axis=2)
        t = t[::step]

    Sxx_db = (10.0 * np.log10(Sxx + 1e-20)).astype(np.float32)
    del Sxx

    # Replace 0 Hz center rows with bootstrap noise (skip on unwrapped Nyquist pane)
    if not skip_dc_bootstrap:
        dc_rows = np.where(np.abs(f) <= 35.0)[0]
        guard_rows = np.where((f > 50.0) & (f <= 250.0))[0] if is_real_audio else np.where((np.abs(f) > 50.0) & (np.abs(f) <= 250.0))[0]
        if len(dc_rows) > 0 and len(guard_rows) > 0:
            rng = np.random.default_rng(42)
            rand_idx = rng.choice(guard_rows, size=(len(dc_rows), Sxx_db.shape[1]), replace=True)
            col_idx = np.arange(Sxx_db.shape[1])[None, :]
            Sxx_db[dc_rows, :] = Sxx_db[rand_idx, col_idx]

    # Noise-anchored scaling with gamma lift to brighten faint signals
    # Lower vmin to the 35th percentile so faint signals rise clearly above the noise floor
    vmin = float(np.percentile(Sxx_db, 35))
    vmax = vmin + 24.0

    # Stronger gamma lift (0.48) pulls dim traces into the bright cyan/emerald phosphor bands
    Sxx_norm = np.clip((Sxx_db - vmin) / (vmax - vmin + 1e-12), 0.0, 1.0)
    Sxx_lifted = (Sxx_norm ** 0.48) * (vmax - vmin) + vmin

    extent = [float(t[0]), float(t[-1]), float(f[0]), float(f[-1])]
    im = ax.imshow(
        Sxx_lifted,
        origin="lower",
        aspect="auto",
        extent=extent,
        interpolation="nearest",
        cmap=make_naval_sonar_colormap(),
        vmin=vmin,
        vmax=vmax,
    )

    # Tactical HUD palette with Pure Black (#000000) in the first slot
    palette = ["#F59E0B", "#F43F5E", "#A855F7", "#EA580C"]

    for idx, (t0, t1, f_min, f_max, mean_snr, baud) in enumerate(locks):
        color = palette[idx % len(palette)]
        is_black = color == "#000000"

        halo_color = "#FFFFFF" if is_black else "#020605"
        badge_bg = "#F8FAFC" if is_black else "#020605"
        active_halo = [
            path_effects.Stroke(linewidth=2.6, foreground=halo_color, alpha=0.85),
            path_effects.Normal(),
        ]

        half_bw = baud * 1.25
        y_bottom = f_min - half_bw
        height = (f_max - f_min) + 2.0 * half_bw
        width = t1 - t0

        # 1. Whisper-light glass tint
        fill_color = "#FFFFFF" if is_black else color
        ax.add_patch(
            patches.Rectangle(
                (t0, y_bottom),
                width,
                height,
                linewidth=0,
                facecolor=fill_color,
                alpha=0.05 if is_black else 0.035,
                zorder=4,
            )
        )

        # 2. Translucent dashed boundary line with contrast halo
        border = patches.Rectangle(
            (t0, y_bottom),
            width,
            height,
            linewidth=1.1,
            edgecolor=color,
            facecolor="none",
            linestyle="--",
            alpha=0.80,
            zorder=5,
        )
        border.set_path_effects(active_halo)
        ax.add_patch(border)

        # 3. Crisp tactical corner brackets (reticles)
        tick_w = min(width * 0.15, float(t[-1] - t[0]) * 0.008)
        tick_h = height * 0.18
        corners = [
            ([t0, t0, t0 + tick_w], [y_bottom + tick_h, y_bottom, y_bottom]),
            ([t0, t0, t0 + tick_w], [y_bottom + height - tick_h, y_bottom + height, y_bottom + height]),
            ([t0 + width - tick_w, t0 + width, t0 + width], [y_bottom, y_bottom, y_bottom + tick_h]),
            ([t0 + width - tick_w, t0 + width, t0 + width], [y_bottom + height, y_bottom + height, y_bottom + height - tick_h]),
        ]
        for cx, cy in corners:
            line, = ax.plot(cx, cy, color=color, linewidth=1.7, alpha=0.95, zorder=6)
            line.set_path_effects(active_halo)

        # 4. Floating HUD badge
        badge = ax.text(
            t0 + 0.1,
            y_bottom + height + (sample_rate * 0.008),
            f"TRK {idx + 1} · {baud:.1f} Bd ({mean_snr:.1f} dB)",
            color=color,
            fontsize=7.5,
            fontweight="bold",
            bbox=dict(
                boxstyle="round,pad=0.5",
                facecolor=badge_bg,
                edgecolor=color,
                linewidth=1.0,
                alpha=0.55,
            ),
            zorder=7,
        )


#        ax.text(
#            t0 + 0.1,
#            y_bottom + height + (sample_rate * 0.008),
#            f"TRK {idx}",  # Replace with your existing label string
#            color=color,
#            fontsize=8.5,
#            fontweight="bold",
#            ha=label_ha,
#            va="bottom",
#            zorder=7,
#            clip_on=True,
#            bbox=dict(
#                boxstyle="round,pad=0.25",
#                facecolor=badge_bg,
#                edgecolor=color,
#                linewidth=1.0,
#                alpha=0.92,
#            ),
#        )
        badge.set_path_effects(active_halo)


    cbar = fig.colorbar(im, ax=ax, pad=0.015)
    cbar.set_label("PSD (dBFS/Hz)", color="#E2E8F0", fontsize=9.5)
    cbar.ax.yaxis.set_tick_params(color="#E2E8F0")
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="#E2E8F0")

    ax.set_title(title_text, color="#FFFFFF", fontsize=11.5, fontweight="bold", pad=10)
    ax.set_ylabel("Frequency Offset (Hz)", color="#E2E8F0", fontsize=10)
    ax.tick_params(colors="#E2E8F0")
    ax.grid(True, which="major", color="#0F3D2E", linestyle=":", linewidth=0.7, alpha=0.65)

    if locks:
        pad_hz = max(r[5] * 6.0 for r in locks)
        y_lo = min(r[2] for r in locks) - pad_hz
        y_hi = max(r[3] for r in locks) + pad_hz
        min_bound = 0.0 if is_real_audio else -sample_rate / 2.0
        ax.set_ylim(max(min_bound, y_lo), min(sample_rate / 2.0, y_hi))

def split_nyquist_edge_locks(all_locks, sample_rate, edge_margin_ratio=0.15, is_real_audio=False):
    """Splits detected locks into interior passband signals and Nyquist-edge signals
    (catching both the lower -Fs/2 edge and upper +Fs/2 edge).
    """
    nyq = sample_rate / 2.0
    edge_limit = nyq * (1.0 - edge_margin_ratio)

    interior_locks = []
    edge_locks = []

    for lock in all_locks:
        t0, t1, f_min, f_max, mean_snr, baud = lock
        half_bw = baud * 1.25
        # Check both lower Nyquist (-Fs/2) and upper Nyquist (+Fs/2)
        lower_bound = 0.0 if is_real_audio else -nyq
        at_lower_edge = (f_min - half_bw) <= (lower_bound + nyq * edge_margin_ratio)
        at_upper_edge = (f_max + half_bw) >= (nyq * (1.0 - edge_margin_ratio))

#        at_lower_edge = (f_min - half_bw) <= -edge_limit
#        at_upper_edge = (f_max + half_bw) >= edge_limit

        if at_lower_edge or at_upper_edge:
            edge_locks.append(lock)
        else:
            interior_locks.append(lock)

    return interior_locks, edge_locks

def load_iq_wav(
    filename,
    is_real_audio=False,
    swap_iq=False,
    reverse_time=False,
    notch_half_width_hz=45.0,
):
    """Loads either a 2-channel complex IQ WAV file or a real positive-frequency audio WAV file.

    When `is_real_audio=True`, converts real audio into an analytic signal occupying
    positive frequencies [0 Hz, +Fs/2] so the entire downstream detector and waterfall work natively.
    """
    with wave.open(filename, "rb") as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        sample_rate = wf.getframerate()
        raw_bytes = wf.readframes(wf.getnframes())

    if sampwidth == 2:
        data = np.frombuffer(raw_bytes, dtype=np.int16).astype(np.float64) / 32768.0
    elif sampwidth == 4:
        data = np.frombuffer(raw_bytes, dtype=np.int32).astype(np.float64) / 2147483648.0
    else:
        raise ValueError(f"Unsupported sample width: {sampwidth} bytes")

    if is_real_audio:
        # Handle mono or stereo real audio (average channels if stereo)
        if n_channels == 2:
            real_sig = 0.5 * (data[0::2] + data[1::2])
        elif n_channels == 1:
            real_sig = data
        else:
            raise ValueError(f"Unsupported channel count for real audio: {n_channels}")

        if reverse_time:
            real_sig = real_sig[::-1]

        real_sig = real_sig - np.mean(real_sig)

        # Convert real audio to analytic complex signal (positive frequencies 0 to +Fs/2)
        n = len(real_sig)
        spec = np.fft.fft(real_sig)
        h = np.zeros(n, dtype=np.float64)
        if n % 2 == 0:
            h[0] = h[n // 2] = 1.0
            h[1 : n // 2] = 2.0
        else:
            h[0] = 1.0
            h[1 : (n + 1) // 2] = 2.0
        iq = np.fft.ifft(spec * h)
    else:
        if n_channels != 2:
            raise ValueError("IQ WAV file must be 2-channel (I and Q). Set is_real_audio=True for mono audio.")
        iq = (data[0::2] - 1j * data[1::2]) if swap_iq else (data[0::2] + 1j * data[1::2])
        if reverse_time:
            iq = iq[::-1]
        iq = iq - np.mean(iq)

    # Replace any persistent 0 Hz DC/hum spike with matched thermal noise
    n = len(iq)
    spec = np.fft.fft(iq)
    freqs = np.fft.fftfreq(n, d=1.0 / sample_rate)

    # For real audio, only search positive frequencies (0 to +500 Hz)
    search_mask = (freqs >= 0.0) & (freqs <= 500.0) if is_real_audio else (np.abs(freqs) <= 500.0)
    if np.any(search_mask):
        center_freqs = freqs[search_mask]
        center_mags = np.abs(spec[search_mask])
        spike_freq = float(center_freqs[np.argmax(center_mags)])

        spike_mask = np.abs(freqs - spike_freq) <= notch_half_width_hz
        guard_mask = (np.abs(freqs - spike_freq) > notch_half_width_hz * 1.5) & (
            np.abs(freqs - spike_freq) <= notch_half_width_hz * 4.0
        )
        if is_real_audio:
            guard_mask &= freqs > 0.0

        guard_mags = np.abs(spec[guard_mask])
        sigma = (np.median(guard_mags) / 1.1774100225) if len(guard_mags) > 0 else 0.0

        n_bad = int(np.count_nonzero(spike_mask))
        rng = np.random.default_rng(42)
        spec[spike_mask] = sigma * (rng.standard_normal(n_bad) + 1j * rng.standard_normal(n_bad))
        iq = np.fft.ifft(spec)

    return iq.astype(np.complex64), sample_rate


def find_candidate_channels(iq, sample_rate, min_sep_hz=800.0, max_channels=4, is_real_audio=False):
    """Finds distinct frequency regions containing signal energy above the noise floor."""
    nfft = 4096
    f, psd = signal.welch(
        iq, fs=sample_rate, nperseg=nfft, return_onesided=False, scaling="density"
    )
    f = np.fft.fftshift(f)
    psd_db = 10.0 * np.log10(np.fft.fftshift(psd) + 1e-20)

    # Smooth PSD to merge BPSK sidebands into a single channel hump
    kernel_bins = max(5, int(round(300.0 / (sample_rate / nfft))) | 1)
    smooth_psd = signal.medfilt(psd_db, kernel_size=kernel_bins)
    if is_real_audio:
        pos_mask = f >= 0.0
        f = f[pos_mask]
        smooth_psd = smooth_psd[pos_mask]

    noise_floor = np.percentile(smooth_psd, 30)

    min_dist_bins = max(1, int(min_sep_hz / (sample_rate / nfft)))
    # Pad edges so signals hugging -Fs/2 or +Fs/2 still register as valid peaks
    padded_psd = np.pad(smooth_psd, (1, 1), mode="constant", constant_values=noise_floor)
    peaks, props = signal.find_peaks(
        padded_psd,
        height=noise_floor + 4.5,
        prominence=3.5,
        distance=min_dist_bins,
    )
    peaks = peaks - 1  # Shift indices back after removing padding

    if len(peaks) == 0:
        return [0.0]

    # Sort peaks by prominence and keep top candidates
    order = np.argsort(props["prominences"])[::-1][:max_channels]
    return [float(f[p]) for p in order]


def isolate_channel(iq, sample_rate, center_hz, channel_bw=3000.0):
    """Shifts a target frequency offset to 0 Hz, strips DC, and low-pass filters."""
    t = np.arange(len(iq), dtype=np.float32) / sample_rate
    shifted = iq * np.exp(-1j * 2.0 * np.pi * center_hz * t).astype(np.complex64)

    # Remove 0 Hz DC offset so it doesn't pull carrier frequency estimation to center_hz
    shifted -= np.mean(shifted)

    nyq = sample_rate / 2.0
    cutoff = min(channel_bw / 2.0, nyq * 0.9)
    sos = signal.butter(5, cutoff / nyq, btype="low", output="sos")
    filtered = signal.sosfiltfilt(sos, shifted).astype(np.complex64)

    decim = max(1, int(sample_rate // (cutoff * 4.0)))
    if decim > 1:
        filtered = filtered[::decim]
    return filtered, sample_rate / decim


def estimate_baud_rate(iq_chan, fs_chan, min_baud=30.0, max_baud=3000.0):
    """Estimates symbol rate on an isolated baseband channel with 4x zero-padded FFT."""
    diff_mag = np.abs(np.diff(iq_chan))
    diff_mag -= np.mean(diff_mag)

    # 4x zero-padding resolves fractional baud rates like 200.39 Bd cleanly
    nfft = 1 << ((len(diff_mag) - 1).bit_length() + 2)
    spec = np.abs(np.fft.rfft(diff_mag * np.hanning(len(diff_mag)), n=nfft))
    freqs = np.fft.rfftfreq(nfft, d=1.0 / fs_chan)

    mask = (freqs >= min_baud) & (freqs <= min(max_baud, fs_chan * 0.45))
    valid_freqs = freqs[mask]
    valid_spec = spec[mask]

    if len(valid_spec) == 0:
        return 0.0, 0.0

    peak_idx = int(np.argmax(valid_spec))
    est_baud = float(valid_freqs[peak_idx])

    # Parabolic sub-bin interpolation
    if 0 < peak_idx < len(valid_spec) - 1:
        y0, y1, y2 = np.log(valid_spec[peak_idx - 1 : peak_idx + 2] + 1e-12)
        denom = y0 - 2.0 * y1 + y2
        if denom != 0:
            delta = 0.5 * (y0 - y2) / denom
            bin_width = valid_freqs[1] - valid_freqs[0]
            est_baud += delta * bin_width

    # Confidence SNR of the detected baud clock peak
    noise_med = np.median(valid_spec) + 1e-12
    clock_snr = 20.0 * np.log10(valid_spec[peak_idx] / noise_med)
    return est_baud, float(clock_snr)


def detect_channel_locks(
    iq_chan,
    fs_chan,
    center_offset_hz,
    baud_rate,
    win_sec=0.75,
    hop_sec=0.05,
    core_snr_db=9.0,
    tail_snr_db=3.8,
    max_gap_sec=1.5,
    min_duration_sec=1.2,
):
    """Finds AOS-to-LOS locked intervals and accurately tracks the BPSK carrier frequency."""
    win_len = int(win_sec * fs_chan)
    hop_len = int(hop_sec * fs_chan)
    if win_len < 32 or len(iq_chan) <= win_len:
        return []

    half_hop = hop_sec / 2.0
    hann_win = np.hanning(win_len - 1)
    nfft = 1 << ((win_len - 1).bit_length() + 1)
    freqs = np.fft.rfftfreq(nfft, d=1.0 / fs_chan)

    sig_mask = np.abs(freqs - baud_rate) <= max(2.5, baud_rate * 0.035)
    noise_mask = (np.abs(freqs - baud_rate) > baud_rate * 0.08) & (
        np.abs(freqs - baud_rate) <= baud_rate * 0.45
    )

    c_nfft = 1 << (win_len.bit_length() + 2)
    c_freqs = np.fft.fftshift(np.fft.fftfreq(c_nfft, d=1.0 / fs_chan)) / 2.0
    # Mask out the exact 0 Hz DC bin (+/- 8 Hz) so DC leakage never hijacks carrier tracking
    dc_notch_mask = np.abs(c_freqs) > 8.0

    times, snrs, carrier_freqs = [], [], []

    for start in range(0, len(iq_chan) - win_len, hop_len):
        seg = iq_chan[start : start + win_len]
        t_center = (start + win_len / 2.0) / fs_chan

        env = np.abs(np.diff(seg))
        env -= np.mean(env)
        spec = np.abs(np.fft.rfft(env * hann_win, n=nfft)) ** 2

        if np.any(sig_mask) and np.any(noise_mask):
            peak_pwr = np.max(spec[sig_mask])
            noise_pwr = np.median(spec[noise_mask]) + 1e-20
            snr_db = 10.0 * np.log10(peak_pwr / noise_pwr)
        else:
            snr_db = 0.0

        # Square the DC-free segment to collapse BPSK modulation into a pure 2*f_c carrier spike
        seg_ac = seg - np.mean(seg)
        sq = seg_ac**2
        c_spec = np.abs(np.fft.fftshift(np.fft.fft(sq * np.hanning(len(sq)), n=c_nfft)))
        c_spec = np.where(dc_notch_mask, c_spec, 0.0)
        f_local = float(c_freqs[np.argmax(c_spec)])

        times.append(t_center)
        snrs.append(snr_db)
        carrier_freqs.append(center_offset_hz + f_local)

    med_kernel = max(3, int(round(0.3 / hop_sec)) | 1)
    smooth_snrs = signal.medfilt(np.array(snrs), kernel_size=med_kernel)
    # Smooth the tracked carrier frequency to reject single-hop noise jumps
    smooth_freqs = signal.medfilt(np.array(carrier_freqs), kernel_size=med_kernel)
    n_hops = len(smooth_snrs)

    locked_mask = np.zeros(n_hops, dtype=bool)
    for i in range(n_hops):
        if smooth_snrs[i] >= core_snr_db and not locked_mask[i]:
            locked_mask[i] = True
            j = i - 1
            while j >= 0 and smooth_snrs[j] >= tail_snr_db:
                locked_mask[j] = True
                j -= 1
            k = i + 1
            while k < n_hops and smooth_snrs[k] >= tail_snr_db:
                locked_mask[k] = True
                k += 1

    locked_hops = [
        (times[i] - half_hop, times[i] + half_hop, float(smooth_freqs[i]), float(smooth_snrs[i]))
        for i in range(n_hops)
        if locked_mask[i]
    ]
    if not locked_hops:
        return []

    merged = []
    cur_start, cur_end, freqs_list, snrs_list = (
        locked_hops[0][0],
        locked_hops[0][1],
        [locked_hops[0][2]],
        [locked_hops[0][3]],
    )

    for h_start, h_end, f_c, snr in locked_hops[1:]:
        if h_start <= cur_end + max_gap_sec:
            cur_end = max(cur_end, h_end)
            freqs_list.append(f_c)
            snrs_list.append(snr)
        else:
            if (cur_end - cur_start) >= min_duration_sec:
                f_lo = float(np.percentile(freqs_list, 5))
                f_hi = float(np.percentile(freqs_list, 95))
                merged.append((cur_start, cur_end, f_lo, f_hi, float(np.mean(snrs_list)), baud_rate))
            cur_start, cur_end, freqs_list, snrs_list = h_start, h_end, [f_c], [snr]

    if (cur_end - cur_start) >= min_duration_sec:
        f_lo = float(np.percentile(freqs_list, 5))
        f_hi = float(np.percentile(freqs_list, 95))
        merged.append((cur_start, cur_end, f_lo, f_hi, float(np.mean(snrs_list)), baud_rate))

    return merged


def make_red_white_colormap():
    """Inverted high-contrast colormap:
    - Noise floor (0 dB): Pure white
    - Faint signals (+3 to +7 dB): Light gray -> Vivid red
    - Strong signals (+12 to +16 dB+): Dark crimson -> Pure black
    """
    colors = [
        (0.00, "#FFFFFF"),  # 0.0 dB: Thermal noise floor (clean white background)
        (0.15, "#E5E5E5"),  # +2.4 dB: Upper noise ripples (light gray)
        (0.28, "#FF7A7A"),  # +4.5 dB: Very faint signal emergence (salmon/red)
        (0.44, "#E60000"),  # +7.0 dB: Target demodulator signals (vivid red)
        (0.68, "#800000"),  # +10.9 dB: Moderate signal body (deep crimson)
        (0.88, "#2B0000"),  # +14.1 dB: Strong carrier (dark maroon)
        (1.00, "#000000"),  # +16.0 dB+: Peak signal power (pure black)
    ]
    return LinearSegmentedColormap.from_list("inverted_high_contrast_red", colors)


def plot_multi_signal_spectrogram(iq, sample_rate, all_locks, output_png="multi_baud_lock.png"):
    """Plots a memory-safe smooth SoX-like spectrogram using imshow instead of pcolormesh."""
    nperseg = max(1024, 1 << int(np.round(np.log2(sample_rate / 6.0))))
    # Keep overlap moderate on long files (600s+) to avoid massive STFT arrays
    duration_sec = len(iq) / sample_rate
    overlap_ratio = 0.50 if duration_sec > 180.0 else 0.75
    noverlap = int(nperseg * overlap_ratio)

    f, t, Sxx = signal.spectrogram(
        iq,
        fs=sample_rate,
        window=("kaiser", 7.0),
        nperseg=nperseg,
        noverlap=noverlap,
        return_onesided=False,
        mode="psd",
    )

    f = np.fft.fftshift(f)
    Sxx = np.fft.fftshift(Sxx, axes=0)

    # Decimate time columns to max ~4000 pixels so matplotlib uses <100 MB RAM
    # Max-pool time columns instead of skipping (::step) so brief signals never vanish
    max_cols = 4000
    if Sxx.shape[1] > max_cols:
        step = int(np.ceil(Sxx.shape[1] / max_cols))
        pad_len = (step - (Sxx.shape[1] % step)) % step
        if pad_len > 0:
            Sxx = np.pad(Sxx, ((0, 0), (0, pad_len)), mode="edge")
            t = np.pad(t, (0, pad_len), mode="edge")
        Sxx = Sxx.reshape(Sxx.shape[0], -1, step).max(axis=2)
        t = t[::step]

    Sxx_db = (10.0 * np.log10(Sxx + 1e-20)).astype(np.float32)
    del Sxx
    from scipy.ndimage import uniform_filter
    # Replace the exact 0 Hz center row(s) frame-by-frame using local noise statistics
    # 1. Replace the exact 0 Hz center rows FIRST
    # Replace 0 Hz center rows by randomly sampling actual pixels from the guard rows
    dc_rows = np.where(np.abs(f) <= 35.0)[0]
    guard_rows = np.where((np.abs(f) > 50.0) & (np.abs(f) <= 250.0))[0]
    if len(dc_rows) > 0 and len(guard_rows) > 0:
        rng = np.random.default_rng(42)
        # Pick random guard-row indices for every (dc_row, time_col) pixel
        rand_idx = rng.choice(guard_rows, size=(len(dc_rows), Sxx_db.shape[1]), replace=True)
        col_idx = np.arange(Sxx_db.shape[1])[None, :]
        Sxx_db[dc_rows, :] = Sxx_db[rand_idx, col_idx]

    # Smooth ONLY along the time axis (1 freq bin x 3 time frames) so thin signals keep full peak height
    Sxx_db = uniform_filter(Sxx_db, size=(1, 3))

    # Anchor vmin to the 50th percentile (true thermal noise median) so weak signals stay above vmin
  #  vmin = float(np.percentile(Sxx_db, 32))
  #  vmax = vmin + 14.0

  #  vmax = float(np.percentile(Sxx_db, 99.8))
  #  vmin = vmax - 85.0
    # Anchor the bottom of the color scale to the median thermal noise floor
    noise_floor_db = float(np.median(Sxx_db))
    vmin = noise_floor_db         # Deep background noise
    vmax = noise_floor_db + 16.0       # Strong carrier peaks (+28 dB above noise)
    # On a 30 dB span (-2 to +28 dB), +7 dB sits at (7 - (-2)) / 30 = 0.30

    fig, ax = plt.subplots(figsize=(16, 7.5), dpi=180)
    fig.patch.set_facecolor("#0A0A0A")
    ax.set_facecolor("#000000")

    # imshow with bilinear interpolation gives the smooth SoX look without pcolormesh RAM explosion
    extent = [float(t[0]), float(t[-1]), float(f[0]), float(f[-1])]

    im = ax.imshow(
        Sxx_db,
        origin="lower",
        aspect="auto",
        extent=extent,
        interpolation="nearest",
        cmap=make_red_white_colormap(),
        vmin=vmin,
        vmax=vmax,
    )

    palette = ["#00FFCC", "#FFD166", "#00BBF9", "#A8FF60"]
    for idx, (t0, t1, f_min, f_max, mean_snr, baud) in enumerate(all_locks):
        color = palette[idx % len(palette)]
        half_bw = baud * 1.25
        y_bottom = f_min - half_bw
        height = (f_max - f_min) + 2.0 * half_bw
        width = t1 - t0

        ax.add_patch(
            patches.Rectangle(
                (t0, y_bottom), width, height, linewidth=1.5, edgecolor=color, facecolor=color, alpha=0.10, zorder=4
            )
        )
        ax.add_patch(
            patches.Rectangle(
                (t0, y_bottom), width, height, linewidth=1.5, edgecolor=color, facecolor="none", zorder=5
            )
        )
        ax.text(
            t0 + 0.15,
            y_bottom + height + (sample_rate * 0.012),
            f"TRK #{idx + 1} | {baud:.2f} Bd ({mean_snr:.1f} dB)",
            color=color,
            fontsize=8.0,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#020B08", edgecolor=color, alpha=0.90),
            zorder=6,
        )

    cbar = fig.colorbar(im, ax=ax, pad=0.015)
    cbar.set_label("Power Spectral Density (dBFS/Hz)", color="#E2E8F0", fontsize=10)
    cbar.ax.yaxis.set_tick_params(color="#E2E8F0")
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="#E2E8F0")

    ax.set_title(
        f"Multi-Signal IQ Spectrogram | Detected Locked Signals: {len(all_locks)}",
        color="#FFFFFF",
        fontsize=12,
        fontweight="bold",
        pad=12,
    )
    ax.set_xlabel("Time (seconds)", color="#E2E8F0", fontsize=10)
    ax.set_ylabel("Baseband Frequency Offset (Hz)", color="#E2E8F0", fontsize=10)
    ax.tick_params(colors="#E2E8F0")

    if all_locks:
        pad_hz = max(r[5] * 6.0 for r in all_locks)
        y_lo = min(r[2] for r in all_locks) - pad_hz
        y_hi = max(r[3] for r in all_locks) + pad_hz
        ax.set_ylim(max(-sample_rate / 2, y_lo), min(sample_rate / 2, y_hi))

    plt.tight_layout()
    plt.savefig(output_png, dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved multi-signal spectrogram to {output_png}")
import os

def demodulate_locked_regions(
    iq, sample_rate, all_locks, output_dir="demod_tracks", loop_bw_ratio=0.05
):
    """Slices out each locked (t0, t1, f_min, f_max, snr, baud) region, mixes it to
    baseband, runs BPSK Costas + Gardner symbol recovery, and writes packed/unpacked bits.
    """
    if not all_locks:
        print("No locked regions to demodulate.")
        return

    os.makedirs(output_dir, exist_ok=True)
    print(f"\nDemodulating {len(all_locks)} locked regions into ./{output_dir}/ ...")

    for idx, (t0, t1, f_min, f_max, mean_snr, baud_rate) in enumerate(all_locks):
        # 1. Extract exact time slice for this locked burst (with 0.1s guard margin)
        start_idx = max(0, int((t0 - 0.1) * sample_rate))
        end_idx = min(len(iq), int((t1 + 0.1) * sample_rate))
        seg = iq[start_idx:end_idx]
        if len(seg) < int(sample_rate * 0.2):
            continue

        # 2. Mix center of this burst's frequency bounds down to 0 Hz baseband
        f_center = 0.5 * (f_min + f_max)
        t_vec = np.arange(len(seg), dtype=np.float32) / sample_rate
        baseband = seg * np.exp(-1j * 2.0 * np.pi * f_center * t_vec).astype(np.complex64)

        # 3. Matched boxcar/low-pass filter & decimate to ~8 samples per symbol
        sps_raw = sample_rate / baud_rate
        taps_len = max(1, int(round(sps_raw)))
        taps = np.ones(taps_len, dtype=np.float32) / taps_len
        filtered = signal.lfilter(taps, 1.0, baseband)

        decim = max(1, int(round(sps_raw / 8.0)))
        decimated = filtered[::decim]
        fs_decim = sample_rate / decim
        sps_decim = fs_decim / baud_rate

        if len(decimated) < 32:
            continue

        # Normalize RMS amplitude for stable Costas loop gain
        rms = float(np.sqrt(np.mean(np.abs(decimated) ** 2)))
        if rms > 0:
            decimated = decimated / rms

        # 4. 2nd-Order Costas Loop for fine carrier & Doppler tracking
        loop_bw = baud_rate * loop_bw_ratio
        damping = 0.707
        theta = (loop_bw / fs_decim) / (damping + 1.0 / (4.0 * damping))
        denom = 1.0 + 2.0 * damping * theta + theta**2
        alpha = (4.0 * damping * theta) / denom
        beta = (4.0 * theta**2) / denom

        costas_phase = 0.0
        costas_freq = 0.0
        i_rail = np.empty(len(decimated), dtype=np.float32)

        for n in range(len(decimated)):
            rot = decimated[n] * np.exp(-1j * costas_phase)
            i_val = rot.real
            q_val = rot.imag
            i_rail[n] = i_val

            err = (1.0 if i_val >= 0.0 else -1.0) * q_val
            costas_freq += beta * err
            costas_phase += costas_freq + alpha * err
            costas_phase = (costas_phase + np.pi) % (2.0 * np.pi) - np.pi

        # 5. Gardner Fractional Symbol Timing Recovery
        mu = 0.0
        omega = sps_decim
        omega_mid = sps_decim
        ted_gain = 0.005
        bits = []
        idx_s = 0

        while idx_s + int(mu + omega) + 2 < len(i_rail):
            p0 = idx_s + mu
            i0 = int(p0)
            f0 = p0 - i0
            sym_curr = i_rail[i0] * (1.0 - f0) + i_rail[i0 + 1] * f0

            p_mid = idx_s + mu + 0.5 * omega
            im = int(p_mid)
            fm = p_mid - im
            sym_mid = i_rail[im] * (1.0 - fm) + i_rail[im + 1] * fm

            p_next = idx_s + mu + omega
            inext = int(p_next)
            fnext = p_next - inext
            sym_next = i_rail[inext] * (1.0 - fnext) + i_rail[inext + 1] * fnext

            ted_err = (sym_next - sym_curr) * sym_mid
            omega = np.clip(omega + ted_gain * 0.05 * ted_err, omega_mid * 0.98, omega_mid * 1.02)

            bits.append(1 if sym_curr > 0.0 else 0)

            step = mu + omega + ted_gain * ted_err
            int_step = int(step)
            idx_s += int_step
            mu = step - int_step

        bit_arr = np.array(bits, dtype=np.uint8)
        base_name = f"trk_{idx + 1:02d}_{t0:.1f}s_to_{t1:.1f}s_{baud_rate:.1f}bd"

        # Save packed binary (8 bits per byte) and unpacked bits (1 byte per bit)
        packed_path = os.path.join(output_dir, f"{base_name}_packed.bin")
        unpacked_path = os.path.join(output_dir, f"{base_name}_unpacked.u8")

        np.packbits(bit_arr).tofile(packed_path)
        bit_arr.tofile(unpacked_path)
        print(
            f"  [TRK {idx + 1:02d}] {t0:.2f}s-{t1:.2f}s @ {f_center:.1f} Hz ({baud_rate:.2f} Bd) -> "
            f"{len(bit_arr)} bits saved to {packed_path}"
        )


if __name__ == "__main__":
    IS_REAL_AUDIO = True  # Set True for standard positive-frequency audio WAV; False for 2-ch IQ WAV

    iq_data, fs = load_iq_wav(
        "/Users/khronos/baseband_pi.wav",
        is_real_audio=IS_REAL_AUDIO,
        swap_iq=False,
        reverse_time=False,
    )
    print(f"Loaded WAVE format (Real Audio={IS_REAL_AUDIO}): {len(iq_data)} samples at {fs} Hz")

    channels = find_candidate_channels(
        iq_data, fs, min_sep_hz=800.0, max_channels=4, is_real_audio=IS_REAL_AUDIO
    )
    print(f"Candidate channel centers (Hz): {[round(c, 1) for c in channels]}")

    all_detected_locks = []
    for ch_idx, center_hz in enumerate(channels):
        iq_ch, fs_ch = isolate_channel(iq_data, fs, center_hz, channel_bw=3500.0)
        est_baud, clk_snr = estimate_baud_rate(iq_ch, fs_ch, min_baud=30.0, max_baud=2500.0)
        print(f"Channel {ch_idx + 1} (@ {center_hz:.1f} Hz): Estimated Baud = {est_baud:.2f} Bd (Clock SNR = {clk_snr:.1f} dB)")

        if est_baud > 0 and clk_snr >= 10.0:
            ch_locks = detect_channel_locks(
                iq_ch, fs_ch, center_hz, est_baud,
                win_sec=0.75, hop_sec=0.05, core_snr_db=9.0, tail_snr_db=3.8,
            )
            all_detected_locks.extend(ch_locks)

    all_detected_locks.sort(key=lambda x: x)
    plot_tracks_with_nyquist_split(
        iq_data, fs, all_detected_locks, main_png="multi_baud_lock.png", is_real_audio=IS_REAL_AUDIO
    )
    all_detected_locks.sort(key=lambda x: x[0])
    plot_tracks_with_nyquist_split(
        iq_data, fs, all_detected_locks, main_png="multi_baud_lock.png", is_real_audio=IS_REAL_AUDIO
    )

    # Demodulate every locked region and write packed/unpacked bit files to ./demod_tracks/
    demodulate_locked_regions(iq_data, fs, all_detected_locks, output_dir="demod_tracks")

