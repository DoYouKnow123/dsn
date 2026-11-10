import shutil
import struct
import subprocess
from collections import deque
from pathlib import Path
import numpy as np

# =====================================================================
# PIPELINE CONFIGURATION
# =====================================================================
TELEMETRY_BIN = Path("telemetry_output.bin")
APID_BIN_DIR = Path("./extracted_apids")
WAVELET_JPG_DIR = Path("./wavelet_jpgs")      # Optional folder for pre-existing wavelet JPGs
OUTPUT_JPG_DIR = Path("./reconstructed_jpgs")

TARGET_APIDS = [i for i in range(1, 6000)]
BLOCK_SIZE = 1115

# Frame Dimensions for Raw APID Payloads
# Set IMAGE_WIDTH = None to auto-detect row stride via autocorrelation
IMAGE_WIDTH = None

# Color ICER Mode:
# "auto"         -> Auto-detects 3-APID triplets, 3 sequential planes, or Bayer quad_lattice
# "planar_3ch"   -> Single APID payload holds 3 stacked planes (Plane 0, Plane 1, Plane 2)
# "apid_triplets"-> Groups matching consecutive APIDs (N, N+1, N+2) as R/G/B or Y/Cb/Cr
# "bayer_rggb"   -> Demosaics 2x2 quad_lattice as R, G1, G2, B after IDWT
# "bayer_bggr"   -> Demosaics 2x2 quad_lattice as B, G1, G2, R after IDWT
# "grayscale"    -> Legacy single-channel mode
COLOR_MODE = "auto"

# Color Space of the 3 ICER Planes:
# "YCbCr" -> Standard NASA ICER color space (Luminance + 2 Chrominance bands)
# "RGB"   -> Direct Red, Green, Blue wavelet planes
COLOR_SPACE = "YCbCr"

# Lattice / Telemetry Interleaving Mode:
# "checkerboard" -> 2D lattice ((row + col) % 2) -> outputs _1, _2
# "quad_lattice" -> 2x2 lattice ((row % 2, col % 2)) -> outputs _1, _2, _3, _4
# "rows"         -> Alternating scanlines -> outputs _1, _2
# "columns"      -> Alternating columns -> outputs _1, _2
# "none"         -> No sub-lattice splitting
LATTICE_MODE = "quad_lattice"
DEINTERLEAVE_BEFORE_IDWT = True

# Sensor Banding Removal Parameters
DEBAND_DIRECTION = "both"        # "horizontal", "vertical", "both", or "none"
WAVELET_DENOISE_THRESH = 6.0     # Soft-thresholding for sensor noise in detail subbands (0 = off)
SPATIAL_DEBAND_STRENGTH = 0.85   # 0.0 to 1.0 (1.0 = full row/column median bias removal)

# Dark Cloudy Patch Removal Parameters
ENABLE_DARK_PATCH_REMOVAL = False
DARK_PATCH_KERNEL = 65           # Must be larger than widest crater (e.g., 45 to 121 px)
DARK_PATCH_STRENGTH = 0.85       # 0.0 to 1.0
DARK_PATCH_MODE = "divide"       # "divide" (flat-field gain) or "subtract" (additive offset)

# Crater Lighting & Histogram Balance Parameters
ENABLE_LIGHT_BALANCE = False
AUTO_BIMODAL_STD_THRESH = 55.0   # Only stretch frames with high contrast std-dev (0.0 = always stretch)
LOW_PERCENTILE = 0.5
HIGH_PERCENTILE = 99.5
ASINH_SOFTNESS = 3.0             # Lifts dark crater floors while compressing bright rims
GAMMA_VALUE = 1.05

# ICER Wavelet Parameters
STAGES = 5            # Number of decomposition stages per separated image
SIGNED_OFFSET = 128   # Set to 0 if detail subbands (HL, LH, HH) are not midpoint-shifted by 128
JPEG_QUALITY = 95     # Output JPEG quality (1-100)


# =====================================================================
# IMAGE CLASSIFICATION (STARFIELD VS. PLANETARY)
# =====================================================================
def classify_space_image(
    matrices: list,
    star_sigma: float = 20,
    max_star_area_ratio: float = 0.00035,
    max_single_object_ratio: float = 0.00015
) -> str:
    """
    Classifies a reconstructed image as 'starfield' or 'planetary' using
    noise-floor thresholding and connected-component blob analysis.
    """
    if len(matrices) == 1:
        gray = np.array(matrices[0], dtype=np.float64)
    else:
        # Use Rec.601 luminance weights for multi-channel color images
        r = np.array(matrices[0], dtype=np.float64)
        g = np.array(matrices[1], dtype=np.float64)
        b = np.array(matrices[2], dtype=np.float64)
        gray = 0.299 * r + 0.587 * g + 0.114 * b

    h, w = gray.shape
    total_pixels = float(h * w)
    if total_pixels == 0:
        return "starfield"

    bg_median = np.median(gray)
    mad = np.median(np.abs(gray - bg_median))
    robust_std = max(1.4826 * mad, 2.0)

    bright_mask = gray > (bg_median + star_sigma * robust_std)
    bright_count = int(np.sum(bright_mask))
    bright_ratio = bright_count / total_pixels

    if bright_ratio > max_star_area_ratio:
        return "planetary"
    if bright_count == 0:
        return "starfield"

    visited = np.zeros((h, w), dtype=bool)
    max_blob_size = 0
    ys, xs = np.where(bright_mask)

    for start_y, start_x in zip(ys, xs):
        if visited[start_y, start_x]:
            continue

        blob_size = 0
        queue = deque([(start_y, start_x)])
        visited[start_y, start_x] = True

        while queue:
            cy, cx = queue.popleft()
            blob_size += 1

            if (blob_size / total_pixels) > max_single_object_ratio:
                return "planetary"

            for ny in range(max(0, cy - 1), min(h, cy + 2)):
                for nx in range(max(0, cx - 1), min(w, cx + 2)):
                    if not visited[ny, nx] and bright_mask[ny, nx]:
                        visited[ny, nx] = True
                        queue.append((ny, nx))

        if blob_size > max_blob_size:
            max_blob_size = blob_size

    if (max_blob_size / total_pixels) > max_single_object_ratio:
        return "planetary"

    return "starfield"


# =====================================================================
# STAGE 1: CCSDS DESCRAMBLING & APID EXTRACTION
# =====================================================================
def descramble_block_payload(payload_bytes: np.ndarray) -> np.ndarray:
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


def extract_clean_telemetry(filename: Path, target_apids: list, block_size: int = 1115) -> dict:
    """
    Descrambles AOS blocks, extracts CCSDS packets per target APID, saves .bin files,
    and returns a dict mapping {apid: concatenated_payload_bytes_without_ccsds_headers}.
    """
    print("--- Stage 1: Executing CCSDS Telemetry Offset Pass ---")
    if not filename.exists():
        print(f"[!] Telemetry file '{filename}' not found. Skipping binary extraction.")
        return {}

    APID_BIN_DIR.mkdir(parents=True, exist_ok=True)
    raw_data = np.frombuffer(filename.read_bytes(), dtype=np.uint8)

    usable_bytes = (len(raw_data) // block_size) * block_size
    matrix = raw_data[:usable_bytes].reshape(-1, block_size)

    for header_offset in [6, 8, 12, 14]:
        apid_map = {}
        extracted_packets = {apid: [] for apid in target_apids}
        extracted_payloads = {apid: bytearray() for apid in target_apids}

        for block in matrix:
            descrambled_payload = descramble_block_payload(block[header_offset:])
            ptr = 0
            payload_len = len(descrambled_payload)

            while ptr < payload_len - 6:
                pid, seq, pkt_len = struct.unpack('>HHH', descrambled_payload[ptr:ptr + 6])
                version = (pid >> 13) & 0x07
                apid = pid & 0x07FF
                actual_pkt_len = pkt_len + 7

                if version == 0 and 0 < actual_pkt_len <= (payload_len - ptr):
                    apid_map[apid] = apid_map.get(apid, 0) + 1
                    if apid in target_apids:
                        pkt_bytes = descrambled_payload[ptr:ptr + actual_pkt_len].tobytes()
                        extracted_packets[apid].append(pkt_bytes)
                        extracted_payloads[apid].extend(pkt_bytes[6:])
                    ptr += actual_pkt_len
                else:
                    ptr += 1

        active_channels = [a for a in apid_map.keys() if 1000 <= a <= 1200]
        if active_channels or 2047 in apid_map:
            print(f"\n[+] Applied Header Offset: {header_offset} bytes")
            print("--- Top 5 Active Target APIDs Found ---")
            for a_id, count in sorted(apid_map.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"    APID {a_id:4d} (0x{a_id:03X}) : {count} packets")

            active_streams = {}
            for apid in target_apids:
                if extracted_packets[apid]:
                    out_name = APID_BIN_DIR / f"apid_{apid}_final.bin"
                    with open(out_name, 'wb') as out_f:
                        for pkt in extracted_packets[apid]:
                            out_f.write(pkt)
                    print(f"    ==> Saved active stream data to {out_name}")
                    active_streams[apid] = bytes(extracted_payloads[apid])

            if active_channels:
                return active_streams

    return {}


# =====================================================================
# STAGE 2: UBUNTU JPEG I/O & STRIDE DETECTION
# =====================================================================
def check_ubuntu_jpeg_tools():
    if not shutil.which("djpeg") or not shutil.which("cjpeg"):
        raise RuntimeError(
            "Ubuntu's native 'djpeg'/'cjpeg' tools were not found. "
            "Install them via apt: sudo apt update && sudo apt install -y libjpeg-turbo-progs"
        )


def read_jpg(filepath: Path):
    proc = subprocess.run(["djpeg", "-pnm", str(filepath)], capture_output=True, check=True)
    data = proc.stdout

    idx = 0
    tokens = []
    while len(tokens) < 4:
        while idx < len(data) and data[idx:idx + 1].isspace():
            idx += 1
        if data[idx:idx + 1] == b"#":
            while idx < len(data) and data[idx:idx + 1] != b"\n":
                idx += 1
            continue
        start = idx
        while idx < len(data) and not data[idx:idx + 1].isspace():
            idx += 1
        tokens.append(data[start:idx])

    magic = tokens[0]
    width = int(tokens[1])
    height = int(tokens[2])
    maxval = int(tokens[3])

    if magic not in (b"P5", b"P6") or maxval != 255:
        raise ValueError(f"Unsupported PNM format: {magic}, maxval={maxval}")

    raw_pixels = data[idx + 1:]
    channels = 1 if magic == b"P5" else 3
    stride = width * channels

    matrices = []
    for ch in range(channels):
        mat = []
        for y in range(height):
            row = [float(raw_pixels[y * stride + x * channels + ch]) for x in range(width)]
            mat.append(row)
        matrices.append(mat)

    return matrices, width, height


def write_jpg(filepath: Path, matrices: list, width: int, height: int, quality: int = 95):
    channels = len(matrices)
    magic = b"P5\n" if channels == 1 else b"P6\n"
    header = magic + f"{width} {height}\n255\n".encode("ascii")

    # Fast vectorized packing for P5/P6 output
    stacked = np.stack([np.asarray(m, dtype=np.float64) for m in matrices], axis=-1)
    clipped = np.clip(np.rint(stacked), 0, 255).astype(np.uint8)
    raw_bytes = clipped.tobytes()

    subprocess.run(
        ["cjpeg", "-quality", str(quality), "-outfile", str(filepath)],
        input=header + raw_bytes,
        check=True
    )


def detect_row_width(byte_stream: bytes, min_w: int = 64, max_w: int = 2048) -> int:
    """Uses normalized autocorrelation to estimate the row stride of a raw telemetry stream."""
    arr = np.frombuffer(byte_stream, dtype=np.uint8).astype(np.float64)
    if len(arr) < min_w * 4:
        return 0
    arr -= np.mean(arr)
    norm = np.dot(arr, arr)
    if norm == 0:
        return 0

    best_w = 256
    best_corr = -1.0
    limit = min(max_w, len(arr) // 3)

    candidates = sorted(set([2**p for p in range(6, 12)] + list(range(min_w, limit, 16))))
    for w in candidates:
        if w >= limit:
            continue
        corr = np.dot(arr[:-w], arr[w:]) / norm
        if corr > best_corr:
            best_corr = corr
            best_w = w
    return best_w


# =====================================================================
# STAGE 3: DE-INTERLEAVING, ICER IDWT, COLOR CONVERSION & DEBANDING
# =====================================================================
def soft_threshold(val: float, thresh: float) -> float:
    if thresh <= 0.0:
        return val
    if val > thresh:
        return val - thresh
    elif val < -thresh:
        return val + thresh
    return 0.0


def inv_lifting_1d(low: list, high: list) -> list:
    n_low = len(low)
    n_high = len(high)
    total = n_low + n_high
    out = [0.0] * total

    even = [0.0] * n_low
    for i in range(n_low):
        h_left = high[i - 1] if i > 0 else (high[0] if n_high > 0 else 0.0)
        h_right = high[i] if i < n_high else (high[-1] if n_high > 0 else 0.0)
        even[i] = low[i] - ((h_left + h_right + 2.0) / 4.0)

    odd = [0.0] * n_high
    for i in range(n_high):
        e_left = even[i]
        e_right = even[i + 1] if (i + 1) < n_low else even[-1]
        odd[i] = high[i] + ((e_left + e_right) / 2.0)

    for i in range(n_low):
        out[2 * i] = even[i]
    for i in range(n_high):
        out[2 * i + 1] = odd[i]

    return out


def inv_dwt_2d(matrix: list, stages: int) -> list:
    height = len(matrix)
    width = len(matrix[0])

    dims = []
    h, w = height, width
    for _ in range(stages):
        dims.append((h, w))
        h = (h + 1) // 2
        w = (w + 1) // 2

    for stage_idx in reversed(range(stages)):
        cur_h, cur_w = dims[stage_idx]
        half_h = (cur_h + 1) // 2
        half_w = (cur_w + 1) // 2

        for r in range(cur_h):
            for c in range(cur_w):
                is_hl = (r < half_h and c >= half_w)
                is_lh = (r >= half_h and c < half_w)
                is_hh = (r >= half_h and c >= half_w)

                if is_hl or is_lh or is_hh:
                    val = matrix[r][c] - SIGNED_OFFSET
                    thresh = WAVELET_DENOISE_THRESH
                    if is_lh and DEBAND_DIRECTION in ("horizontal", "both"):
                        thresh *= 1.5
                    elif is_hl and DEBAND_DIRECTION in ("vertical", "both"):
                        thresh *= 1.5
                    matrix[r][c] = soft_threshold(val, thresh)

        for c in range(cur_w):
            low_col = [matrix[r][c] for r in range(half_h)]
            high_col = [matrix[r][c] for r in range(half_h, cur_h)]
            recon_col = inv_lifting_1d(low_col, high_col)
            for r in range(cur_h):
                matrix[r][c] = recon_col[r]

        for r in range(cur_h):
            low_row = matrix[r][:half_w]
            high_row = matrix[r][half_w:cur_w]
            recon_row = inv_lifting_1d(low_row, high_row)
            matrix[r][:cur_w] = recon_row

    return matrix


def median(values: list) -> float:
    s = sorted(values)
    n = len(s)
    if n == 0:
        return 0.0
    mid = n // 2
    return s[mid] if n % 2 == 1 else (s[mid - 1] + s[mid]) / 2.0


def remove_spatial_banding(matrix: list, direction: str, strength: float) -> list:
    if direction == "none" or strength <= 0.0:
        return matrix

    height = len(matrix)
    width = len(matrix[0])
    window = 5

    if direction in ("horizontal", "both"):
        row_medians = [median(matrix[r]) for r in range(height)]
        for r in range(height):
            r_min = max(0, r - window)
            r_max = min(height, r + window + 1)
            local_baseline = median(row_medians[r_min:r_max])
            bias = (row_medians[r] - local_baseline) * strength
            for c in range(width):
                matrix[r][c] -= bias

    if direction in ("vertical", "both"):
        col_medians = [median([matrix[r][c] for r in range(height)]) for c in range(width)]
        for c in range(width):
            c_min = max(0, c - window)
            c_max = min(width, c + window + 1)
            local_baseline = median(col_medians[c_min:c_max])
            bias = (col_medians[c] - local_baseline) * strength
            for r in range(height):
                matrix[r][c] -= bias

    return matrix


def deinterleave_matrix(matrix: list, mode: str) -> list:
    height = len(matrix)
    width = len(matrix[0])

    if mode == "rows":
        return [
            [matrix[r][:] for r in range(0, height, 2)],
            [matrix[r][:] for r in range(1, height, 2)]
        ]
    elif mode == "columns":
        return [
            [[matrix[r][c] for c in range(0, width, 2)] for r in range(height)],
            [[matrix[r][c] for c in range(1, width, 2)] for r in range(height)]
        ]
    elif mode == "checkerboard":
        sub_w = width // 2
        img1, img2 = [], []
        for r in range(height):
            row1, row2 = [], []
            for c_pair in range(sub_w):
                c0, c1 = 2 * c_pair, 2 * c_pair + 1
                if r % 2 == 0:
                    row1.append(matrix[r][c0])
                    row2.append(matrix[r][c1])
                else:
                    row1.append(matrix[r][c1])
                    row2.append(matrix[r][c0])
            img1.append(row1)
            img2.append(row2)
        return [img1, img2]
    elif mode == "quad_lattice":
        return [
            [[matrix[r][c] for c in range(0, width, 2)] for r in range(0, height, 2)],
            [[matrix[r][c] for c in range(1, width, 2)] for r in range(0, height, 2)],
            [[matrix[r][c] for c in range(0, width, 2)] for r in range(1, height, 2)],
            [[matrix[r][c] for c in range(1, width, 2)] for r in range(1, height, 2)]
        ]
    elif mode == "none":
        return [matrix]
    else:
        raise ValueError(f"Unknown LATTICE_MODE: {mode}")


def ycbcr_to_rgb_matrices(planes: list) -> list:
    """
    Converts 3-plane YCbCr (with midpoint-shifted 128 chrominance) to RGB matrices.
    Standard inverse transform used in NASA ICER color decompression.
    """
    if len(planes) != 3:
        return planes

    Y = np.asarray(planes[0], dtype=np.float64)
    Cb = np.asarray(planes[1], dtype=np.float64) - 128.0
    Cr = np.asarray(planes[2], dtype=np.float64) - 128.0

    R = Y + 1.402 * Cr
    G = Y - 0.344136 * Cb - 0.714136 * Cr
    B = Y + 1.772 * Cb

    return [
        np.clip(R, 0.0, 255.0).tolist(),
        np.clip(G, 0.0, 255.0).tolist(),
        np.clip(B, 0.0, 255.0).tolist()
    ]


def demosaic_bayer_quad(quad_planes: list, pattern: str = "RGGB") -> list:
    """
    Reconstructs a full-resolution 3-channel [R, G, B] image from 4 decompressed
    2x2 sub-lattice planes ([0,0], [0,1], [1,0], [1,1]) using bilinear interpolation.
    """
    if len(quad_planes) != 4:
        return quad_planes

    p00 = np.asarray(quad_planes[0], dtype=np.float64)
    p01 = np.asarray(quad_planes[1], dtype=np.float64)
    p10 = np.asarray(quad_planes[2], dtype=np.float64)
    p11 = np.asarray(quad_planes[3], dtype=np.float64)

    sub_h, sub_w = p00.shape
    h, w = sub_h * 2, sub_w * 2

    if pattern.upper() == "BGGR":
        B_sub, G1_sub, G2_sub, R_sub = p00, p01, p10, p11
    else:  # Default RGGB
        R_sub, G1_sub, G2_sub, B_sub = p00, p01, p10, p11

    R = np.zeros((h, w), dtype=np.float64)
    G = np.zeros((h, w), dtype=np.float64)
    B = np.zeros((h, w), dtype=np.float64)

    R[0::2, 0::2] = R_sub
    G[0::2, 1::2] = G1_sub
    G[1::2, 0::2] = G2_sub
    B[1::2, 1::2] = B_sub

    # Interpolate Green at Red and Blue locations (average of 4 cardinal neighbors)
    G_pad = np.pad(G, 1, mode="reflect")
    G_interp = 0.25 * (G_pad[:-2, 1:-1] + G_pad[2:, 1:-1] + G_pad[1:-1, :-2] + G_pad[1:-1, 2:])
    G[0::2, 0::2] = G_interp[0::2, 0::2]
    G[1::2, 1::2] = G_interp[1::2, 1::2]

    def interp_rb(channel, r_off, c_off):
        pad = np.pad(channel, 1, mode="reflect")
        # Horizontal neighbors
        channel[r_off::2, (1 - c_off)::2] = 0.5 * (
            pad[1 + r_off:-1:2, 1 + (1 - c_off) - 1:-1:2] +
            pad[1 + r_off:-1:2, 1 + (1 - c_off) + 1::2]
        )
        # Vertical neighbors
        channel[(1 - r_off)::2, c_off::2] = 0.5 * (
            pad[1 + (1 - r_off) - 1:-1:2, 1 + c_off:-1:2] +
            pad[1 + (1 - r_off) + 1::2, 1 + c_off:-1:2]
        )
        # Diagonal neighbors
        channel[(1 - r_off)::2, (1 - c_off)::2] = 0.25 * (
            pad[1 + (1 - r_off) - 1:-1:2, 1 + (1 - c_off) - 1:-1:2] +
            pad[1 + (1 - r_off) - 1:-1:2, 1 + (1 - c_off) + 1::2] +
            pad[1 + (1 - r_off) + 1::2, 1 + (1 - c_off) - 1:-1:2] +
            pad[1 + (1 - r_off) + 1::2, 1 + (1 - c_off) + 1::2]
        )
        return channel

    R = interp_rb(R, 0, 0)
    B = interp_rb(B, 1, 1)

    return [
        np.clip(R, 0.0, 255.0).tolist(),
        np.clip(G, 0.0, 255.0).tolist(),
        np.clip(B, 0.0, 255.0).tolist()
    ]


def check_planar_color_correlation(arr_2d: np.ndarray) -> bool:
    """
    Checks if a 2D payload whose height is divisible by 3 consists of 3 correlated
    spatial color planes (e.g., R/G/B or Y/Cb/Cr) rather than a single tall frame.
    """
    h, w = arr_2d.shape
    if h % 3 != 0 or (h // 3) < (2 ** STAGES):
        return False

    plane_h = h // 3
    p0 = arr_2d[0:plane_h, :].ravel()
    p1 = arr_2d[plane_h:2 * plane_h, :].ravel()
    p2 = arr_2d[2 * plane_h:3 * plane_h, :].ravel()

    if np.std(p0) < 1e-3 or np.std(p1) < 1e-3 or np.std(p2) < 1e-3:
        return False

    corr_01 = np.corrcoef(p0, p1)[0, 1]
    corr_02 = np.corrcoef(p0, p2)[0, 1]
    return bool(corr_01 > 0.35 or corr_02 > 0.35)


# =====================================================================
# STAGE 4: DARK PATCH REMOVAL & CRATER LIGHTING EQUALIZATION
# =====================================================================
def remove_dark_patches(
    matrices: list,
    kernel_size: int = 65,
    strength: float = 0.85,
    mode: str = "divide"
) -> list:
    """
    Removes large-scale dark cloudy patches and uneven background shading
    while preserving crisp crater rims and surface detail.
    """
    cleaned = []
    half_k = kernel_size // 2

    for ch_mat in matrices:
        arr = np.array(ch_mat, dtype=np.float64)
        h, w = arr.shape

        if h < kernel_size or w < kernel_size:
            cleaned.append(ch_mat)
            continue

        padded = np.pad(arr, half_k, mode="reflect")
        integral = np.cumsum(np.cumsum(padded, axis=0), axis=1)
        integral = np.pad(integral, ((1, 0), (1, 0)), mode="constant", constant_values=0)

        bg = (
            integral[kernel_size:, kernel_size:]
            - integral[:-kernel_size, kernel_size:]
            - integral[kernel_size:, :-kernel_size]
            + integral[:-kernel_size, :-kernel_size]
        ) / float(kernel_size * kernel_size)

        target_level = np.percentile(bg, 75.0)

        if mode == "divide":
            safe_bg = np.maximum(bg, 15.0)
            gain = target_level / safe_bg
            effective_gain = 1.0 + strength * (gain - 1.0)
            corrected = arr * effective_gain
        else:
            delta = (target_level - bg) * strength
            corrected = arr + delta

        cleaned.append(np.clip(corrected, 0.0, 255.0).tolist())

    return cleaned


def balance_crater_lighting(
    matrices: list,
    low_pct: float = 0.5,
    high_pct: float = 99.5,
    asinh_softness: float = 3.0,
    gamma: float = 1.05,
    std_thresh: float = 55.0
) -> list:
    """
    Evens out bimodal shadow/highlight spikes using luminance-coupled stretching
    so RGB color ratios remain balanced without false color casts.
    """
    if len(matrices) == 3:
        r = np.array(matrices[0], dtype=np.float64)
        g = np.array(matrices[1], dtype=np.float64)
        b = np.array(matrices[2], dtype=np.float64)
        lum = 0.299 * r + 0.587 * g + 0.114 * b

        if std_thresh > 0.0 and np.std(lum) < std_thresh:
            return matrices

        vmin, vmax = np.percentile(lum, [low_pct, high_pct])
        if vmax - vmin < 1e-6:
            return matrices

        norm_lum = np.clip((lum - vmin) / (vmax - vmin), 0.0, 1.0)
        if asinh_softness > 0.0:
            norm_lum = np.arcsinh(norm_lum * asinh_softness) / np.arcsinh(asinh_softness)
        if gamma != 1.0:
            norm_lum = np.power(norm_lum, 1.0 / gamma)

        target_lum = norm_lum * 255.0
        scale = target_lum / np.maximum(lum, 1.0)

        return [
            np.clip(r * scale, 0.0, 255.0).tolist(),
            np.clip(g * scale, 0.0, 255.0).tolist(),
            np.clip(b * scale, 0.0, 255.0).tolist()
        ]

    # Single-channel fallback
    balanced = []
    for ch_mat in matrices:
        arr = np.array(ch_mat, dtype=np.float64)

        if std_thresh > 0.0 and np.std(arr) < std_thresh:
            balanced.append(ch_mat)
            continue

        vmin, vmax = np.percentile(arr, [low_pct, high_pct])
        if vmax - vmin < 1e-6:
            balanced.append(ch_mat)
            continue

        norm = np.clip((arr - vmin) / (vmax - vmin), 0.0, 1.0)
        if asinh_softness > 0.0:
            norm = np.arcsinh(norm * asinh_softness) / np.arcsinh(asinh_softness)
        if gamma != 1.0:
            norm = np.power(norm, 1.0 / gamma)

        balanced.append((norm * 255.0).tolist())

    return balanced


def _finalize_and_save_single_frame(
    item_channels: list,
    base_stem: str,
    suffix: str,
    star_dir: Path,
    planet_dir: Path
):
    """Applies YCbCr->RGB conversion if needed, classifies, post-processes, and writes JPEG."""
    if len(item_channels) == 3 and COLOR_SPACE.upper() == "YCBCR":
        item_channels = ycbcr_to_rgb_matrices(item_channels)

    category = classify_space_image(item_channels)

    if category == "planetary":
        if ENABLE_DARK_PATCH_REMOVAL:
            item_channels = remove_dark_patches(
                item_channels, DARK_PATCH_KERNEL, DARK_PATCH_STRENGTH, DARK_PATCH_MODE
            )
        if ENABLE_LIGHT_BALANCE:
            item_channels = balance_crater_lighting(
                item_channels, LOW_PERCENTILE, HIGH_PERCENTILE,
                ASINH_SOFTNESS, GAMMA_VALUE, AUTO_BIMODAL_STD_THRESH
            )
        target_folder = planet_dir
    else:
        if ENABLE_LIGHT_BALANCE:
            item_channels = balance_crater_lighting(
                item_channels, low_pct=1.0, high_pct=99.9,
                asinh_softness=5.0, gamma=1.0, std_thresh=0.0
            )
        target_folder = star_dir

    sub_h = len(item_channels[0])
    sub_w = len(item_channels[0][0])
    color_tag = "RGB" if len(item_channels) == 3 else "BW"
    if sub_h > 0 and sub_w > 0:
        out_path = target_folder / f"{base_stem}{suffix}.jpg"
        write_jpg(out_path, item_channels, sub_w, sub_h, quality=JPEG_QUALITY)
        print(f"    [{category.upper()} | {color_tag}] {base_stem} -> {out_path}")


def reconstruct_and_save_matrices(matrices: list, base_stem: str, force_bayer: str = None):
    """Runs de-interleaving, ICER IDWT, Bayer demosaicing / YCbCr conversion, and classification."""
    star_dir = OUTPUT_JPG_DIR / "starfields"
    planet_dir = OUTPUT_JPG_DIR / "planetary_bodies"
    star_dir.mkdir(parents=True, exist_ok=True)
    planet_dir.mkdir(parents=True, exist_ok=True)

    # Bayer Mosaic Path (Single raw sensor matrix split into 2x2 quad_lattice -> demosaiced to RGB)
    if force_bayer in ("RGGB", "BGGR") and len(matrices) == 1:
        quad_planes = deinterleave_matrix(matrices[0], "quad_lattice")
        decompressed_quad = []
        for plane in quad_planes:
            recon = inv_dwt_2d(plane, STAGES)
            recon = remove_spatial_banding(recon, DEBAND_DIRECTION, SPATIAL_DEBAND_STRENGTH)
            decompressed_quad.append(recon)

        rgb_channels = demosaic_bayer_quad(decompressed_quad, pattern=force_bayer)
        _finalize_and_save_single_frame(rgb_channels, base_stem, "_bayer_rgb", star_dir, planet_dir)
        return

    # Standard Multi-Channel (3-plane RGB/YCbCr) or Single-Channel Path
    if DEINTERLEAVE_BEFORE_IDWT:
        split_per_channel = [deinterleave_matrix(ch_mat, LATTICE_MODE) for ch_mat in matrices]
        num_images = len(split_per_channel[0])

        for img_idx in range(num_images):
            item_channels = []
            for ch in range(len(matrices)):
                recon = inv_dwt_2d(split_per_channel[ch][img_idx], STAGES)
                recon = remove_spatial_banding(recon, DEBAND_DIRECTION, SPATIAL_DEBAND_STRENGTH)
                item_channels.append(recon)

            suffix = f"_{img_idx + 1}" if num_images > 1 else ""
            _finalize_and_save_single_frame(item_channels, base_stem, suffix, star_dir, planet_dir)


# =====================================================================
# MAIN PIPELINE ORCHESTRATOR
# =====================================================================
def _payload_to_2d(payload: bytes, width_override: int = None):
    width = width_override if width_override else detect_row_width(payload)
    if width <= 0:
        return None, 0, 0
    height = len(payload) // width
    if height < (2 ** STAGES):
        return None, width, height
    usable = width * height
    arr_2d = np.frombuffer(payload[:usable], dtype=np.uint8).astype(np.float64).reshape(height, width)
    return arr_2d, width, height


def run_full_pipeline():
    check_ubuntu_jpeg_tools()
    OUTPUT_JPG_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Extract and descramble telemetry binary streams
    active_apid_streams = extract_clean_telemetry(TELEMETRY_BIN, TARGET_APIDS, BLOCK_SIZE)

    # 2. Process extracted APID binary payloads with color ICER detection
    if active_apid_streams:
        print(f"\n--- Stage 2A: Reconstructing Extracted APID Wavelet Streams (COLOR_MODE={COLOR_MODE}) ---")
        sorted_apids = sorted(active_apid_streams.keys())
        consumed_apids = set()

        # Pass A: Check for 3-APID color triplets (APID N, N+1, N+2 with matching byte sizes)
        if COLOR_MODE in ("auto", "apid_triplets"):
            for i in range(len(sorted_apids) - 2):
                a0, a1, a2 = sorted_apids[i], sorted_apids[i + 1], sorted_apids[i + 2]
                if a0 in consumed_apids or a1 in consumed_apids or a2 in consumed_apids:
                    continue
                if (a1 == a0 + 1) and (a2 == a0 + 2):
                    len0 = len(active_apid_streams[a0])
                    len1 = len(active_apid_streams[a1])
                    len2 = len(active_apid_streams[a2])
                    if abs(len0 - len1) <= BLOCK_SIZE and abs(len0 - len2) <= BLOCK_SIZE:
                        min_len = min(len0, len1, len2)
                        arr0, w, h = _payload_to_2d(active_apid_streams[a0][:min_len], IMAGE_WIDTH)
                        arr1, _, _ = _payload_to_2d(active_apid_streams[a1][:min_len], w)
                        arr2, _, _ = _payload_to_2d(active_apid_streams[a2][:min_len], w)

                        if arr0 is not None and arr1 is not None and arr2 is not None:
                            print(f"[*] Processing Color APID Triplet {a0}/{a1}/{a2} ({w}x{h} {COLOR_SPACE})...")
                            reconstruct_and_save_matrices(
                                [arr0.tolist(), arr1.tolist(), arr2.tolist()],
                                f"apid_{a0}_{a1}_{a2}_color"
                            )
                            consumed_apids.update([a0, a1, a2])

        # Pass B: Process remaining individual APIDs (3-plane stacked, Bayer mosaic, or grayscale)
        for apid in sorted_apids:
            if apid in consumed_apids:
                continue

            payload = active_apid_streams[apid]
            arr_2d, width, height = _payload_to_2d(payload, IMAGE_WIDTH)
            if arr_2d is None:
                print(f"[SKIP] APID {apid}: Dimensions ({width}x{height}) invalid for {STAGES}-stage IDWT.")
                continue

            if COLOR_MODE == "planar_3ch" or (COLOR_MODE == "auto" and check_planar_color_correlation(arr_2d)):
                plane_h = height // 3
                if plane_h >= (2 ** STAGES):
                    p0 = arr_2d[0:plane_h, :].tolist()
                    p1 = arr_2d[plane_h:2 * plane_h, :].tolist()
                    p2 = arr_2d[2 * plane_h:3 * plane_h, :].tolist()
                    print(f"[*] Processing APID {apid} as 3-Plane {COLOR_SPACE} ({width}x{plane_h})...")
                    reconstruct_and_save_matrices([p0, p1, p2], f"apid_{apid}_3ch")
                    continue

            if COLOR_MODE in ("bayer_rggb", "bayer_bggr"):
                pattern = "BGGR" if COLOR_MODE == "bayer_bggr" else "RGGB"
                print(f"[*] Processing APID {apid} as Bayer {pattern} ({width}x{height})...")
                reconstruct_and_save_matrices([arr_2d.tolist()], f"apid_{apid}", force_bayer=pattern)
                continue

            # In "auto" mode with quad_lattice, export BOTH standard de-interleaved frames AND a Bayer RGB composite
            print(f"[*] Processing APID {apid} ({width}x{height} raw matrix)...")
            reconstruct_and_save_matrices([arr_2d.tolist()], f"apid_{apid}_final")
            if COLOR_MODE == "auto" and LATTICE_MODE == "quad_lattice":
                reconstruct_and_save_matrices([arr_2d.tolist()], f"apid_{apid}", force_bayer="RGGB")

    # 3. Process any pre-existing wavelet JPEGs in WAVELET_JPG_DIR (supports both P5 gray and P6 RGB)
    if WAVELET_JPG_DIR.exists():
        jpg_files = sorted(WAVELET_JPG_DIR.glob("*.jpg")) + sorted(WAVELET_JPG_DIR.glob("*.jpeg"))
        if jpg_files:
            print(f"\n--- Stage 2B: Reconstructing {len(jpg_files)} Pre-existing Wavelet JPEGs ---")
            for jpg_path in jpg_files:
                matrices, w, h = read_jpg(jpg_path)
                print(f"[*] Reconstructing {jpg_path.name} ({w}x{h}, {len(matrices)} ch)...")
                reconstruct_and_save_matrices(matrices, jpg_path.stem)


if __name__ == "__main__":
    run_full_pipeline()
