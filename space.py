import sys
import re
import argparse
import numpy as np

# =====================================================================
# CORE ALGORITHMIC ENGINES
# =====================================================================

def decode_viterbi_numpy(encoded_bits, k, rate, polynomials, inversion_mask):
    """Vectorized NumPy Viterbi Decoder for large constraint lengths (K > 8)."""
    num_states = 1 << (k - 1)
    states = np.arange(num_states, dtype=np.int32)
    
    # Precompute trellis: map next_state -> prev_states
    prev_state_0 = (states >> 1)
    prev_state_1 = (states >> 1) | (1 << (k - 2))
    
    # Precompute expected outputs
    expected_outputs = np.zeros((num_states, 2, rate), dtype=np.uint8)
    for bit in (0, 1):
        reg = (states << 1) | bit
        for i, poly in enumerate(polynomials):
            parity = np.zeros(num_states, dtype=np.uint8)
            temp_reg = reg & poly
            while np.any(temp_reg > 0):
                parity ^= (temp_reg & 1).astype(np.uint8)
                temp_reg >>= 1
            if inversion_mask[i]:
                parity ^= 1
            expected_outputs[:, bit, i] = parity

    path_metrics = np.full(num_states, 1000000, dtype=np.int32)
    path_metrics[0] = 0  # Start state is known 0
    
    num_steps = len(encoded_bits) // rate
    if num_steps == 0: return []
    
    decision_history = np.zeros((num_steps, num_states), dtype=np.uint8)
    received = np.array(encoded_bits[:num_steps * rate], dtype=np.uint8).reshape(-1, rate)
    
    for step in range(num_steps):
        rx_syms = received[step]
        bm_0 = np.sum(expected_outputs[:, 0, :] != rx_syms, axis=1)
        bm_1 = np.sum(expected_outputs[:, 1, :] != rx_syms, axis=1)
        
        metric_cand_0 = path_metrics[prev_state_0] + bm_0[prev_state_0]
        metric_cand_1 = path_metrics[prev_state_1] + bm_1[prev_state_1]
        
        decision = metric_cand_1 < metric_cand_0
        path_metrics = np.where(decision, metric_cand_1, metric_cand_0)
        decision_history[step] = decision.astype(np.uint8)
        
    # Traceback
    decoded_bits = []
    curr_state = np.argmin(path_metrics)
    for step in reversed(range(num_steps)):
        decision = decision_history[step, curr_state]
        decoded_bits.append(curr_state & 1)
        curr_state = prev_state_1[curr_state] if decision else prev_state_0[curr_state]
        
    decoded_bits.reverse()
    return decoded_bits


def decode_viterbi_standard(encoded_bits, k, rate, polynomials, inversion_mask):
    """Fast lookup dictionary Viterbi Decoder for small constraint lengths (K <= 8)."""
    num_states = 1 << (k - 1)
    next_states = {s: {} for s in range(num_states)}
    outputs = {s: {} for s in range(num_states)}
    
    for s in range(num_states):
        for b in (0, 1):
            next_states[s][b] = ((s << 1) | b) & (num_states - 1)
            reg = (s | (b << (k - 1)))
            out_bits = []
            for i, poly in enumerate(polynomials):
                parity = bin(reg & poly).count('1') % 2
                if inversion_mask[i]:
                    parity ^= 1
                out_bits.append(parity)
            outputs[s][b] = out_bits

    path_metrics = {s: float('inf') for s in range(num_states)}
    path_metrics[0] = 0
    history = []
    
    for i in range(0, len(encoded_bits) - rate + 1, rate):
        rx = encoded_bits[i:i+rate]
        new_metrics = {s: float('inf') for s in range(num_states)}
        new_hist = {}
        for s, metric in path_metrics.items():
            if metric == float('inf'): continue
            for b in (0, 1):
                nxt = next_states[s][b]
                bm = sum(r ^ e for r, e in zip(rx, outputs[s][b]))
                if metric + bm < new_metrics[nxt]:
                    new_metrics[nxt] = metric + bm
                    new_hist[nxt] = (s, b)
        if not new_hist: break
        path_metrics, history = new_metrics, history + [new_hist]
        
    decoded_bits = []
    best_state = min(path_metrics, key=path_metrics.get)
    for step in reversed(history):
        prev_state, bit = step[best_state]
        decoded_bits.append(bit)
        best_state = prev_state
    return list(reversed(decoded_bits))

# =====================================================================
# CCSDS SPACE LOG FRAME PARSER
# =====================================================================
def parse_ccsds_frames(data_bytes):
    """Scans raw bytes for standard CCSDS Attached Sync Markers (1A CF FC 1D)."""
    asm = b'\x1A\xCF\xFC\x1D'
    indices = [m.start() for m in re.finditer(re.escape(asm), data_bytes)]
    if not indices:
        print("[-] Verification: No CCSDS frames found with standard ASM.", file=sys.stderr)
        return False

    print("\n" + "="*60, file=sys.stderr)
    print("                PARSED CCSDS TELEMETRY FRAMES             ", file=sys.stderr)
    print("="*60, file=sys.stderr)

    for idx in indices:
        header_start = idx + len(asm)
        if len(data_bytes) < header_start + 6: continue
            
        header_bytes = data_bytes[header_start:header_start+6]
        version = (header_bytes[0] >> 6) & 0x03
        
        if version == 0:    # TM Primary Channel
            scid = ((header_bytes[0] & 0x3F) << 4) | ((header_bytes[1] >> 4) & 0x0F)
            vcid = (header_bytes[1] & 0x0E) >> 1
            frame_type = "TM (Version 1)"
        elif version == 1:  # AOS Channel
            scid = ((header_bytes[0] & 0x3F) << 2) | ((header_bytes[1] >> 6) & 0x03)
            vcid = header_bytes[1] & 0x3F
            frame_type = "AOS (Version 2)"
        else:
            scid, vcid, frame_type = "Unknown", "Unknown", f"Unknown (V{version})"

        apid_str = "N/A"
        if len(data_bytes) >= header_start + 12:
            pkt_hdr = data_bytes[header_start+6:header_start+8]
            apid = ((pkt_hdr[0] & 0x07) << 8) | pkt_hdr[1]
            apid_str = f"{apid} (0x{apid:03X})"

        print(f"[+] Sync Marker Frame at Byte Offset: 0x{idx:04X}")
        print(f"    |-- Protocol Standard : {frame_type}")
        print(f"    |-- Spacecraft ID     : {scid}")
        print(f"    |-- Virtual Channel   : {vcid}")
        print(f"    |-- App Process ID    : {apid_str}")
        print("-" * 60)
    return True

# =====================================================================
# ENTRYPOINT PIPELINE
# =====================================================================
def main():
    parser = argparse.ArgumentParser(description="Generic Satellite Viterbi Decoder & CCSDS Parser")
    parser.add_argument("-k", type=int, default=15, help="Constraint Length (e.g. 7 or 15)")
    parser.add_argument("-r", "--rate", type=int, default=4, help="Code Rate denominator (e.g. 2 or 4)")
    parser.add_argument("-p", "--polys", type=str, default="4CE9,52B9,64ED,72CF", 
                        help="Comma-separated hex polynomials (e.g. '4F,6D' or '4CE9,52B9,64ED,72CF')")
    parser.add_argument("-i", "--inv", type=str, default="1,0,0,1", 
                        help="Comma-separated channel binary inversion mask flags (e.g. '0,0' or '1,0,0,1')")
    args = parser.parse_args()

    # Parse parameters cleanly
    polynomials = [int(p.strip(), 16) for p in args.polys.split(",")]
    inversion_mask = [bool(int(i.strip())) for i in args.inv.split(",")]
    
    if len(polynomials) != args.rate or len(inversion_mask) != args.rate:
        print("Error: The count of polynomials and inversion flags must match the code rate.", file=sys.stderr)
        return

    print(f"[*] Configuration Loaded: K={args.k}, Rate=1/{args.rate}", file=sys.stderr)
    print(f"[*] Polynomial Masks    : {[hex(p) for p in polynomials]}", file=sys.stderr)
    print(f"[*] Over-The-Air Invert : {inversion_mask}", file=sys.stderr)

    # Ingest text log from standard input
    bit_stream = []
    hex_to_bits = {f'{i:01x}': [(i>>j)&1 for j in range(3,-1,-1)] for i in range(16)}
    
    for line in sys.stdin:
        clean_line = line.strip().lower()
        if not clean_line: continue
        parts = re.split(r'\|', clean_line)
        tokens = re.split(r'\s+|\:', parts[0].strip())
        for token in tokens:
            if len(token) > 8 or (len(token) == 4 and token.endswith('0')): continue
            if re.match(r'^[0-9a-f]{2}$', token):
                for char in token:
                    bit_stream.extend(hex_to_bits[char])

    if not bit_stream:
        print("Error: No valid data targets processed from standard input.", file=sys.stderr)
        return

    print(f"[*] Extracted {len(bit_stream)} tracking bits. Running decoder matrix...", file=sys.stderr)

    # Automatically swap engines depending on code size
    if args.k > 8:
        decoded_bits = decode_viterbi_numpy(bit_stream, args.k, args.rate, polynomials, inversion_mask)
    else:
        decoded_bits = decode_viterbi_standard(bit_stream, args.k, args.rate, polynomials, inversion_mask)

    # Reassemble bytes
    decoded_bytes = bytearray()
    for i in range(0, len(decoded_bits), 8):
        chunk = decoded_bits[i:i+8]
        if len(chunk) < 8: break
        val = 0
        for b in chunk: val = (val << 1) | b
        decoded_bytes.append(val)

    # Run CCSDS Aligner
    parse_ccsds_frames(bytes(decoded_bytes))
    
    # Pipe raw binary directly to file stdout redirection
    sys.stdout.buffer.write(decoded_bytes)

if __name__ == '__main__':
    main()

