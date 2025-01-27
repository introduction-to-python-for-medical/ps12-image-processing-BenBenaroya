from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    my_image = Image.open(file_path)
    arr_image = np.array(my_image)
    return arr_image

def edge_detection(image):
    grayscale_image = np.mean(clean_image, axis=2)
    kernelY = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    kernelX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    filted_x = convolve2d(grayscale_image, kernelX)
    filted_y = convolve2d(grayscale_image, kernelY)
    edged_image = np.sqrt(filted_x**2 + filted_y**2)
    return edged_image
