import os
from PIL import Image
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


def compress(file, frames):

    # Get the path of the file
    filepath = os.path.join(os.getcwd(), "frames/"+file)
    savepath = os.path.join(os.getcwd(), "compressed")
    # print(savepath)
    # open the image
    picture = Image.open(filepath)
    picture.save(savepath+"/Compressed_"+file,
                 "JPEG", optimize=True, quality=10)
    size = os.path.getsize(savepath+"/Compressed_"+file)
    return size


def colorfulness(file):
    filepath = os.path.join(os.getcwd(), "frames/"+file)
    # load an image in grayscale mode
    img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
    img = cv2.resize(img, (225, 225))
    # cv2.imshow("frame",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    l, u, v = cv2.split(img)

    eq_histl = cv2.equalizeHist(l)
    eq_histu = cv2.equalizeHist(u)
    eq_histv = cv2.equalizeHist(v)

    # calculate frequency of pixels in range 0-255

    histl = cv2.calcHist([l], [0], None, [len(eq_histl)], [0, len(eq_histl)])
    histu = cv2.calcHist([u], [0], None, [len(eq_histu)], [0, len(eq_histu)])
    histv = cv2.calcHist([v], [0], None, [len(eq_histv)], [0, len(eq_histv)])

    # finding sum of squares
    sum_sql = np.sum(np.square(eq_histl - histl))
    sum_squ = np.sum(np.square(eq_histu - histu))
    sum_sqv = np.sum(np.square(eq_histv - histv))

    # Doing squareroot and
    d_l = np.sqrt(sum_sql)/2
    d_u = np.sqrt(sum_squ)/2
    d_v = np.sqrt(sum_sqv)/2
    # printing Euclidean distance
    return ((d_l+d_u+d_v)/3)/1000000


def main():
    # finds current working dir
    frames = os.path.join(os.getcwd(), "frames")
    formats = ('.jpg', '.jpeg')
    complexscore = []
    colourfulnessscore = []
    # looping through all the files
    # in a current directory
    for file in os.listdir(frames):
        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            # print('compressing', file)
            compresedframesize = compress(file, frames)
            ogframesize = os.path.getsize(frames+"/"+file)
            cr = ogframesize/compresedframesize
            crate = 1/cr
            cscore = crate/2
            complexscore.append(cscore)
            clrscore = colorfulness(file)
            colourfulnessscore.append(clrscore)

    return complexscore, colourfulnessscore


if __name__ == "__main__":
    a, b = main()
    print(a)
    print(b)
