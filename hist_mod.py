import cv2
import numpy as np
from matplotlib import pyplot as plt


# load an image in grayscale mode
img = cv2.imread('ex.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
img = cv2.resize(img, (225, 225))
# cv2.imshow("frame",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

l, u, v = cv2.split(img)

# calculate frequency of pixels in range 0-255

histl = cv2.calcHist([l], [0], None, [256], [0, 256])
histu = cv2.calcHist([u], [0], None, [256], [0, 256])
histv = cv2.calcHist([v], [0], None, [256], [0, 256])

eq_histl = cv2.equalizeHist(l)
eq_histu = cv2.equalizeHist(u)
eq_histv = cv2.equalizeHist(v)


