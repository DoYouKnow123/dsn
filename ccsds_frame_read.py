import pathlib
import sys
import re

def parse_xxd_to_bytes(stream):
    hex_buffer = bytearray()
    hex_regex = re.compile(r"[0-9A-Fa-f]{2}")
    for line in stream:
        if "|" in line:
            parts = line.split("|")
            text_to_parse = parts if len(parts) >= 2 else line
        else:
            text_to_parse = line
        for ht in hex_regex.findall(text_to_parse[0]):
            hex_buffer.append(int(ht, 16))
    return bytes(hex_buffer)

def process_frame_chunk(frame_bytes, frame_num, output_filename="iceeye_recovered.bin"):
    b0 = frame_bytes[0]
    b1 = frame_bytes[1]
    b2 = frame_bytes[2]
    b3 = frame_bytes[3]
    
    version = (b0 >> 6) & 0x03
    scid = ((b0 & 0x3F) << 4) | ((b1 >> 4) & 0x0F) if version == 0 else (((b0 & 0x3F) << 2) | ((b1 >> 6) & 0x03))
    vcid = (b1 >> 1) & 0x07 if version == 0 else (b1 & 0x3F)
    frame_counter = (b2 << 16) | (b3 << 8) | frame_bytes[4]

    # Filter out pure idle/null frames to keep the screen tidy
    if scid == 0 and vcid == 0 and frame_counter == 0:
        return

    scid_map = {
        27: "MetOp-SG A2 (EUMETSAT)",
        30: "MSTI-3 (US Department of Defense)",
        51: "SCD-1 (INPE Brazil)",
        54: "SCD-2 (INPE Brazil)",
        72: "CNES Network (France)",
        123: "KOMPSAT-3 (KARI South Korea)",
        725: "James Webb Space Telescope (NASA/ESA)",
        3151: "OneWeb Satellite Network",
        5583: "ICEYE Commercial SAR Constellation (Finland)"
    }
    spacecraft_name = scid_map.get(scid, f"Unmapped Platform (SCID {scid})")
    protocol = f"TM Protocol (V1)" if version == 0 else f"AOS Protocol (V2)"

    print(f"[FRAME ENTRY #{frame_num:04d}] Protocol: {protocol} | Platform: {spacecraft_name} | VCID: {vcid} | Counter: #{frame_counter}")

def main():
    raw_data_bytes = parse_xxd_to_bytes(sys.stdin)
    if not raw_data_bytes:
        return

    # Automatically append the entire raw batch to your binary ledger
    with open("iceeye_recovered.bin", "ab") as bin_file:
        bin_file.write(raw_data_bytes)
    print(f"--- Carved {len(raw_data_bytes)} total bytes to iceeye_recovered.bin ---")
    print("Parsing active telemetry frames in 128-byte increments:\\n")

    # Step through the 22KB buffer in clean 128-byte chunks
    frame_size = 128
    frame_num = 0
    for offset in range(0, len(raw_data_bytes) - (frame_size - 1), frame_size):
        frame_num += 1
        chunk = raw_data_bytes[offset:offset+frame_size]
        process_frame_chunk(chunk, frame_num)

if __name__ == "__main__":
    main()

