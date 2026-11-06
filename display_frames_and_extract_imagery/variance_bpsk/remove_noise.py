import cv2
import numpy as np

def hybrid_median_filter(img, size=5):
    """
    Applies a hybrid median filter to protect thin line spatial widths
    while aggressively discarding extreme impulse pixels.
    """
    radius = size // 2
    padded = cv2.copyMakeBorder(img, radius, radius, radius, radius, cv2.BORDER_REFLECT)
    output = img.copy()
    
    for y in range(radius, padded.shape[0] - radius):
        for x in range(radius, padded.shape[1] - radius):
            # Extract the window local patch
            window = padded[y-radius:y+radius+1, x-radius:x+radius+1]
            
            # Cross neighbors (Horizontal + Vertical center lines)
            cross = np.hstack([window[radius, :], window[:, radius]])
            median_cross = np.median(cross)
            
            # Diagonal neighbors (X shape lines)
            diag1 = np.diag(window)
            diag2 = np.diag(np.fliplr(window))
            diagonals = np.hstack([diag1, diag2])
            median_diag = np.median(diagonals)
            
            # Compare with the original pixel to choose the structure-preserving value
            pixel = window[radius, radius]
            output[y-radius, x-radius] = np.median([median_cross, median_diag, pixel])
            
    return output

def restore_spatial_shading(input_path="scid_out_206_2d_matrix.jpg", output_path="restored_spatial_shading.png"):
    # 1. Load image in grayscale
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"[-] Error: Could not find or open input image file: {input_path}")
        return

    print("[*] Image loaded. Initializing structure-preserving restoration pipeline...")

    # 2. Run Hybrid Median Filter to keep thin shapes wide
    denoised_img = hybrid_median_filter(img, size=5)

    # 3. Use Morphological Reconstruction (Dilation + Min) to restore light gray widths
    # This prevents the edges of light gray patches from eroding away into dark noise regions
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(denoised_img, kernel)
    reconstructed_gray = cv2.min(dilated, img) # Bound it back to original boundary envelopes

    # 4. Apply a mild bilateral filter to smooth remaining noise without shifting gray gradients
    final_img = cv2.bilateralFilter(reconstructed_gray, d=5, sigmaColor=50, sigmaSpace=25)

    # 5. Export clean raster output
    cv2.imwrite(output_path, final_img)
    print(f"[+] Spatial restoration complete! File saved to: {output_path}")

if __name__ == "__main__":
    restore_spatial_shading()
