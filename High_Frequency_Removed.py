import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. Load and prepare image
img = Image.open('examples.jpg')  # Changed to relative path
img_gray = img.convert('L')
img_array = np.array(img_gray)

# 2. FFT transform
f_transform = np.fft.fft2(img_array)
f_shift = np.fft.fftshift(f_transform)
magnitude_spectrum = 20 * np.log(np.abs(f_shift))

# 3. Create circular mask
rows, cols = img_array.shape  # Get dimensions of the image array
crow, ccol = rows//2, cols//2  # Find center point of the image
radius = 40  # Set circle radius to 40 pixels

# Create coordinate grid centered at (crow,ccol) using memory-efficient ogrid
y, x = np.ogrid[-crow:rows-crow, -ccol:cols-ccol]
mask = x*x + y*y <= radius*radius  # Create circular mask using x² + y² ≤ r²
mask = mask.astype(float)  # Convert boolean mask to float (True->1.0, False->0.0)

# 4. Apply mask to FFT
# When multiplying by (1 - mask):
# - mask=1 → 1-1=0 → remove these frequencies
# - mask=0 → 1-0=1 → keep these frequencies
f_shift_masked = f_shift * (1 - mask)

# 5. Calculate phase
phase = np.angle(f_shift)
phase_masked = np.angle(f_shift_masked)

# 6. Inverse FFT
f_inverse_shift = np.fft.ifftshift(f_shift_masked)
img_reconstructed = np.fft.ifft2(f_inverse_shift)
img_reconstructed = np.abs(img_reconstructed)

# Create figure for visualization
fig = plt.figure(figsize=(15, 10))

# 1. Original image
plt.subplot(231)
plt.imshow(img_array, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# 2. FFT spectrum
plt.subplot(232)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('FFT Spectrum')
plt.axis('off')

# 3. Phase
plt.subplot(233)
plt.imshow(phase, cmap='gray')
plt.title('Phase')
plt.axis('off')

# 4. Masked FFT spectrum
masked_spectrum = 20 * np.log(np.abs(f_shift_masked) + 1)  # Add 1 to avoid log(0)
plt.subplot(234)
plt.imshow(masked_spectrum, cmap='gray')
plt.title('Masked FFT')
plt.axis('off')

# 5. Masked Phase
plt.subplot(235)
plt.imshow(phase_masked, cmap='gray')
plt.title('Masked Phase')
plt.axis('off')

# 6. Reconstructed Image
plt.subplot(236)
plt.imshow(img_reconstructed, cmap='gray')
plt.title('Reconstructed Image')
plt.axis('off')

plt.tight_layout()
plt.show()
