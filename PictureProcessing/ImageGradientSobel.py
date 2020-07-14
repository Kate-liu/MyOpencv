# Sobel PICTURE OPERATION

import cv2


def showImg(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pie = cv2.imread('..\Data\pie.png', cv2.IMREAD_GRAYSCALE)
showImg('pie', pie)

# Sobel
#  Most often, the function is called with ( xorder = 1, yorder = 0, ksize = 3)
# or ( xorder = 0, yorder = 1, ksize = 3) to calculate the first x- or y- image derivative.
# sobelX：right pixel - left pixel, so It can be cut off 0-255, need used CV_64F
sobelX = cv2.Sobel(pie, cv2.CV_64F, 1, 0, ksize=3)
showImg('sobelX', sobelX)

# used convertScaleAbs CAL sobelX
sobelX = cv2.Sobel(pie, cv2.CV_64F, 1, 0, ksize=3)
sobelXAbs = cv2.convertScaleAbs(sobelX)
showImg('sobelXAbs', sobelXAbs)

# sobelY
sobelY = cv2.Sobel(pie, cv2.CV_64F, 0, 1, ksize=3)
sobelYAbs = cv2.convertScaleAbs(sobelY)
showImg('sobelYAbs', sobelYAbs)

# sobelX add sobelY
sobelXY = cv2.addWeighted(sobelXAbs, 0.5, sobelYAbs, 0.5, 0)
showImg('sobelXY', sobelXY)

# VS dx1 dy=1 sobel
# This is can be find some point, discontinuity
VSsobelXY = cv2.Sobel(pie, cv2.CV_64F, 1, 1, ksize=3)
showImg('VSsobelXY', VSsobelXY)

# Some other example of lena
# use first x-, then y-
lena = cv2.imread('..\Data\lena.jpg', cv2.IMREAD_GRAYSCALE)
showImg('lena', lena)

sobelXLena = cv2.Sobel(lena, cv2.CV_64F, 1, 0, ksize=3)
sobelXLenaAbs = cv2.convertScaleAbs(sobelXLena)
showImg('sobelXLena', sobelXLena)

sobelYLena = cv2.Sobel(lena, cv2.CV_64F, 0, 1, ksize=3)
sobelYLenaAbs = cv2.convertScaleAbs(sobelYLena)
showImg('sobelYLena', sobelYLena)

sobelXYLena = cv2.addWeighted(sobelXLenaAbs, 0.5, sobelYLenaAbs, 0.5, 0)
showImg('sobelXYLena', sobelXYLena)

# use x- and y-
VSsobelXYLena = cv2.Sobel(lena, cv2.CV_64F, 1, 1, ksize=3)
showImg('VSsobelXYLena', VSsobelXYLena)
