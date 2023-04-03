from PIL import Image, ImageFilter
import os
from math import sqrt
from utils import show_horizontal, show_vertical, in_file, out_file

def show_edges(filename, direction='x', offset=0, threshold=128):
    original = Image.open(in_file(filename)).convert('L')
    XSOBEL = ImageFilter.Kernel((3, 3),
                                [-1, 0, 1,
                                 -2, 0, 2,
                                 -1, 0, 1],
                                1,
                                offset)
    YSOBEL = ImageFilter.Kernel((3, 3),
                                [-1, -2, -1,
                                 0, 0, 0,
                                 1, 2, 1],
                                1,
                                offset)
    w, h = original.size
    if direction == 'x':
        filtered = original.filter(XSOBEL)
    elif direction == 'y':
        filtered = original.filter(YSOBEL)
    else:
        vsobel = original.filter(XSOBEL)
        hsobel = original.filter(YSOBEL)
        filtered = Image.new('L', (w, h))

        for i in range(w):
            for j in range(h):
                value = sqrt(vsobel.getpixel((i,j))**2 + hsobel.getpixel((i,j))**2)
                value = int(min(value, 255))
                filtered.putpixel((i, j), value)

    # Thresholding
    D = []
    for j in range(h):
        row = []
        for i in range(w):
            if filtered.getpixel((i, j)) < threshold:
                row.append(0)
            else:
                row.append(1)
        D.append(row)

    show_horizontal(original, filtered)
    filtered.save(
        out_file(
            '{}_{}sobel_{}_th{}.jpg'.format(
                filename[:filename.index('.')],
                direction,
                offset,
                threshold)
        )
    )

    return D

if __name__ == "__main__":
    D1 = show_edges('Inosukefiltered.jpeg', 'y', 0, threshold=128)
    D2 = show_edges('Inosukefiltered.jpeg', 'x', 0, threshold=128)
    D3 = show_edges('Inosukefiltered.jpeg', 'a', 0, threshold=128)

    # example of using the generated D matrix
    print(D1[0][0])  # access the top-left pixel in D1