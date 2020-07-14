# Scharr And Laplacian PICTURE OPERATION


import cv2
import numpy as np


def showImg(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


lena = cv2.imread('..\Data\lena.jpg', cv2.IMREAD_GRAYSCALE)

# review Sobel
sobelXLena = cv2.Sobel(lena, cv2.CV_64F, 1, 0, ksize=3)
sobelYLena = cv2.Sobel(lena, cv2.CV_64F, 0, 1, ksize=3)

sobelXLenaAbs = cv2.convertScaleAbs(sobelXLena)
sobelYLenaAbs = cv2.convertScaleAbs(sobelYLena)

sobelXYLena = cv2.addWeighted(sobelXLenaAbs, 0.5, sobelYLenaAbs, 0.5, 0)
showImg('sobelXYLena', sobelXYLena)

# Scharr
# {-3}{0}{3}{-10}{0}{10}{-3}{0}{3}
scharrX = cv2.Scharr(lena, cv2.CV_64F, 1, 0)
scharrY = cv2.Scharr(lena, cv2.CV_64F, 0, 1)
scharrXAbs = cv2.convertScaleAbs(scharrX)
scharrYAbs = cv2.convertScaleAbs(scharrY)
scharrXY = cv2.addWeighted(scharrXAbs, 0.5, scharrYAbs, 0.5, 0)

showImg('scharrXY', scharrXY)


# Laplacian
# {0}{1}{0}{1}{-4}{1}{0}{1}{0}
laplacian = cv2.Laplacian(lena, cv2.CV_64F)
laplacianAbs = cv2.convertScaleAbs(laplacian)

showImg('laplacianAbs', laplacianAbs)


# show all image
allGradient = np.hstack((lena, sobelXYLena, scharrXY, laplacianAbs))
showImg('allGradient', allGradient)
