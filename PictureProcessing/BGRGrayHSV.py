# REVIEW PICTURE OPERATION

import cv2


def showImage(Winname, mat):
    cv2.imshow(Winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # BGR
    catImg = cv2.imread('..\Data\cat.jpg')
    print(catImg.shape)
    showImage('BGR', catImg)

    # GRAY
    grayImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2GRAY)
    print(grayImg.shape)
    showImage('GRAY', grayImg)

    # HSV
    hsvImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2HSV)
    print(hsvImg.shape)
    showImage("HSV", hsvImg)
