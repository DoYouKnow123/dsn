import cv2
import matplotlib.pyplot as plt
import numpy as np


def find_image_width_via_autocorrelation(filepath, max_width_guess=2048):
    # 1. Load the raw binary data as a 1D sequence of unsigned 8-bit integers
    raw_data = np.fromfile(filepath, dtype=np.uint8)

    # Use a chunk of data for performance (e.g., first 500k bytes)
    # Ensure it's long enough to cover several rows of an image
    signal_chunk = raw_data[:500000].astype(np.float32)

    # Center the signal around zero to eliminate a massive DC bias peak
    signal_chunk -= np.mean(signal_chunk)

    # 2. Compute 1D Autocorrelation using FFT for O(N log N) speed
    n = len(signal_chunk)
    fft_vals = np.fft.fft(signal_chunk, n=2 * n)
    power_spectrum = fft_vals * np.conj(fft_vals)
    autocorr = np.fft.ifft(power_spectrum).real[:n]

    # Normalize the autocorrelation output
    if autocorr[0] != 0:
        autocorr /= autocorr[0]

    # 3. Find the dominant structural period (Width)
    # Ignore the absolute peak at lag=0; look for peaks between reasonable width bounds
    min_width_bound = 16
    search_region = autocorr[min_width_bound:max_width_guess]

    # Find the local maxima within our search region
    detected_width = min_width_bound + np.argmax(search_region)
    peak_strength = search_region[np.argmax(search_region)]

    print(f"Detected dominant image width (stride): {detected_width} pixels")
    print(f"Peak correlation strength: {peak_strength:.4f}")

    return detected_width, raw_data


def extract_and_render_image(raw_data, width, height=480, offset=0):
    # 4. Slice out the suspected frame size based on detected stride
    frame_size = width * height

    if offset + frame_size > len(raw_data):
        print("Warning: Requested frame boundaries exceed file size.")
        frame_data = raw_data[offset:]
        # Calculate trailing dimension dynamically if short
        height = len(frame_data) // width
        frame_data = frame_data[: width * height]
    else:
        frame_data = raw_data[offset : offset + frame_size]

    # Reshape the 1D segment into 2D raster matrix
    image_matrix = frame_data.reshape((height, width))

    # Render image using matplotlib or opencv
    plt.figure(figsize=(10, 6))
    plt.imshow(image_matrix, cmap="gray", aspect="auto")
    plt.title(f"Extracted Image Frame (Width: {width}, Offset: {offset})")
    plt.colorbar(label="Pixel Intensity")
    plt.show()


# --- Execution Pipeline ---
file_path = "raw_payload_stream.bin"
width, binary_stream = find_image_width_via_autocorrelation(file_path)
extract_and_render_image(binary_stream, width=width, height=640, offset=0)
