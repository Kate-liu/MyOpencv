# Channel PICTURE OPERATION

import cv2


def showImage(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


# split
cat = cv2.imread('..\Data\cat.jpg')

red, green, blue = cv2.split(cat)

print(red)
print(green)
print(blue)

print(red.shape)
print(green.shape)
print(blue.shape)

# merge
mergeCat = cv2.merge((red, green, blue))
print(mergeCat.shape)

# just save red channel
# cv2 read picture is not RGB format, is BGR format
showRedCat = cat.copy()
showRedCat[:, :, 0] = 0
showRedCat[:, :, 1] = 0
showImage("showRedCat", showRedCat)

# just save green channel
showGreenCat = cat.copy()
showGreenCat[:, :, 0] = 0
showGreenCat[:, :, 2] = 0
showImage("showGreenCat", showGreenCat)

# just save blue channel
# cv2 read picture is not RGB format, is BGR format
showBlueCat = cat.copy()
showBlueCat[:, :, 1] = 0
showBlueCat[:, :, 2] = 0
showImage("showBlueCat", showBlueCat)
