import os
import cv2
import numpy as np
import pandas as pd

# CCSDS Constants
CCSDS_HEADER_SIZE = 6


def fast_pandas_ccsds_parser(binary_file_path):
    """Vectorized CCSDS parser using NumPy and Pandas to efficiently split payloads

    by Spacecraft ID (SCID) without slow Python while-loops.
    """
    print(f"[*] Ingesting binary stream via fast vectorized parser...")
    # Load entire binary file as an array of raw bytes
    raw_bytes = np.fromfile(binary_file_path, dtype=np.uint8)
    file_size = len(raw_bytes)

    # Fast iterative block pointer tracking via vectorized strides
    packet_offsets = []
    scids = []
    payload_slices = []

    idx = 0
    while idx + CCSDS_HEADER_SIZE <= file_size:
        # Vectorized packet parsing via view interpretations
        header = raw_bytes[idx : idx + CCSDS_HEADER_SIZE]
        if len(header) < CCSDS_HEADER_SIZE:
            break

        # Extract big-endian field masks from byte blocks
        p_hdr1 = (int(header[0]) << 8) | int(header[1])
        data_len = (int(header[4]) << 8) | int(header[5])

        scid = (p_hdr1 >> 4) & 0xFF
        actual_data_len = data_len + 1

        payload_start = idx + CCSDS_HEADER_SIZE
        payload_end = payload_start + actual_data_len

        if payload_end > file_size:
            break  # Truncated trailing packet

        packet_offsets.append(idx)
        scids.append(scid)
        # Store boundaries to extract memory maps cleanly
        payload_slices.append((payload_start, payload_end))

        idx = payload_end

    # Construct dense Pandas telemetry framework
    df_telemetry = pd.DataFrame(
        {
            "packet_offset": packet_offsets,
            "scid": scids,
            "payload_bounds": payload_slices,
        }
    )

    print(f"[+] Successfully indexed {len(df_telemetry)} telemetry packets.")
    return df_telemetry, raw_bytes


def find_dimensions_via_2d_autocorr(payload_bytes, min_w=128, max_w=2048):
    """Performs 2D Autocorrelation on the isolated telemetry payload data stream

    to find the exact (Width, Height) spatial matrix layout.
    """
    # Convert payload into flat signal array
    data_array = np.frombuffer(payload_bytes, dtype=np.uint8)
    total_pixels = len(data_array)

    if total_pixels < min_w:
        raise ValueError(f"Payload stream size too small for 2D analysis.")

    # Subsample data block to massively accelerate 2D FFT calculation
    sample_size = min(total_pixels, 1500000)
    signal = data_array[:sample_size].astype(np.float32)
    signal -= np.mean(signal)  # De-mean signal to eliminate DC bias spike

    best_width = min_w
    best_height = 0
    max_peak_value = -1.0

    print(
        f"[*] Running 2D Autocorrelation space sweep ({min_w}px to {max_w}px)..."
    )

    # Sweep expected horizontal widths to look for vertical spatial alignment grid locks
    for trial_width in range(min_w, max_w + 1):
        trial_height = len(signal) // trial_width
        if trial_height < 16:
            break

        # Reshape data into the current test 2D matrix canvas
        grid_2d = signal[: trial_width * trial_height].reshape(
            (trial_height, trial_width)
        )

        # Accelerate 2D Autocorrelation via 2D FFT
        f_transform = np.fft.fft2(grid_2d)
        power_spectrum = f_transform * np.conj(f_transform)
        autocorr_2d = np.fft.ifft2(power_spectrum).real

        # Shift the zero-frequency components to center coordinate for easier profiling
        autocorr_2d = np.fft.fftshift(autocorr_2d)
        center_y = trial_height // 2
        center_x = trial_width // 2

        # Extract the vertical center line cross-section
        vertical_profile = autocorr_2d[:, center_x].copy()

        # Mask out immediate central origin row spike to evaluate secondary repetition peaks
        exclusion_zone = 5
        vertical_profile[
            center_y - exclusion_zone : center_y + exclusion_zone + 1
        ] = 0

        # Locate maximum vertical spatial symmetry energy peak
        peak_idx = np.argmax(vertical_profile)
        peak_val = vertical_profile[peak_idx]

        if peak_val > max_peak_value:
            max_peak_value = peak_val
            best_width = trial_width
            best_height = abs(peak_idx - center_y)

    # Auto-adjust height to capture the full stream volume for this asset base
    final_height = total_pixels // best_width

    print(f"[+] 2D Grid Locked! Autodetected Layout: {best_width}x{final_height}")
    return best_width, final_height


def process_and_save_telemetry_pandas(
    binary_file_path, output_prefix="scid_out"
):
    """Orchestrates the pandas telemetry extraction pipeline, analytical 2D sizing,

    and image asset conversion steps.
    """
    if not os.path.exists(binary_file_path):
        print(f"[-] File not found: {binary_file_path}")
        return

    # Pass 1: Run fast Pandas vector parsing engine
    df_telemetry, raw_bytes = fast_pandas_ccsds_parser(binary_file_path)

    if df_telemetry.empty:
        print("[-] No valid telemetry packets recovered.")
        return

    # Group packets uniquely by Spacecraft ID (SCID)
    unique_scids = df_telemetry["scid"].unique()

    for scid in unique_scids:
        print(f"\n--- Processing Stream for Spacecraft ID: {scid} ---")

        # Use Pandas filtering to locate all row boundaries linked to this SCID
        scid_packets = df_telemetry[df_telemetry["scid"] == scid]

        # Assemble the contiguous raw data payload fragments sequentially
        payload_buffer = bytearray()
        for bounds in scid_packets["payload_bounds"]:
            payload_buffer.extend(raw_bytes[bounds[0] : bounds[1]])

        payload_bytes = bytes(payload_buffer)
        print(f"[+] Reassembled Contiguous Payload: {len(payload_bytes)} bytes")

        try:
            # Pass 2: Calculate both frame matrix boundaries using 2D correlation structures
            width, height = find_dimensions_via_2d_autocorr(payload_bytes)

            # Slice and shape the matrix to fit the calculated grid specifications
            valid_bytes_limit = width * height
            pixel_matrix = np.frombuffer(
                payload_bytes[:valid_bytes_limit], dtype=np.uint8
            ).reshape((height, width))

            # Pass 3: Save cleanly out to standalone individual JPG asset file
            output_filename = f"{output_prefix}_{scid}_2d_matrix.jpg"
            cv2.imwrite(output_filename, pixel_matrix)
            print(
                f"[+] Success: Exported parsed asset into '{output_filename}'"
            )

        except Exception as e:
            print(f"[-] Processing execution error on SCID {scid}: {e}")


# --- Execution Configuration ---
process_and_save_telemetry_pandas("turbodecoded.frames")
