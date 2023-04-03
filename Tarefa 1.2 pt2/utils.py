from PIL import Image, ImageFilter
import os
import numpy as np

# Caminho relativo das pastas de entrada e saída de imagens
INPUT_DIR = os.path.join('images', 'input')
OUTPUT_DIR = os.path.join('images', 'output')


def in_file(filename):
    '''Retorna o caminho de um arquivo de entrada'''

    return os.path.join(INPUT_DIR, filename)

def out_file(filename):
    '''Retorna o caminho de um arquivo de saída'''

    return os.path.join(OUTPUT_DIR, filename)

