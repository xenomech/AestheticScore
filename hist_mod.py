import cv2
import numpy as np
from matplotlib import pyplot as plt


# load an image in grayscale mode
img = cv2.imread('ex.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
