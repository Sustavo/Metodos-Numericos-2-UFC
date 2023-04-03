import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
from utils import in_file, out_file

matplotlib.use('TkAgg')
laplacian_filter = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])

# Load the image
img = np.array(Image.open(in_file('Inosukefiltered.jpeg')).convert('L'))

# Apply the Laplacian filter
filtered_img = np.zeros_like(img)
tolerance = 0.0001
for i in range(1, img.shape[0]-1):
    for j in range(1, img.shape[1]-1):
        if abs(img[i, j]) < tolerance:
            filtered_img[i, j] = 1  # or any desired value
        else:
            filtered_img[i, j] = np.sum(laplacian_filter * img[i-1:i+2, j-1:j+2])

# Save the filtered image
Image.fromarray(filtered_img.astype(np.uint8)).save(out_file('Inosukefiltered_zero.jpeg'))

# Plot the original and filtered images
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')
axs[1].imshow(filtered_img, cmap='gray')
axs[1].set_title('Filtered Image')
axs[1].axis('off')
plt.show()