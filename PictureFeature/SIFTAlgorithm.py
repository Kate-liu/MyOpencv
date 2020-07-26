# SIFT algorithm

import cv2
import numpy as np

img = cv2.imread('../Data/test_1.jpg')
# img = cv2.imread('../Data/lena.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# opencv version
# recommend: version 3.4.1.15
# pip install opencv-python==3.4.1.15
# pip install opencv-contrib-python==3.4.1.15
# but, used 4.3.0.36 is not error
print(cv2.__version__)

# get class
sift = cv2.xfeatures2d.SIFT_create()

# get key point
kp = sift.detect(gray, None)

# draw
img = cv2.drawKeypoints(gray, kp, img)

# cv2 show image
cv2.imshow('Keypoints', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# calculate key point
kp, des = sift.compute(gray, kp)

print(np.array(kp).shape)  # kp is a KeyPoint List
print(des.shape)
print(des[0])  # 128 dimensionality
