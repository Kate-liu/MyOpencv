# RESIZE PICTURE OPERATION


import cv2


def showImage(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(100000)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('..\Data\cat.jpg')

    cat = img[0:50, 0:200]

    showImage("resizeCat", cat)
