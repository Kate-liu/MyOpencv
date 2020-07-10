# RESIZE PICTURE OPERATION


import cv2


def showImage(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(100000)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('..\Data\cat.jpg')

    cat = img[0:50, 0:200]
    # showImage("resizeCat", cat)

    # resize method
    newCat1 = cv2.resize(img, (0, 0), fx=1, fy=1)
    showImage("newCat", newCat1)

    newCat2 = cv2.resize(img, (0, 0), fx=2, fy=2)
    showImage("newCat", newCat2)

    newCat3 = cv2.resize(img, (500, 500))
    showImage("newCat", newCat3)
