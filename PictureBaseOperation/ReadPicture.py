# READ PICTURE OPERATION


import cv2

############################ color ###############################################

# read color picture
# IMREAD_COLOR = 1
img = cv2.imread('..\Data\cat.jpg')

# print one picture
print(img)

# show one picture
cv2.imshow("catImage", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()


# create function show picture
def showImage(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


showImage("newCatImage", img)

# show format: height weight mat
print(img.shape)

################################ gray #############################################
# read gray picture
# IMREAD_GRAYSCALE = 0
grayImg = cv2.imread('..\Data\cat.jpg', cv2.IMREAD_GRAYSCALE)

print(grayImg)
showImage("grayImage", grayImg)

# show format: height weight
print(grayImg.shape)

################################# detail #############################################

# show data format : numpy.ndarray
print(type(img))
print(type(grayImg))

# show all pixel number: height * weight
print(img.size)
print(grayImg.size)

# show dtype: uint8, value:0-255
print(img.dtype)
print(grayImg.dtype)


################################# write #############################################

cv2.imwrite('newcat.jpg', img)
cv2.imwrite('newGrayCat.jpg', grayImg)

