import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. Load and prepare image
img = Image.open('examples/example.jpg')  # Changed to relative path
img_gray = img.convert('L')
img_array = np.array(img_gray)

# 2. FFT
f_transform = np.fft.fft2(img_array)
f_shift = np.fft.fftshift(f_transform)
magnitude_spectrum = 20 * np.log(np.abs(f_shift))

# 3. Create circular mask for low frequencies
rows, cols = img_array.shape
crow, ccol = rows//2, cols//2
radius = 40

y, x = np.ogrid[-crow:rows-crow, -ccol:cols-ccol]
mask = x*x + y*y <= radius*radius  # Mask for low frequencies
mask = mask.astype(float)

# 4. Apply mask to FFT
f_shift_masked = f_shift * (1 - mask)

# 5. Calculate phase
phase = np.angle(f_shift)
phase_masked = np.angle(f_shift_masked)

# 6. Inverse FFT
f_inverse_shift = np.fft.ifftshift(f_shift_masked)
img_reconstructed = np.fft.ifft2(f_inverse_shift)
img_reconstructed = np.abs(img_reconstructed)

# Display results
fig = plt.figure(figsize=(15, 10))

plt.subplot(231)
plt.imshow(img_array, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(232)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('FFT Spectrum')
plt.axis('off')

plt.subplot(233)
plt.imshow(phase, cmap='gray')
plt.title('Phase')
plt.axis('off')

plt.subplot(234)
masked_spectrum = 20 * np.log(np.abs(f_shift_masked) + 1)
plt.imshow(masked_spectrum, cmap='gray')
plt.title('Masked FFT (Low Freqs)')
plt.axis('off')

plt.subplot(235)
plt.imshow(phase_masked, cmap='gray')
plt.title('Masked Phase')
plt.axis('off')

plt.subplot(236)
plt.imshow(img_reconstructed, cmap='gray')
plt.title('Reconstructed Image')
plt.axis('off')

plt.tight_layout()
plt.show()
