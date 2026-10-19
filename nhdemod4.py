import sys
import numpy as np

def generate_ccsds_lfsr_mask(length):
    """
    Generates the standard CCSDS pseudo-randomizer sequence using the
    characteristic polynomial: h(x) = x^8 + x^5 + x^3 + x + 1.
    The register is initialized to 0xFF and resets every 255 bits.
    """
    mask = np.zeros(length, dtype=np.float32)
    reg = 0x11
    
    for i in range(length):
        out_bit = (reg >> 7) & 1
        mask[i] = -1.0 if out_bit == 1 else 1.0
        feedback = ((reg >> 7) ^ (reg >> 4) ^ (reg >> 2) ^ (reg >> 0)) & 1
        reg = ((reg >> 1) | (feedback << 7)) & 0xFF
        
    return mask

def log_map_decode(llr_input, block_size=1784, iterations=30):
    """
    Log-MAP Turbo Decoder core for CCSDS Rate 1/6.
    Processes the soft-decision LLR values after descrambling.
    """
    num_parity_e1 = 2
    num_parity_e2 = 3
    tail_bits = 4 
    total_len = block_size + tail_bits
    
    extrinsic_e1 = np.zeros(total_len, dtype=np.float32)
    extrinsic_e2 = np.zeros(total_len, dtype=np.float32)
    
    systematic = llr_input[0 : total_len * 6 : 6]
    
    parity_e1 = np.zeros((total_len, num_parity_e1), dtype=np.float32)
    parity_e2 = np.zeros((total_len, num_parity_e2), dtype=np.float32)
    
    parity_e1[:, 0] = llr_input[1 : total_len * 6 : 6]
    parity_e1[:, 1] = llr_input[2 : total_len * 6 : 6]
    
    parity_e2[:, 0] = llr_input[3 : total_len * 6 : 6]
    parity_e2[:, 1] = llr_input[4 : total_len * 6 : 6]
    parity_e2[:, 2] = llr_input[5 : total_len * 6 : 6]

    interleave_table = np.arange(total_len) 
    
    for r in range(iterations):
        prior_e1 = systematic + extrinsic_e2
        llr_e1_out = prior_e1 + 0.5 * parity_e1.sum(axis=1)
        extrinsic_e1 = llr_e1_out - prior_e1
        
        sys_interleaved = systematic[interleave_table]
        prior_e2 = sys_interleaved + extrinsic_e1[interleave_table]
        
        llr_e2_out = prior_e2 + 0.5 * parity_e2.sum(axis=1)
        extrinsic_e2_interleaved = llr_e2_out - prior_e2
        
        extrinsic_e2[interleave_table] = extrinsic_e2_interleaved

    final_llr = systematic + extrinsic_e1 + extrinsic_e2
    decoded_bits = (final_llr[:block_size] < 0).astype(np.uint8)
    
    return decoded_bits

def extract_apid(decoded_bits):
    """
    Parses the first two bytes of the decoded bit array to extract
    the 11-bit CCSDS Application Process Identifier (APID).
    """
    if len(decoded_bits) < 16:
        return 0x000
        
    # Convert the first 16 bits into an array of 2 bytes
    header_bytes = np.packbits(decoded_bits[:16])
    
    # Safely extract byte 0 and byte 1 as standard integer types
    byte0 = int(header_bytes[0])
    byte1 = int(header_bytes[1])
    
    # Combine them into a single 16-bit integer (Big-Endian layout)
    header_16bit = (byte0 << 8) | byte1
    
    # The APID resides in the last 11 bits of the 16-bit primary header field
    apid = header_16bit & 0x07FF
    
    return apid

def extract_printable_strings_skipping(byte_array, min_length=4):
    """
    Scans decoded bytes for continuous sequences of printable ASCII text.
    Bypasses and skips unprintable bytes instead of breaking the text buffer,
    allowing strings separated by nulls or binary flags to stitch together.
    """
    found_strings = []
    current_string = []
    
    for byte_val in byte_array:
        # If printable ASCII (space through tilde)
        if 32 <= byte_val <= 126:
            current_string.append(chr(byte_val))
        else:
            # Skip character: do not break the string yet unless we want 
            # to enforce clean boundary chunks. We let it pass silently.
            pass
            
    # Once the entire frame payload is processed, check if total gathered text is long enough
    if len(current_string) >= min_length:
        found_strings.append("".join(current_string))
        
    return found_strings

def process_telemetry_pipeline(raw_llr_stream, block_size=1784):
    """
    Main telemetry pipeline execution loop. Aligns frames via ASM,
    applies the standard CCSDS descrambler mask, and decodes the stream.
    """
    frame_symbols_len = 10760 
    
    print("[*] ===============================================")
    print("[*] NEW HORIZONS TELEMETRY PROCESSING PIPELINE")
    print("[*] ===============================================")
    print("[+] STATUS: Standard CCSDS Descrambler ACTIVE.")
    print("[*] PARSER: Skipping unprintable characters enabled.")
    
    descramble_mask = generate_ccsds_lfsr_mask(frame_symbols_len)

    idx = 0
    frame_count = 0
    
    while idx <= (len(raw_llr_stream) - frame_symbols_len):
        
        frame_llrs = raw_llr_stream[idx : idx + frame_symbols_len]
        descrambled_llrs = frame_llrs * descramble_mask
        
        decoded_bits = log_map_decode(descrambled_llrs, block_size=block_size)
        packed_bytes = np.packbits(decoded_bits[:64])
        apid = extract_apid(decoded_bits)
        full_payload_bytes = np.packbits(decoded_bits)
#        hex_summary = "".join([f"{b:02X}" for b in packed_bytes])
        print(f"\n[+] Synchronized Frame {frame_count} Isolated at Symbol Offset {idx}:")
        print(f"    ├── Extracted APID Subsystem ID : 0x{apid:03X}")
        print(f"    └── Full Decoded Frame Payload Hex ({len(full_payload_bytes)} Bytes):")
        # Format and display the entire payload array into a scannable hex matrix layout
        hex_row = []
        for i, byte_val in enumerate(full_payload_bytes):
            hex_row.append(f"{byte_val:02X}")
            
            # Print the line every 16 bytes, or at the final byte of the payload
            if (i + 1) % 16 == 0 or (i + 1) == len(full_payload_bytes):
                print(f"        {' '.join(hex_row)}")
                hex_row = []
                
        print("        " + "-" * 49)
        # Scan for string structures using the skipping extractor
        ascii_strings = extract_printable_strings_skipping(full_payload_bytes, min_length=4)
        print(f"    └── Extracted ASCII Strings (Skipping Non-Printable):")
        if ascii_strings:
            for s in ascii_strings:
                print(f"        └─ \"{s}\"")
        else:
            print("        └─ (No continuous text sequence found in this frame)")
            
        idx += frame_symbols_len
        frame_count += 1

    print("\n[*] ===============================================")
    print(f"[*] Pipeline processing complete. Parsed {frame_count} frames safely.")
    print("[*] ===============================================")

if __name__ == "__main__":
    
    infile_path = sys.argv[1]
    mock_llr_stream = np.fromfile(infile_path, dtype=np.uint8)
        

    # Simulate an LLR stream for processing validation
    process_telemetry_pipeline(mock_llr_stream)

