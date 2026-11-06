import sys
import struct
import re
def extract_ccsds_scid(first_two_bytes_hex):
    """
    Extracts the 10-bit SCID from the first 16 bits of a CCSDS Transfer Frame.
    Works for both Telemetry (TM) and Telecommand (TC) frame headers.
    """
    # 1. Convert the 4 hex characters into a 16-bit integer
    header_int = int(first_two_bytes_hex, 16)
    
    # 2. Shift right by 4 bits to discard the trailing VCID and status flags
    shifted = header_int >> 4
    
    # 3. Mask with 0x3FF (binary: 0011 1111 1111) to isolate only the 10 SCID bits
    scid = shifted & 0x3FF
    
    # 4. (Optional) Extract Virtual Channel ID (VCID) for telemetry frames (bits 12-14)
    vcid = (header_int >> 1) & 0x07
    
    return scid, vcid
def parse_telemetry_line(raw_hex_line):
    """
    Sanitizes the input string, extracts routing SCIDs from the header,
    decodes the 32-bit floating-point sensor data, and prints them side-by-side.
    """
    # 1. Strip out spaces or ASCII-translation noise characters
    clean_hex = re.sub(r'[^0-9a-fA-F]', '', raw_hex_line)
    # Ensure line has at least 8 characters (4 bytes) to parse out basic fields
    if len(clean_hex) < 8:
        return

    try:

        # 2. Extract and decode the 16-bit Master Routing Header (First 2 Bytes)
        header_bytes = clean_hex[0:22]
        scid2=extract_ccsds_scid(clean_hex[0:2])
        # Calculate SCID for AOS Protocol (8-bit width)
        apid_aos = int(header_bytes[0:4],16)
        sclk=int(header_bytes[12:20],16)
# Insert at the very top of your parsing function
        first_byte = int(header_bytes[:2], 16)
        version_bits = (first_byte >> 6) & 0x03
        aos_frame=False
        if version_bits == 1:
            # 🛰️ THIS IS AN AOS FRAME! Extract the 10-bit SCID instead of an APID
            aos_frame=True
            header_int = int(clean_hex[:4], 16)
     #       scid = (header_int >> 4) & 0x03FF
    
   #         if scid == 0x330 or scid == 816:
   #             spacecraft = "Mio (BepiColombo AOS Link Frame)"
   #             # Apply your live launch-based time calculation
   #             true_utc_date = MIO_LAUNCH + datetime.timedelta(seconds=time_tag_raw)

         # Calculate SCID for TM Protocol (7-bit width from standard APID partitioning)
      #  scid_tm = (header_int >> 4) & 0x7F
      #  scid_naif = scid_tm - 256
        full_binary_header = f"{int(clean_hex[:4], 16):016b}"
        
        # 3. Extract the 32-bit Floating-Point Sensor Data Field (First 4 Bytes)
        velocity_bytes = bytes.fromhex(clean_hex[0:8])
        velocity = struct.unpack('>f', velocity_bytes)[0]
        if (apid_aos > 2047):
            aos_ver=int(full_binary_header[0:2],2)
            scid2=(~(int(full_binary_header[2:12],2)))+1
            vcid=int(full_binary_header[10:14],2)
            print(f"{line[0:-1]}, TM-XFER, aos_ver = {aos_ver}, vcid = {vcid}, scid = {scid2}, SCLK = {sclk}")
        if (aos_frame == True):
            aos_ver=int(full_binary_header[0:2],2)
            scid2=(~(int(full_binary_header[2:12],2)))+1
            vcid=int(full_binary_header[10:14],2)
            print(f"{line[0:-1]}, AOS, scid = {scid2}, SCLK = {sclk}")
        else:
            # 4. Print the unified telemetry line
            aos_ver=int(full_binary_header[0:2],2)
            scid2=(~(int(full_binary_header[2:12],2)))+1
            vcid=int(full_binary_header[10:14],2)
            print(f"{line[0:-1]}, apid = {apid_aos}, apid_hex = 0x{apid_aos:03X}, scid = {scid2}, SCLK = {sclk}")
        
    except (ValueError, struct.error):
        # Safely bypass malformed data lines or text boilerplate lines
        pass

if __name__ == '__main__':
    # Stream line-by-line continuously from standard input (stdin)
    for line in sys.stdin:
        if line.strip():
            parse_telemetry_line(line.split(', ')[-1].split(' ')[-1])
