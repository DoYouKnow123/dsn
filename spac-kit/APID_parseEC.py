import struct
import numpy as np

def descramble_block_payload(payload_bytes):
    """Applies standard CCSDS 15-stage additive descrambler to a block payload."""
    out = np.copy(payload_bytes)
    lfsr = 0x7FFF
    for i in range(len(out)):
        b_out = 0
        for bit in range(8):
            lfsr_bit = lfsr & 1
            feedback = (lfsr ^ (lfsr >> 1)) & 1
            lfsr = (lfsr >> 1) | (feedback << 14)
            
            data_bit = (out[i] >> (7 - bit)) & 1
            b_out |= ((data_bit ^ lfsr_bit) << (7 - bit))
        out[i] = b_out
    return out

def extract_clean_telemetry(filename, target_apids=[1144, 1145], block_size=1115):
    print("--- Executing Final Telemetry Offset Pass ---")
    
    with open(filename, 'rb') as f:
        raw_data = np.frombuffer(f.read(), dtype=np.uint8)
        
    usable_bytes = (len(raw_data) // block_size) * block_size
    matrix = raw_data[:usable_bytes].reshape(-1, block_size)
    
    # Test typical AOS trailer/header slice boundaries
    # Standard engineering header is 6 bytes. 
    # If trailing Reed-Solomon parity bytes (160 bytes) are appended, we slice accordingly.
    for header_offset in [6, 8, 12, 14]:
        apid_map = {}
        extracted_data = {apid: [] for apid in target_apids}
        
        for block in matrix:
            # Descramble starting cleanly at the payload boundary
            descrambled_payload = descramble_block_payload(block[header_offset:])
            
            ptr = 0
            payload_len = len(descrambled_payload)
            
            while ptr < payload_len - 6:
                pid, seq, pkt_len = struct.unpack('>HHH', descrambled_payload[ptr:ptr+6])
                version = (pid >> 13) & 0x07
                apid = pid & 0x07FF
                actual_pkt_len = pkt_len + 7
                
                if version == 0 and 0 < actual_pkt_len <= (payload_len - ptr):
                    apid_map[apid] = apid_map.get(apid, 0) + 1
                    if apid in target_apids:
                        extracted_data[apid].append(descrambled_payload[ptr : ptr + actual_pkt_len].tobytes())
                    ptr += actual_pkt_len
                else:
                    ptr += 1
                    
        # Check if the active science/engineering range is unlocked
        active_channels = [a for a in apid_map.keys() if 1000 <= a <= 1200]
        if active_channels or 2047 in apid_map:
            print(f"\n[+] Applied Header Offset: {header_offset} bytes")
            print("--- Top 5 Active Target APIDs Found ---")
            for a_id, count in sorted(apid_map.items(), key=lambda x: x[1], reverse=True)[:]:
                print(f"    APID {a_id:4d} (0x{a_id:03X}) : {count} packets")
                
            for apid in target_apids:
                if extracted_data[apid]:
                    out_name = f"apid_{apid}_final.bin"
                    with open(out_name, 'wb') as out_f:
                        for pkt in extracted_data[apid]:
                            out_f.write(pkt)
                    print(f"    ==> Saved active stream data to {out_name}")
            if active_channels:
                return

if __name__ == "__main__":
    extract_clean_telemetry("telemetry_output.bin", target_apids=[1025, 1089, 1153, 1216, 1217, 1218, 1219, 1222, 1223, 1226, 1227, 1232, 1281, 1345, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1409, 1419, 1424, 1426, 1473, 1474, 1537, 1601, 1665, 1729])
