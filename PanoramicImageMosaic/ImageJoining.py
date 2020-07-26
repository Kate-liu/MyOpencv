# -*- coding:utf-8 -*-
import cv2
from Joiner import Joiner

if __name__ == '__main__':
    image1 = cv2.imread("./Data/right_01.png")  # need right picture
    image2 = cv2.imread("./Data/left_01.png")  # need left picture

    # get joiner
    joiner = Joiner()
    (result, draw_image) = joiner.join([image1, image2], showMatches=True)

    cv2.imshow("image1", image1)
    cv2.imshow("image2", image2)
    cv2.imshow("draw maeches", draw_image)
    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
