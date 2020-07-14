# Canny Edge detection PICTURE OPERATION

import cv2
import numpy as np


def showImg(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


lena = cv2.imread('..\Data\lena.jpg', cv2.IMREAD_GRAYSCALE)

# http://en.wikipedia.org/wiki/Canny_edge_detector
# Double-Threshold: threshold1, threshold2
canny1 = cv2.Canny(lena, 50, 150)
canny2 = cv2.Canny(lena, 80, 150)

allCanny = np.hstack((lena, canny1, canny2))
showImg('Canny', allCanny)


# Use car example
car = cv2.imread('..\Data\car.png', cv2.IMREAD_GRAYSCALE)
car1 = cv2.Canny(car, 50, 150)
car2 = cv2.Canny(car, 50, 250)

allCar = np.hstack((car1, car2))
showImg('allCar', allCar)
