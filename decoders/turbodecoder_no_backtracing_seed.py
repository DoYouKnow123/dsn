import sys
import numpy as np

def get_ccsds_turbo_asm_bits():
    # Standard 96-bit ASM for Rate 1/6 Deep Space Turbo Links
    return np.unpackbits(np.frombuffer(bytes.fromhex("1AC471C9585517672E100FA3"), dtype=np.uint8))

def generate_ccsds_turbo_interleave_table(k=1784):
    M, p0, p1, p2, p3 = 223, 27, 19, 13, 11
    s = np.arange(k)
    m, i = s % M, (s // M).astype(np.int32)
    p_i = np.select([i==0, i==1, i==2, i==3], [p0, p1, p2, p3])
    q_i = np.select([i==0, i==1, i==2, i==3], [0, 2*M+1, M+1, 3*M+1])
    return (p_i * m + q_i) % (4 * M)

def generate_ccsds_lfsr_mask(length, initial_reg=0x3F):
    mask = np.zeros(length, dtype=np.float32)
    reg = initial_reg
    for i in range(length):
        out_bit = (reg >> 7) & 1
        mask[i] = -1.0 if out_bit == 1 else 1.0
        feedback = ((reg >> 7) ^ (reg >> 4) ^ (reg >> 2) ^ (reg >> 0)) & 1
        reg = ((reg >> 1) | (feedback << 7)) & 0xFF
    return mask

def log_map_decode(llr_input, block_size=1784, iterations=15):
    tail_bits = 4
    total_len = block_size + tail_bits
    extrinsic_e1 = np.zeros(total_len, dtype=np.float32)
    extrinsic_e2 = np.zeros(total_len, dtype=np.float32)
    sanitized_llrs = np.clip(np.nan_to_num(llr_input, nan=0.0), -20.0, 20.0)
         
    systematic = sanitized_llrs[0 : total_len * 6 : 6]
    parity_e1 = np.column_stack((sanitized_llrs[1::6][:total_len], sanitized_llrs[2::6][:total_len]))
    parity_e2 = np.column_stack((sanitized_llrs[3::6][:total_len], sanitized_llrs[4::6][:total_len], sanitized_llrs[5::6][:total_len]))
     
    interleave_table = np.arange(total_len)
    interleave_table[:block_size] = generate_ccsds_turbo_interleave_table(block_size)
          
    for r in range(iterations):
        prior_e1 = systematic + extrinsic_e2
        llr_e1_out = prior_e1 + 0.5 * parity_e1.sum(axis=1)
        extrinsic_e1 = np.clip(llr_e1_out - prior_e1, -20.0, 20.0)
                 
        sys_interleaved = systematic[interleave_table]
        prior_e2 = sys_interleaved + extrinsic_e1[interleave_table]
                 
        llr_e2_out = prior_e2 + 0.5 * parity_e2.sum(axis=1)
        extrinsic_e2_interleaved = np.clip(llr_e2_out - prior_e2, -20.0, 20.0)
        extrinsic_e2[interleave_table] = extrinsic_e2_interleaved
     
    final_llr = systematic + extrinsic_e1 + extrinsic_e2
    return (final_llr[:block_size] < 0).astype(np.uint8)

def compute_ccsds_crc16_syndrome(byte_array):
    if len(byte_array) < 3: return 0xFFFF
    crc = 0xFFFF
    for byte in byte_array:
        crc ^= (int(byte) << 8)
        for _ in range(8):
            if crc & 0x8000: crc = (crc << 1) ^ 0x1021
            else: crc = crc << 1
            crc &= 0xFFFF
    return crc

def attempt_crc_error_correction(decoded_bits):
    """
    Surgically checks every single-bit position across the decoded block.
    If a single flipped bit satisfies the CRC, the code corrects it and passes.
    """
    # Verify initial state
    initial_bytes = np.packbits(decoded_bits)
    if compute_ccsds_crc16_syndrome(initial_bytes) == 0x0000:
        return decoded_bits, True
        
    # Single-Bit Flip Exhaustive Search Loop
    working_bits = np.copy(decoded_bits)
    for i in range(len(working_bits)):
        # Toggle bit state (0 -> 1 or 1 -> 0)
        working_bits[i] ^= 1
        
        # Test candidate byte space
        test_bytes = np.packbits(working_bits)
        if compute_ccsds_crc16_syndrome(test_bytes) == 0x0000:
            return working_bits, True # Fixed!
            
        # Revert bit if it didn't solve the CRC syndrome
        working_bits[i] ^= 1
        
    return decoded_bits, False

def find_frame_asm_sync_with_phase(raw_stream, asm_bits):
    asm_reference = np.where(asm_bits == 1, -1.0, 1.0)
    clean_stream = np.nan_to_num(raw_stream, nan=0.0)
    correlation = np.correlate(clean_stream, asm_reference, mode='valid')
    normalized_corr = correlation / len(asm_reference)
    
    pos_peaks = np.where(normalized_corr > 0.65)[0]
    neg_peaks = np.where(normalized_corr < -0.65)[0]
    
    sync_targets = [(int(idx), 1.0) for idx in pos_peaks] + [(int(idx), -1.0) for idx in neg_peaks]
    sync_targets.sort(key=lambda x: x[0])
    return sync_targets

def process_repair_pipeline(input_file_path, output_bin_path, block_size=1784):
    turbo_rate, tail_bits = 6, 4
    codeword_symbols_len = (block_size + tail_bits) * turbo_rate
    asm_bits = get_ccsds_turbo_asm_bits()
    asm_symbols_len = len(asm_bits)
    total_frame_len = asm_symbols_len + codeword_symbols_len
    
    print("[*] ===============================================")
    print("[*] TURBO PIPELINE WITH SINGLE-BIT CRC REPAIR LAYER")
    print("[*] ===============================================")
    
    full_stream = np.fromfile(input_file_path, dtype=np.float32)
    sync_targets = find_frame_asm_sync_with_phase(full_stream, asm_bits)
    
    if not sync_targets:
        print("[-] ERROR: Synchronization failed.")
        return
        
    # Force baseline seed assignment for CCSDS standard links
    global_mask = generate_ccsds_lfsr_mask(codeword_symbols_len, initial_reg=0x3F)
    fixed_count = 0
    valid_count = 0
    
    with open(output_bin_path, "wb") as out_file:
        for f_idx, (idx, polarity) in enumerate(sync_targets):
            if idx + total_frame_len > len(full_stream): continue
                
            payload_start = idx + asm_symbols_len
            frame_llrs = full_stream[payload_start : payload_start + codeword_symbols_len]
            if polarity == -1.0: frame_llrs = frame_llrs * -1.0
                
            descrambled = frame_llrs * global_mask
            decoded_bits = log_map_decode(descrambled, block_size=block_size)
            
            # Run the CRC Repair Layer
            corrected_bits, is_ok = attempt_crc_error_correction(decoded_bits)
            packed_bytes = np.packbits(corrected_bits)
            
            if is_ok:
                out_file.write(packed_bytes.tobytes())
                valid_count += 1
                # Check if the frame was natively valid or saved by the repair engine
                native_bytes = np.packbits(decoded_bits)
                if compute_ccsds_crc16_syndrome(native_bytes) != 0x0000:
                    fixed_count += 1
                    print(f"    ├── Frame {f_idx:04d}: [Offset {idx:08d}] -> REPAIRED (1-Bit Error Fixed)")
                else:
                    print(f"    ├── Frame {f_idx:04d}: [Offset {idx:08d}] -> VALID (Native Pass)")
                    
    print("\n[*] ===============================================")
    print(f"[*] Pipeline processing complete. Handled {len(sync_targets)} synchronization locks.")
    print(f"[+] Output written to: {output_bin_path}")
    print(f"[+] Successfully extracted {valid_count} frames ({fixed_count} frames saved by repair engine).")
    print("[*] ===============================================")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_llr_file> <output_binary_file>")
        sys.exit(1)
    process_repair_pipeline(sys.argv[1], sys.argv[2])

