# Harris algorithm

import cv2
import numpy as np

img = cv2.imread('../Data/chessboard.jpg')
# img = cv2.imread('../Data/test_1.jpg')
cv2.imshow('img', img)
print("img.shape", img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)

# src: need float32 value, Input single-channel 8-bit or floating-point image.
# blockSize: check corner area size
# ksize: sobel ksize, used in the window size
# k: often used in the [0.04, 0.06]
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
print("dst.shape", dst.shape)

# corner point compare method
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
