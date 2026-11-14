import cv2
import numpy as np
import sys
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import io
import random
from picamera2 import Picamera2
from scipy.fft import fft2, ifft2, fftshift, ifftshift
from scipy.signal import hilbert

def triangular_window_2d(M, N):
    """Generates a 2D triangular (Bartlett) window to isolate a local spatial region."""
    y = np.bartlett(M)
    x = np.bartlett(N)
    return np.outer(y, x)

def adaptive_holographic_2d_concentrate(tf_matrix, target_center, region_size, concentration_factor=60):
    """
    Applies a 2D triangular-wave windowed holographic kernel to focus diffuse energy.
    Dynamically scales bin sizes based on local coordinate scales.
    """
    M, N = tf_matrix.shape
    r_center, c_center = target_center
    r_size, c_size = region_size
    
    # 1. Isolate the target 2D region using a localized triangular mask
    mask = np.zeros((M, N))
    tri_window = triangular_window_2d(r_size, c_size)
    
    # Slice limits for the 2D region
    r_start = max(0, r_center - r_size // 2)
    r_end = min(M, r_start + r_size)
    c_start = max(0, c_center - c_size // 2)
    c_end = min(N, c_start + c_size)
    
    # Adapt slices if they hit edges
    w_r_slice = slice(0, r_end - r_start)
    w_c_slice = slice(0, c_end - c_start)
    mask[r_start:r_end, c_start:c_end] = tri_window[w_r_slice, w_c_slice]
    
    # Isolate region phase properties
    isolated_region = tf_matrix * mask
    region_phase = np.angle(isolated_region)
    
    # 2. Adaptive Bin Size Modulation (Resolution Scaling)
    # Generate 2D coordinate spaces centered on the target region
    Y, X = np.ogrid[-r_center:M-r_center, -c_center:N-c_center]
    
    # As frequency index (Y) increases, shrink the bin scaling factor
    linear_gradient_y = 1.0 - (np.abs(Y) / M)
    linear_gradient_x = 1.0 - (np.abs(X) / N)
    adaptive_bin_scale = np.outer(linear_gradient_y.ravel(), linear_gradient_x.ravel())
    
    # 3. Holographic Lens Application
    holographic_phase = -1.0 * region_phase * concentration_factor * adaptive_bin_scale
    holographic_kernel = np.exp(1j * holographic_phase)
    
    # Apply forward diffractive focus across the 2D canvas
    focused_region = isolated_region * holographic_kernel
    
    # 4. 2D Spectral Compression (Collapsing diffuse energy via 2D Fourier plane)
    spectrum_2d = fftshift(fft2(focused_region))
    
    # Squeeze bin sizes globally via quadratic-triangular phase scaling in the frequency domain
    V, U = np.ogrid[-M//2:M//2, -N//2:N//2]
    compression_lens = np.exp(-1j * np.pi * (V**2 + U**2) * (1.0 / (concentration_factor + 1e-5)))
    
    compressed_spectrum = spectrum_2d * compression_lens
    concentrated_tf_matrix = ifft2(ifftshift(compressed_spectrum))
    
    # Re-insert concentrated block back into original matrix structure
    output_matrix = tf_matrix.copy()
    output_matrix[r_start:r_end, c_start:c_end] = concentrated_tf_matrix[r_start:r_end, c_start:c_end]
    
    return output_matrix, holographic_kernel, compression_lens, (r_start, r_end, c_start, c_end)

def adaptive_holographic_2d_reconstruct(concentrated_matrix, holo_kernel, comp_lens, boundaries):
    """Reverses the 2D phase-energy compression for a zero-distortion audio return."""
    r_start, r_end, c_start, c_end = boundaries
    target_block = concentrated_matrix[r_start:r_end, c_start:c_end]
    
    # 1. Reverse 2D spectral compression
    spectrum_2d = fftshift(fft2(target_block))
    uncompressed_spectrum = spectrum_2d * np.conj(comp_lens[r_start:r_end, c_start:c_end])
    restored_block = ifft2(ifftshift(uncompressed_spectrum))
    
    # 2. Reverse localized holographic phase
    decoded_block = restored_block * np.conj(holo_kernel[r_start:r_end, c_start:c_end])
    
    output_matrix = concentrated_matrix.copy()
    output_matrix[r_start:r_end, c_start:c_end] = decoded_block
    return output_matrix

# --- SENSOR CONFIGURATIONS ---
CAMERA_INDEX = 14

def add_random_n_places(a, n):
    out = a.astype(float)
    random_values = np.random.uniform(low=-1, high=1, size=n)
    for idx, val in zip(range(0, len(out) - 1), random_values):
        out = np.insert(out, idx, val)
    return out

def extract_row_telemetry_stream(freq_0=8439500000):
    freq_0=int(freq_0)
    sensor_f0 = 25000000
    sensor_x = 2592
    sensor_y = 1944
    freq_1 = (freq_0 / (sensor_f0 / (sensor_x * sensor_y)))
#    print(1/(sensor_f0 / (sensor_x * sensor_y)))
    # Wrap Picamera2 inside a context manager (auto-replaces cap.release())
    with Picamera2() as picam:
        # Configure resolution and format
        config = picam.create_video_configuration(
            raw={"size": (2592,1944), "format": "SGBRG10_CSI2P"}
        )
        picam.configure(config)

        # Set manual exposure controls 
        picam.set_controls({
            "AeEnable": False,
            "AnalogueGain": 1.0,
            "ExposureTime": 20000  # Exposure time in microseconds
        })

        # Start the camera stream
        picam.start()
        frame_rate = config["raw"]["fps"] if "fps" in config["raw"] else 30.0
        # Fix: Safely extract dimensions from the Picamera2 configuration tuple
        actual_width = config["raw"]["size"][0]
        actual_height = config["raw"]["size"][1]

        print("=====================================================================")
        print("   REAL-TIME ROLLING SHUTTER HARMONIC S-BAND BPSK DEMODULATOR        ")
        print("=====================================================================")
        print(f"Hardware Granted Resolution : {actual_width} x {actual_height}")
        print("Target Environmental Setup  : Defocused lens, aimed at flat surface")
        print("Processing line-scan harmonic phase transitions into text payloads...\n")
        
        hex_line_buffer = []
        ascii_line_buffer = []
        
        # Adaptive Clock tracking parameters
        samples_per_symbol = 8.0
        binary_data = io.BytesIO()

        # Fix: Initialize counters before the capture loop to avoid UnboundLocalError
        bit_accumulator = 0
        bit_counter = 0
        framectr = 0
        # Read the mapping file once outside the frame processing loop for optimization
        try:
            rate2, dx = wavfile.read('mapping2.wav')
        except FileNotFoundError:
            print("Warning: 'mapping2.wav' not found. Using fallback zero-array mapping.")
            rate2, dx = 44100, np.zeros(1080)

        try:
            while True:
                # Capture a single frame from the Picamera2 stream
                frame_data = picam.capture_array("raw")
                framectr = (framectr + 1)
                # Extract Y (Luminance) channel 
                gray = frame_data[:, :, 0] if len(frame_data.shape) == 3 else frame_data

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
 #               secs=40
 #               t = np.linspace(0, secs, len(spatial_harmonics))
              #  print(t2[1]-t2[0])
  #            #  frame_rate=cv2.CAP_PROP_FPS
                t=np.linspace(0,len(spatial_harmonics)/(sensor_x*sensor_y),len(spatial_harmonics))   
    #            factor_res=103680
    #            t=(t*factor_res)
#                print((t2[1]-t2[0])/(t[1]-t[0]))
#                t=np.arange(0,40,len(spatial_harmonics))  
                [rate2,dx] = wavfile.read('mapping2.wav')
           # secs=(len(spatial_harmonics)/rate2)
#            t=np.linspace(0,secs,len(spatial_harmonics))
                dx2=signal.resample(dx,len(t))
#            print(dx)
#            print(t)
#            print(dx2)
               # print(freq_1)
     #           factor=4.96145150638
#                print(((freq_0 * factor) / (sensor_f0 / (sensor_x * sensor_y))))
              #  freq_1=freq_1*4.96145150638
              #  print(freq_1)
             #   print(freq_1)

#                freq = ((2/np.pi)*np.arcsin(np.sin(np.pi*np.sin(2*np.pi*freq_0*t))))
                freq = np.sin(2*np.pi*300*t)*(0.7*((2/np.pi)*np.arcsin(np.sin(np.pi*np.sin(2*np.pi*spatial_harmonics*t*(np.sin(freq_1*2*np.pi*t)+dx2)-t)))+(2/np.pi)*np.arcsin(np.sin(0.4*np.pi*np.sin(2*np.pi*spatial_harmonics*t*np.sin(freq_1*2*np.pi*t)+dx2-t)))))
                freq=freq/np.max(freq)
#                freq = 0.7*((2/np.pi)*np.arcsin(np.sin(np.pi*np.sin(2*np.pi*freq_0*t))))
#            print(freq_1)
#                dx3=dx2[(((freq+1)/2).astype(int)*len(freq))]+(freq).astype(float)
#            print(dx3)
#            print(len(dx3))
#            print((freq+1)/2)
                spatial_harmonics=0.2*spatial_harmonics+(0.8*freq)*spatial_harmonics
 #               spatial_harmonics=0.6*((dx3*freq+freq)/np.max(dx3*freq+freq))+0.4*spatial_harmonics


                # Step 4: FIXED SPATIAL AUTO-CORRELATION LOOP
                if np.std(spatial_harmonics) > 0.5:
                    autocorr = np.correlate(spatial_harmonics, spatial_harmonics, mode='full')
                    autocorr = autocorr[autocorr.size // 2:] // 2
                    
                    peaks_tuple = np.where((autocorr[1:-1] > autocorr[:-2]) & (autocorr[1:-1] > autocorr[2:]))
                    peaks = peaks_tuple[0] + 1  
                    
                    if len(peaks) > 0 and peaks[0] > 2:
                        first_peak = peaks[0]
                        samples_per_symbol = 0.95 * samples_per_symbol + 0.05 * first_peak

                # Step 5: 1-D Spatial Phase-Locked Tracking Loop (Adaptive Signal Threshold)
                r = int(samples_per_symbol // 2)
                
                # Dynamically set a threshold based on current frame noise rather than hardcoded 1.2
                dynamic_threshold = max(0.1, np.std(spatial_harmonics) * 0.5)

                while r < actual_height:
                    amplitude = spatial_harmonics[r]
                    
                    if abs(amplitude) > dynamic_threshold:
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
                        hex_line_buffer.append(f"{bit_accumulator:02X}")
                        
                        if 32 <= bit_accumulator <= 126:
                            ascii_line_buffer.append(chr(bit_accumulator))
                        else:
                            ascii_line_buffer.append(".")
                            
                        # Show raw tracking feedback immediately on screen so you know it's working
#                        print(f"[{ascii_line_buffer[-1]}]", end="", flush=True)
                            
                        if len(hex_line_buffer) == 16:
                            hex_string = " ".join(hex_line_buffer)
                            ascii_string = "".join(ascii_line_buffer)
                            # Print standard completed data payload line
                            print(f"\n{hex_string}  | {ascii_string} |")
                            with open("ccsds.log", "a") as f:
                                f.write(f"\n{hex_string}  | {ascii_string} |")
                            # Commit payload stream segments to file
                            binary_data.write(bytes.fromhex(''.join(hex_line_buffer)))
                            uint8_data = np.frombuffer(binary_data.getvalue(), dtype=np.uint8)
                            signal_norm = uint8_data/np.max(uint8_data)

    # Convert 1D time audio into 2D Time-Frequency Image space
                            print("Computing forward Short-Time Fourier Transform (STFT)...")
                            frequencies, times, stft_matrix = signal.stft(signal_norm, fs=rate2, nperseg=16)
    
       # Set the target focus region parameters (targeting center bins of the matrix canvas)
                            target_bin = (stft_matrix.shape[0] // 2, stft_matrix.shape[1] // 2)
    
    # Define window bounds (Height=Frequency bins, Width=Time frames)
    # Scales dynamically to fit inside the computed STFT canvas sizes
                            r_size = min(256, stft_matrix.shape[0])
                            c_size = min(64, stft_matrix.shape[1])
                            region_dimensions = (r_size, c_size)
                            concentration_factor=60
                            print(f"Applying 2D Adaptive Triangular Holographic focus (Factor: {concentration_factor})...")
                            concentrated_image, kernel, lens, bounds = adaptive_holographic_2d_concentrate(
                        stft_matrix, target_bin, region_dimensions, concentration_factor=60
                        )
    
                            print("Executing perfect inversion loop reconstruction...")
                            restored_image = adaptive_holographic_2d_reconstruct(concentrated_image, kernel, lens, bounds)
    
    # Invert image coordinates back down to 1D time audio wave
                            _, reconstructed_audio = signal.istft(restored_image, fs=44100, nperseg=16)
    
    # Re-normalize and convert back into standard audio 16-bit PCM integer scaling to prevent digital clipping
                            print("Normalizing final signal and formatting bit depth...")
                            reconstructed_audio = reconstructed_audio / np.max(np.abs(reconstructed_audio))
                            freq_shift = 0.5*rate2/2
                            t = np.arange(len(reconstructed_audio))/rate2
#                            analytic_signal = hilbert(reconstructed_audio)
#                            mixer = analytic_signal * np.exp(1j * 2 * np.pi * freq_shift * t)
#                            iq_shifted = (reconstructed_audio*mixer)
#                            peak = np.max(np.abs(iq_shifted))
 #                           if peak > 0:
  #                              iq_shifted = iq_shifted / peak
 #                           stereo_iq = np.column_stack((iq_shifted.real, -np.cos(2*np.pi*300*t)*iq_shifted.imag))
# Compute the FFT of the shifted signal
                            audio_to_save = (np.clip(reconstructed_audio, -1.0, 1.0) * 32767).astype(np.int16)
                            wavfile.write("baseband.wav", rate2, audio_to_save)
                            with open("telemetry_output.bin", "wb") as f:
                                uint8_data.tofile(f)
                              #  print("Telemetry trace successfully committed to 'iq.wav'.")

                            # Clean up row buffers for the next 16 bytes
                            hex_line_buffer.clear()
                            ascii_line_buffer.clear()
                        
                        # Reset bit processors for next byte sequence
                        bit_accumulator = 0
                        bit_counter = 0
                    
                    r += int(samples_per_symbol)

        except KeyboardInterrupt:
            print("\nStream stopped by user. Flushing tracking logs...")
            # Save final tracking file data
          #  binary_data.seek(0)
          #  raw_payload = binary_data.read()
         #   if len(raw_payload) > 0:
             #   audio_data = np.frombuffer(raw_payload, dtype=np.uint8)
           #     uint8_data = np.array(raw_payload, dtype=np.uint8)
           #     with open("telemetry_output.bin", "ab") as f:
           #         uint8_data.tofile(f)
            #    print("Telemetry trace successfully committed to 'iq.wav'.")

if __name__ == "__main__":
    if len(sys.argv) < 2: 
        sys.exit(1)


    extract_row_telemetry_stream(sys.argv[1])
