# Morphology PICTURE OPERATION


import cv2
import numpy as np


def showImg(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


########################################## original #################################################
img = cv2.imread('..\Data\dige.png')
showImg('dige', img)

########################################## erode #################################################
kernel = np.ones((3, 3), np.uint8)
erode = cv2.erode(img, kernel, iterations=2)
showImg('erode', erode)

########################################## erode pie #################################################
pie = cv2.imread('..\Data\pie.png')
showImg('pie', pie)

kernelPie = np.ones((30, 30), np.uint8)
erode1 = cv2.erode(pie, kernelPie, iterations=1)
erode2 = cv2.erode(pie, kernelPie, iterations=2)
erode3 = cv2.erode(pie, kernelPie, iterations=3)

allErodePie = np.hstack((erode1, erode2, erode3))
showImg('allErodePie', allErodePie)

########################################## dilate #################################################
kernel = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(img, kernel, iterations=2)
showImg('dilate', dilate)

########################################## dilate pie #################################################
kernelPie = np.ones((30, 30), np.uint8)
dilate1 = cv2.dilate(pie, kernelPie, iterations=1)
dilate2 = cv2.dilate(pie, kernelPie, iterations=2)
dilate3 = cv2.dilate(pie, kernelPie, iterations=3)

allDilatePie = np.hstack((dilate1, dilate2, dilate3))
showImg('allDilatePie', allDilatePie)

########################################## erode and dilate #################################################
# use this reduce small line
kernel = np.ones((3, 3), np.uint8)
erode = cv2.erode(img, kernel, iterations=1)
showImg('erode', erode)

dilate = cv2.dilate(erode, kernel, iterations=1)
showImg('dilate', dilate)

########################################## morphologyEx:open and close #################################################
# MORPH_OPEN：first erode then dilate
# MORPH_CLOSE：first dilate then erode
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
showImg('opening', opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
showImg('closing', closing)

########################################## morphologyEx: gradient #################################################
# MORPH_GRADIENT: dilate - erode
kernel = np.ones((7, 7), np.uint8)

dilatePie = cv2.dilate(pie, kernel, iterations=5)
erodePie = cv2.erode(pie, kernel, iterations=5)
dilateErode = np.hstack((dilatePie, erodePie))
showImg('dilateErode', dilateErode)

gradient = cv2.morphologyEx(pie, cv2.MORPH_GRADIENT, kernel)
showImg('gradient', gradient)

########################################## morphologyEx: gradient #################################################
# MORPH_TOPHAT: img -  open
# MORPH_BLACKHAT: close - img
kernel = np.ones((3, 3), np.uint8)

topHat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackHat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
showImg('topHat', topHat)
showImg('blackHat', blackHat)
