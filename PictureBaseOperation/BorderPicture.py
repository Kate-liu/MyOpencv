# Border PICTURE OPERATION


import cv2
import matplotlib.pyplot as plt

# read image
img = cv2.imread("../Data/cat.jpg")

topSize, bottomSize, leftSize, rightSize = (100, 100, 100, 100)

# copy edge  pixel
replicate = cv2.copyMakeBorder(img, topSize, bottomSize, leftSize, rightSize, borderType=cv2.BORDER_REPLICATE)
# eg: fedcba|abcdefgh|hgfedcb
reflect = cv2.copyMakeBorder(img, topSize, bottomSize, leftSize, rightSize, borderType=cv2.BORDER_REFLECT)
# eg: gfedcb|abcdefgh|gfedcba
reflect101 = cv2.copyMakeBorder(img, topSize, bottomSize, leftSize, rightSize, borderType=cv2.BORDER_REFLECT_101)
# eg: cdefgh|abcdefgh|abcdefg
wrap = cv2.copyMakeBorder(img, topSize, bottomSize, leftSize, rightSize, borderType=cv2.BORDER_WRAP)
# padding value
constant = cv2.copyMakeBorder(img, topSize, bottomSize, leftSize, rightSize, borderType=cv2.BORDER_CONSTANT, value=0)

# Single show
plt.subplot(231), plt.imshow(img, 'gray'), plt.title('Original')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('Original')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('Original')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('Original')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('Original')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('Original')

plt.show()


# Multi show
# plt.imshow(img, 'gray'), plt.title('Original')
# plt.show()
# plt.imshow(replicate, 'gray'), plt.title('Original')
# plt.show()
# plt.imshow(reflect, 'gray'), plt.title('Original')
# plt.show()
# plt.imshow(reflect101, 'gray'), plt.title('Original')
# plt.show()
# plt.imshow(wrap, 'gray'), plt.title('Original')
# plt.show()
# plt.imshow(constant, 'gray'), plt.title('Original')
# plt.show()


# compare cv2 and matplotlib show picture
# cv2 is read BGR
# matplotlib is show RGB

# create function show picture
# def showImage(winname, mat):
#     cv2.imshow(winname, mat)
#     cv2.waitKey(100000)
#     cv2.destroyAllWindows()
#
#
# showImage("cv2Show", img)
#
# plt.imshow(img, 'gray'), plt.title('Original')
# plt.show()
