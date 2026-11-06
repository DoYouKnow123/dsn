import struct
import collections
import numpy as np
from PIL import Image

# CCSDS Constants
CCSDS_HEADER_SIZE = 6

def extract_streams_by_scid(binary_file_path):
    """
    Pass 1: Parses the binary frame dump and aggregates packets 
    into contiguous payload streams indexed by Spacecraft ID (SCID).
    """
    spacecraft_streams = collections.defaultdict(bytearray)
    
    with open(binary_file_path, "rb") as f:
        while True:
            header = f.read(CCSDS_HEADER_SIZE)
            if len(header) < CCSDS_HEADER_SIZE:
                break
            
            p_hdr1, p_hdr2, data_len = struct.unpack(">HHH", header)
            scid = (p_hdr1 >> 4) & 0xFF 
            
            actual_data_len = data_len + 1
            packet_data = f.read(actual_data_len)
            if len(packet_data) < actual_data_len:
                break
                
            spacecraft_streams[scid].extend(packet_data)
            
    return spacecraft_streams

def find_dimensions_via_autocorrelation(payload_bytes, min_width=256, max_width=2048):
    """
    Pass 2: Detects the raster image stride (width) using 1D autocorrelation,
    then automatically adjusts the height to fit the total data size.
    """
    # Convert raw bytes into a 1D NumPy array of 8-bit unsigned integers
    data_array = np.frombuffer(payload_bytes, dtype=np.uint8)
    total_pixels = len(data_array)
    
    if total_pixels < min_width:
        raise ValueError(f"Payload too small ({total_pixels} bytes) for dimension estimation.")

    # Subsample data if it's too large to accelerate computation
    # Analyzing the first 512KB is typically more than enough to find the row stride
    sample_size = min(total_pixels, 524288)
    signal = data_array[:sample_size].astype(np.float32)
    
    # De-mean the signal to remove DC offset for cleaner correlation peaks
    signal -= np.mean(signal)
    
    print(f"[*] Analyzing telemetry periodicity (searching width between {min_width}px and {max_width}px)...")
    
    best_peak_lag = min_width
    max_correlation = -1.0
    
    # Evaluate lags within the expected engineering camera width boundaries
    for lag in range(min_width, min(max_width, sample_size // 2)):
        # Calculate the dot product between the signal and its time-shifted self
        correlation = np.dot(signal[:-lag], signal[lag:])
        
        # Track the absolute maximum peak within the search window
        if correlation > max_correlation:
            max_correlation = correlation
            best_peak_lag = lag

    detected_width = best_peak_lag
    
    # Automatically adjust height based on the discovered width
    detected_height = total_pixels // detected_width
    
    # Calculate tracking remainder to catch truncated frames
    remainder = total_pixels % detected_width
    if remainder != 0:
        print(f"[-] Warning: Stream length not perfectly divisible by width. Remainder: {remainder} bytes.")
        
    print(f"[+] Autocorrelation Peak Detected! Autodetected Grid: {detected_width} x {detected_height}")
    return detected_width, detected_height

def process_and_save_mars_telemetry(raw_binary_dump, output_prefix="scid_out"):
    """
    Orchestrates extraction, signal analysis, dimension adjustment, and saving.
    """
    scid_streams = extract_streams_by_scid(raw_binary_dump)
    
    if not scid_streams:
        print("[-] No valid streams resolved from telemetry binary file.")
        return

    for scid, payload in scid_streams.items():
        print(f"\n[+] Processing Contiguous Stream for SCID: {scid} ({len(payload)} bytes)")
        
        try:
            # Drop hypothetical header bytes if parsing raw ICER payload directly
            # Change payload offset slice if payload contains telemetry wrap headers
            raw_raster_payload = bytes(payload)
            
            # Find dimensions dynamically via signal analysis
            width, height = find_dimensions_via_autocorrelation(raw_raster_payload)
            
            # Truncate stream down to the exact calculated pixel grid matrix size
            valid_pixel_bytes = width * height
            pixel_data = raw_raster_payload[:valid_pixel_bytes]
            
            # Reconstruct raster grid into a grayscale image matrix
            img = Image.frombytes("L", (width, height), pixel_data)
            
            # Convert and save as standard JPEG layout
            output_filename = f"{output_prefix}_{scid}_latest.jpg"
            img.save(output_filename, "JPEG", quality=95)
            print(f"[+] Success: Stored SCID {scid} Hazcam asset into {output_filename}")
            
        except Exception as e:
            print(f"[-] Failed to decode stream for SCID {scid}: {e}")

# Example invocation:
process_and_save_mars_telemetry("turbodecoded.bak")
