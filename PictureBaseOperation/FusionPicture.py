# Fusion PICTURE OPERATION

import cv2
import matplotlib.pyplot as plt


# create function show picture
def showImage(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()


# read image
cat = cv2.imread("../Data/cat.jpg")
dog = cv2.imread("../Data/dog.jpg")

# Error
# picture dimension difference
# catAddDog = cat + dog
# print(catAddDog[:5, :, 0])
# print("\n")

# check shape
print("cat:")
print(cat.shape)
print("dog:")
print(dog.shape)

# resize
resizeDog = cv2.resize(dog, (500, 414))

print("new dog:")
print(resizeDog.shape)

showImage("resizeDog", resizeDog)

# Fusion picture
# addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)
# function: dst = src1*alpha + src2*beta + gamma;
newPicture = cv2.addWeighted(cat, 0.3, resizeDog, 0.7, 0)

plt.imshow(newPicture, 'gray'), plt.title('newPicture')
plt.show()


# try cv2 show
# def showImage(winname, mat):
#     cv2.imshow(winname, mat)
#     cv2.waitKey(100000)
#     cv2.destroyAllWindows()
#
#
# showImage("cv2Show", newPicture)
