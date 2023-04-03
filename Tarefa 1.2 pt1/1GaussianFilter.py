import numpy as np
from PIL import Image
from utils import show_horizontal, show_vertical, in_file, out_file


def gaussian_kernel(size, sigma):
    """
    Creates a Gaussian kernel of the given size and standard deviation.
    """
    x, y = np.meshgrid(np.linspace(-1, 1, size), np.linspace(-1, 1, size))
    d = np.sqrt(x*x + y*y)
    kernel = np.exp(-((d**2)/(2.0*sigma**2)))
    return kernel / np.sum(kernel)

def convolve(image, kernel):
    """
    Applies a 2D convolution on the given image using the given kernel.
    """
    w, h = image.shape
    kw, kh = kernel.shape
    pad_w, pad_h = kw // 2, kh // 2

    # Pad the image with zeros
    padded_image = np.zeros((w + 2 * pad_w, h + 2 * pad_h))
    padded_image[pad_w:-pad_w, pad_h:-pad_h] = image

    # Apply the convolution
    result = np.zeros_like(image)
    for i in range(pad_w, w + pad_w):
        for j in range(pad_h, h + pad_h):
            result[i - pad_w, j - pad_h] = (kernel * padded_image[i - pad_w:i + pad_w + 1, j - pad_h:j + pad_h + 1]).sum()

    return result


def gaussian_filter(image, sigma):
    """
    Applies a Gaussian filter on the given image with the given standard deviation.
    """
    kernel_size = int(2 * np.ceil(3 * sigma) + 1)
    kernel = gaussian_kernel(kernel_size, sigma)
    return convolve(image, kernel)


if __name__ == "__main__":
    # Load the image
    img = np.array(Image.open(in_file("Inosuke.jpg")).convert('L'))

    # Apply the Gaussian filter
    smoothed_img = gaussian_filter(img, sigma=3)

    # Save the smoothed image
    Image.fromarray(smoothed_img.astype(np.uint8)).save(out_file("shoto_filtered.jpeg"))