import cv2 as cv
import sys
import numpy as np


def convolution(matrix, mask):
    _kernelIndex = len(mask) * len(mask[0])
    halfIndexSize = int(len(mask) / 2)
    _kernerlIndex = tuple([(x, y) for x in range(-halfIndexSize, halfIndexSize + 1, 1) for y in
                           range(- halfIndexSize, halfIndexSize + 1, 1)])
    row = len(matrix)
    col = len(matrix[0])
    result = []
    for i in range(0, row):
        for j in range(0, col):
            temp = 0
            for u in range(0, 9):
                rIndex = 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def opening(imgurl):
    img = cv.imread(imgurl, cv.IMREAD_UNCHANGED)
    if img is None:
        sys.exit("Could not read image")
    kernel = np.ones((3, 3), np.uint8)
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    cv.imshow("out", opening)
    cv.waitKey(0)


if __name__ == '__main__':
    opening("./images/binary.jpg")
