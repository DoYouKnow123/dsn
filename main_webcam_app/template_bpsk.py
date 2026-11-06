import cv2
import numpy as np
import sys
import scipy.io.wavfile as wavfile
import scipy.signal as signal
freq_0=8339500000

# --- SENSOR CONFIGURATIONS ---
CAMERA_INDEX = 0

def extract_row_telemetry_stream():
    # Initialize the camera capture device via the Linux V4L2 backend
    cap = cv2.VideoCapture("/dev/video2", cv2.CAP_V4L2)
    if not cap.isOpened():
        print(f"Error: Optical sensor index {CAMERA_INDEX} failed to initialize.")
        return

    # Request High-Definition tracking grids
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # Enforce static exposure rules to stabilize horizontal harmonic line visibility
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1) 
    cap.set(cv2.CAP_PROP_GAIN, 0)          

    # Query the Linux driver to discover the actual hardware resolution granted
    actual_width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print("=====================================================================")
    print("   REAL-TIME ROLLING SHUTTER HARMONIC S-BAND BPSK DEMODULATOR        ")
    print("=====================================================================")
    print(f"Hardware Granted Resolution : {actual_width} x {actual_height}")
    print("Target Environmental Setup  : Defocused lens, aimed at flat surface")
    print("Processing line-scan harmonic phase transitions into text payloads...\n")

    bit_accumulator = 0
    bit_counter = 0
    
    # Line grouping caches for formatted side-by-side printing
    hex_line_buffer = []
    ascii_line_buffer = []
    
    # Adaptive Clock tracking parameters
    samples_per_symbol = 8.0 

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Step 1: Isolate pure luminosity energy channels (Grayscale conversion)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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
            t=np.arange(0,40,len(spatial_harmonics))
            
            [rate2,dx] = wavfile.read('mapping2.wav')
            dx2=signal.resample(dx,len(t))
            freq = 0.7*((2/np.pi)*np.arcsin(np.sin(np.pi*np.sin(2*np.pi*spatial_harmonics*t*(np.sin(freq_0*2*np.pi*t)+dx2)-t)))+(2/np.pi)*np.arcsin(np.sin(0.4*np.pi*np.sin(2*np.pi*spatial_harmonics*t*np.sin(freq_0*2*np.pi*t)+dx2-t))))
#            freq2 = 0.7*((2/np.pi)*np.arcsin(np.sin(np.pi*np.sin(2*np.pi*freq_0*t*t-t)))+(2/np.pi)*np.arcsin(np.sin(0.4*np.pi*np.sin(2*np.pi*freq_0*t*t-t))))
             
            freq = freq - spatial_harmonics
            #repeated_array = np.tile(dx, len(freq) // len(dx) + 1)[:len(freq)]
            #spatial_harmonics=0.2*spatial_harmonics+(0.8*freq)*spatial_harmonics
#            spatial_harmonics=spatial_harmonics/np.max(spatial_harmonics)
            # Step 4: FIXED SPATIAL AUTO-CORRELATION LOOP
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
            cv2.rectangle(frame, (center_x - slice_half_width, 0), (center_x + slice_half_width, actual_height), (0, 255, 0), 2)
            cv2.putText(frame, f"Symbol Rows: {samples_per_symbol:.1f}", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cv2.imshow("Optical Radio Monitoring Matrix", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nDemodulator pipeline halted via manual terminal override.")
    finally:
        # Flush out any leftover partial trailing byte lines upon termination
        if hex_line_buffer:
            hex_string = " ".join(hex_line_buffer).ljust(47) # Keep vertical layout column strict
            ascii_string = "".join(ascii_line_buffer)
            sys.stdout.write(f"{hex_string}  |  {ascii_string}\n")
            
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    extract_row_telemetry_stream()
