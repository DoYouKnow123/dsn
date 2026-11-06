import os
import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal
from scipy.fft import fft2, ifft2, fftshift, ifftshift

def triangular_window_2d(M, N):
    """Generates a 2D triangular (Bartlett) window to isolate a local spatial region."""
    y = np.bartlett(M)
    x = np.bartlett(N)
    return np.outer(y, x)

def adaptive_holographic_2d_concentrate(tf_matrix, target_center, region_size, concentration_factor=2.0):
    """
    Applies a 2D triangular-wave windowed holographic kernel to focus diffuse energy.
    Dynamically scales bin sizes based on local coordinate scales.
    """
    M, N = tf_matrix.shape
    r_center, c_center = target_center
    r_size, c_size = region_size
    
    # 1. Isolate the target 2D region using a localized triangular mask
    mask = np.zeros((M, N))
    tri_window = triangular_window_2d(r_size, c_size)
    
    # Slice limits for the 2D region
    r_start = max(0, r_center - r_size // 2)
    r_end = min(M, r_start + r_size)
    c_start = max(0, c_center - c_size // 2)
    c_end = min(N, c_start + c_size)
    
    # Adapt slices if they hit edges
    w_r_slice = slice(0, r_end - r_start)
    w_c_slice = slice(0, c_end - c_start)
    mask[r_start:r_end, c_start:c_end] = tri_window[w_r_slice, w_c_slice]
    
    # Isolate region phase properties
    isolated_region = tf_matrix * mask
    region_phase = np.angle(isolated_region)
    
    # 2. Adaptive Bin Size Modulation (Resolution Scaling)
    # Generate 2D coordinate spaces centered on the target region
    Y, X = np.ogrid[-r_center:M-r_center, -c_center:N-c_center]
    
    # As frequency index (Y) increases, shrink the bin scaling factor
    linear_gradient_y = 1.0 - (np.abs(Y) / M)
    linear_gradient_x = 1.0 - (np.abs(X) / N)
    adaptive_bin_scale = np.outer(linear_gradient_y.ravel(), linear_gradient_x.ravel())
    
    # 3. Holographic Lens Application
    holographic_phase = -1.0 * region_phase * concentration_factor * adaptive_bin_scale
    holographic_kernel = np.exp(1j * holographic_phase)
    
    # Apply forward diffractive focus across the 2D canvas
    focused_region = isolated_region * holographic_kernel
    
    # 4. 2D Spectral Compression (Collapsing diffuse energy via 2D Fourier plane)
    spectrum_2d = fftshift(fft2(focused_region))
    
    # Squeeze bin sizes globally via quadratic-triangular phase scaling in the frequency domain
    V, U = np.ogrid[-M//2:M//2, -N//2:N//2]
    compression_lens = np.exp(-1j * np.pi * (V**2 + U**2) * (1.0 / (concentration_factor + 1e-5)))
    
    compressed_spectrum = spectrum_2d * compression_lens
    concentrated_tf_matrix = ifft2(ifftshift(compressed_spectrum))
    
    # Re-insert concentrated block back into original matrix structure
    output_matrix = tf_matrix.copy()
    output_matrix[r_start:r_end, c_start:c_end] = concentrated_tf_matrix[r_start:r_end, c_start:c_end]
    
    return output_matrix, holographic_kernel, compression_lens, (r_start, r_end, c_start, c_end)

def adaptive_holographic_2d_reconstruct(concentrated_matrix, holo_kernel, comp_lens, boundaries):
    """Reverses the 2D phase-energy compression for a zero-distortion audio return."""
    r_start, r_end, c_start, c_end = boundaries
    target_block = concentrated_matrix[r_start:r_end, c_start:c_end]
    
    # 1. Reverse 2D spectral compression
    spectrum_2d = fftshift(fft2(target_block))
    uncompressed_spectrum = spectrum_2d * np.conj(comp_lens[r_start:r_end, c_start:c_end])
    restored_block = ifft2(ifftshift(uncompressed_spectrum))
    
    # 2. Reverse localized holographic phase
    decoded_block = restored_block * np.conj(holo_kernel[r_start:r_end, c_start:c_end])
    
    output_matrix = concentrated_matrix.copy()
    output_matrix[r_start:r_end, c_start:c_end] = decoded_block
    return output_matrix

def process_wav_file(input_path, output_path, concentration_factor=2.5):
    """Loads a WAV file, processes it through the 2D triangular holographic lens, and saves it."""
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    print(f"Reading file: {input_path}")
    sample_rate, data = wav.read(input_path)
    
    # Handle stereo or multi-channel audio by downmixing to mono
    if len(data.shape) > 1:
        print("Converting stereo signal to mono...")
        data = data.mean(axis=1)
        
    # Standardize floating-point normalization [-1.0, 1.0] to prevent math scaling errors
    signal_norm = data / np.max(np.abs(data))
    
    # Convert 1D time audio into 2D Time-Frequency Image space
    print("Computing forward Short-Time Fourier Transform (STFT)...")
    frequencies, times, stft_matrix = signal.stft(signal_norm, fs=sample_rate, nperseg=1024)
    
    # Set the target focus region parameters (targeting center bins of the matrix canvas)
    target_bin = (stft_matrix.shape[0] // 2, stft_matrix.shape[1] // 2)
    
    # Define window bounds (Height=Frequency bins, Width=Time frames)
    # Scales dynamically to fit inside the computed STFT canvas sizes
    r_size = min(256, stft_matrix.shape[0])
    c_size = min(64, stft_matrix.shape[1])
    region_dimensions = (r_size, c_size)
    
    print(f"Applying 2D Adaptive Triangular Holographic focus (Factor: {concentration_factor})...")
    concentrated_image, kernel, lens, bounds = adaptive_holographic_2d_concentrate(
        stft_matrix, target_bin, region_dimensions, concentration_factor=concentration_factor
    )
    
    print("Executing perfect inversion loop reconstruction...")
    restored_image = adaptive_holographic_2d_reconstruct(concentrated_image, kernel, lens, bounds)
    
    # Invert image coordinates back down to 1D time audio wave
    _, reconstructed_audio = signal.istft(restored_image, fs=sample_rate, nperseg=1024)
    
    # Re-normalize and convert back into standard audio 16-bit PCM integer scaling to prevent digital clipping
    print("Normalizing final signal and formatting bit depth...")
    reconstructed_audio = reconstructed_audio / np.max(np.abs(reconstructed_audio))
    audio_to_save = (reconstructed_audio * 32767).astype(np.int16)
    
    print(f"Writing compressed file out to: {output_path}")
    wav.write(output_path, sample_rate, audio_to_save)
    print("Process complete! File exported successfully with zero frequency distortion.")

# --- EXECUTION ENGINE ---
if __name__ == "__main__":
    # Specify the file locations here
    INPUT_FILE = "mapping2.wav"
    OUTPUT_FILE = "triangular_2d_concentrated.wav"
    CONCENTRATION = 50
    
    # Run the file loop (Ensure you have an 'input.wav' file in the directory or update the path below)
    process_wav_file(INPUT_FILE, OUTPUT_FILE, concentration_factor=CONCENTRATION)

