from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
from scipy.signal import convolve2d

load_image('lena (1).jpg')
clean_image = median(arr_image, ball(6))
edge_detection(clean_image)
threshold = 140
binary_image = edged_image > threshold
binary_image = binary_image.astype(np.uint8) * 255
edge_image = Image.fromarray(binary_image)
edge_image.save('my_edges.png')
