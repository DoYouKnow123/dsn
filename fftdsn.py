import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import cv2
freq_0=8439500000

import cv2
import numpy as np
import sys
import scipy.io.wavfile as wavfile
import scipy.signal as signal  
    
# --- SENSOR CONFIGURATIONS ---
CAMERA_INDEX = 0
    

def compute_waterfall_data(signal, fft_size=1024, overlap=512):
    """
    Computes a 2D waterfall matrix (dB power) from a 1D signal stream.
    Works perfectly for both real arrays and complex IQ streams.
    """
    # 1. Calculate how many rows will fit given the overlap
    hop_size = fft_size - overlap
    num_rows = (len(signal) - fft_size) // hop_size + 1

    # 2. Slice the 1D signal into a 2D array of overlapping segments (No copies made)
    shape = (num_rows, fft_size)
    strides = (signal.strides[0] * hop_size, signal.strides[0])
    segments = np.lib.stride_tricks.as_strided(signal, shape=shape, strides=strides)

    # 3. Apply a window function to reduce side-lobes/spectral leakage
    window = np.hamming(fft_size)
    windowed_segments = segments * window

    # 4. Compute FFT across all rows at once
    fft_data = np.fft.fft(windowed_segments, n=fft_size, axis=-1)

    # 5. Shift frequencies so 0 Hz (or center frequency) is in the middle
    fft_shifted = np.fft.fftshift(fft_data, axes=-1)

    # 6. Convert the complex absolute magnitude to Decibels (dB Power)
    # Adding 1e-12 safely protects against log10(0) code crashes
    waterfall_matrix = 10 * np.log10(np.abs(fft_shifted) ** 2 + 1e-12)

    return waterfall_matrix

samples_per_symbol=8
# --- CONFIGURATION ---
SAMPLE_RATE = 2.0e6       # 2 MHz sample rate
FFT_SIZE = 1024           # Number of frequency bins
WATERFALL_DEPTH = 200     # Number of time rows to display on screen
DATA_TYPE = np.int16      # Use np.int16 for RTL-SDR / HackRF, np.float32 for float files
# ---------------------
FACTOR=8
# Each complex sample contains two values: I and Q
BYTES_PER_VALUE = 2
SAMPLE_CHUNK_SIZE = FFT_SIZE * 2  
BYTES_TO_READ = 4096

# Initialize an empty waterfall buffer matrix [Rows, Columns]
waterfall_data = np.zeros((WATERFALL_DEPTH, FFT_SIZE*FACTOR))
hanning_window = np.hanning(1024*FACTOR)

# Set up the Matplotlib plot window
fig, ax = plt.subplots(figsize=(10, 6))
freq_min = -1e6
freq_max = 1e6

# Render the initial blank image grid
im = ax.imshow(
    waterfall_data,
    extent=[freq_min, freq_max, 0, WATERFALL_DEPTH],
    origin='lower',
    aspect='auto',
    cmap='viridis',
    vmin=-40, vmax=60 # Adjust these thresholds to tweak color contrast
)

ax.set_title("Real-Time Stdin I/Q Waterfall")
ax.set_xlabel("Frequency (MHz)")
ax.set_ylabel("Time Matrix Window Rows")
fig.colorbar(im, label="Magnitude (dB)")
def update(frame):
    bit_accumulator = 0
    bit_counter = 0
    
    # Line grouping caches for formatted side-by-side printing
    hex_line_buffer = []
    ascii_line_buffer = []
    
    # Adaptive Clock tracking parameters
    samples_per_symbol = 8.0

    # Initialize the camera capture device via the Linux V4L2 backend
    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_AVFOUNDATION)
    if not cap.isOpened():
        print(f"Error: Optical sensor index {CAMERA_INDEX} failed to initialize.")
        return

    # Request High-Definition tracking grids
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
       
    # Enforce static exposure rules to stabilize horizontal harmonic line visibility
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
    cap.set(cv2.CAP_PROP_GAIN, 0)

    # Query the Linux driver to discover the actual hardware resolution granted
    actual_width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    

    ret, frame2 = cap.read()
    
     # Step 1: Isolate pure luminosity energy channels (Grayscale conversion)
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
            # Step 2: Dynamically center the processing slice relative to ACTUAL width
    center_x = actual_width // 2
    slice_half_width = 50
    if center_x - slice_half_width < 0:
        slice_half_width = center_x
            
    vertical_slice = gray[:, center_x - slice_half_width : center_x + slice_half_width]
    row_averages = np.mean(vertical_slice, axis=1)
    
            # Step 3: High-pass spatial filter to erase global room lighting gradients
    row_trend = np.convolve(row_averages, np.ones(15)/15, mode='same')
    spatial_harmonics = row_averages - row_trend
    spatial_harmonics3 = row_trend-row_averages   

    if np.std(spatial_harmonics) > 0.5:
        autocorr = np.correlate(spatial_harmonics, spatial_harmonics, mode='full')
        autocorr = autocorr[autocorr.size // 2:] // 2
                    
                # Fixed: Extract the 1-D indices immediately from the np.where tuple wrapper
        peaks_tuple = np.where((autocorr[1:-1] > autocorr[:-2]) & (autocorr[1:-1] > autocorr[2:]))
        peaks = peaks_tuple[0] + 1
                    
        # Fixed: Use length and explicit index zero extraction to safely check scalars
        if len(peaks) > 0 and peaks[0] > 2:
            first_peak = peaks[0]
            samples_per_symbol = 0.95 * samples_per_symbol + 0.05 * first_peak
              # Step 5: 1-D Spatial Phase-Locked Tracking Loop
    r = int(samples_per_symbol // 2)
    while r < actual_height:
        amplitude = spatial_harmonics[r]
            
                # Check phase against dynamic noise threshold bounds
                # Bright row element = Phase 0° (Bit 1), Dark row element = Phase 180° (Bit 0)
        if abs(amplitude) > 1.2:
            bit = 1 if amplitude > 0.0 else 0
            
                    # Clock alignment stabilization
            if r + 1 < actual_height and abs(spatial_harmonics[r+1]) > abs(amplitude):
                r += 1
            elif r - 1 >= 0 and abs(spatial_harmonics[r-1]) > abs(amplitude):
                r -= 1
        else:
            r += int(samples_per_symbol)
            continue
                
                  
                # Step 6: Accumulate Bits and Reconstruct ASCII Characters
        bit_accumulator = (bit_accumulator << 1) | bit
        bit_counter += 1
            
        if bit_counter == 8:
                    # Cache current byte into hex log
            hex_line_buffer.append(f"{bit_accumulator:02X}")
                    
                    # Decode to readable ASCII or display clean placeholder padding dots
            if 32 <= bit_accumulator <= 126:
                ascii_line_buffer.append(chr(bit_accumulator))
            else:
                ascii_line_buffer.append(".") # Placeholder for non-printable/sync characters
                    
                    # Standard 16-byte telemetry row layout alignment
            if len(hex_line_buffer) == 16:
                hex_string = " ".join(hex_line_buffer)
                ascii_string = "".join(ascii_line_buffer)
                        # Print structured telemetry side-by-side
                sys.stdout.write(f"{hex_string}  |  {ascii_string}\n")
                sys.stdout.flush()
                
                hex_line_buffer.clear()
                ascii_line_buffer.clear()
            
            bit_accumulator = 0
            bit_counter = 0
                    
        r += int(samples_per_symbol)
                    
            # Draw visual processing feedback overlay using actual dimensions
    cv2.rectangle(frame2, (center_x - slice_half_width, 0), (center_x + slice_half_width, actual_height), (0, 255, 0), 2)
    cv2.putText(frame2, f"Symbol Rows: {samples_per_symbol:.1f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)                
    cv2.imshow("Optical Radio Monitoring Matrix", frame2)
                    


    freq3=[]
    print(f"frame: {frame}")
    global waterfall_data
    # 1. Read exactly one FFT block size of raw data from standard input
    t=np.arange(2048*frame,2048*(frame+1024*FACTOR),2048)
    print(f"lent: {t}")
    print(t.itemsize)                
    [rate2,dx] = wavfile.read('mapping2.wav')
    dx2 = signal.resample(dx,8192)
    
    freq = 0.7*((2/np.pi)*np.arcsin(np.sin(np.pi*np.sin(2*np.pi*t*(np.sin(freq_0*2*np.pi*t)*(dx2*t))-t)))+(2/np.pi)*np.arcsin(np.sin(0.4*np.pi*np.sin(2*np.pi*t*np.sin(freq_0*2*np.pi*t)*((dx2*t))-t))))
 #   freq0 = 0.7*((2/np.pi)*np.arcsin(np.sin(np.pi*np.sin(2*np.pi*(t-(np.sin(2*np.pi*dx2*t-(np.pi/2))))))+(2/np.pi)*np.arcsin(np.sin(0.4*np.pi*np.sin(2*np.pi*(t-((np.sin(dx2*2*np.pi*t-(np.pi/2))))))))))
   # freq2 = 0.7*((2/np.pi)*np.arcsin(np.sin(np.pi*np.sin(2*np.pi*freq_0*(t)))+(2/np.pi)*np.arcsin(np.sin(0.4*np.pi*np.sin(2*np.pi*freq_0*(t)))))-(2/np.pi)*np.arcsin(np.sin(np.pi*(2*np.pi*dx2*freq_0*t))))
   # freq = 0.7*((2/np.pi)*np.arcsin(np.sin(np.pi*np.sin(2*np.pi*freq_0*t-t)))+(2/np.pi)*np.arcsin(np.sin(0.4*np.pi*np.sin(2*np.pi*freq_0*t-t))))
    repeated_array = np.tile(dx, len(freq) // len(dx) + 1)[:len(freq)]
    spatial_harmonics2=(spatial_harmonics[:1080]*0.8)+(0.2*(spatial_harmonics[:1080]*dx[:1080]+dx[:1080]*repeated_array[:1080]))
    spatial_harmonics3=spatial_harmonics3[-1:]
    raw_bytes=np.empty(len(freq) + len(spatial_harmonics))
    raw_bytes[0::2]=signal.resample(spatial_harmonics2,len(raw_bytes[0::2]))
    raw_bytes[1::2]=signal.resample(freq[:1080]*spatial_harmonics3[:1080], len(raw_bytes[0::2]))
    print(f"raw_bytes, {raw_bytes}")
#    raw_bytes = freq3[frame:frame+1]
#    raw_bytes = sys.stdin.buffer.read(BYTES_TO_READ)
    print(len(raw_bytes))    
    # Exit if stdin stream ends or gets interrupted
#    if len(raw_bytes) < 4096:
#        return [im]
        
    # 2. Unpack binary bytes into raw array numbers
#    converted_chunk = np.frombuffer(raw_bytes, dtype=DATA_TYPE)
 #   iq_chunk[np.isnan(iq_chunk)] = 0.0

    # 3. Interleave individual elements to construct complex array (I + jQ)
    # Cast to float64 so the math functions don't truncate values
    iq_chunk = raw_bytes[0::2] + 1j * raw_bytes[1::2]
    iq_chunk=signal.resample(raw_bytes,8192) 
    
    # 4. Apply windowing to mitigate edge leakage distortion
    windowed_chunk = iq_chunk * hanning_window
    
    # 5. Compute FFT and realign center frequencies
    fft_output = np.fft.fftshift(np.fft.fft(windowed_chunk))
    fft_output[np.isnan(fft_output)] = 0.0
    print(f"fftoutput: {fft_output}")
    magnitude_db = 20 * np.log10(np.abs(fft_output) + 1e-10)
#    bg_average = None
#    ALPHA = 0.5  # Adaptation rate (0.01 = slow change, 0.2 = fast change)

#    if bg_average is None:
#         bg_average = np.copy(magnitude_db)
#    else:
#         # Exponential moving average formula
#         bg_average = (1 - ALPHA) * bg_average + ALPHA * magnitude_db
        
    # 3. Subtract the background to remove static carriers
    # This centers the noise floor around 0 dB, stripping out vertical lines
 #   clean_magnitude = magnitude_db - bg_average    
    # 6. Shift rows down to create a scrolling waterfall effect
    waterfall_data = np.roll(waterfall_data, -1, axis=0)
    waterfall_data[-1, :] = magnitude_db  # Insert newest line at bottom row
    
    # 7. Update image array container graphics data
    im.set_array(waterfall_data)
    return [im]

# Run live drawing loop configuration
ani = FuncAnimation(fig, update, blit=True, interval=10, save_count=1)
plt.show()

