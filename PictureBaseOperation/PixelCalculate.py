# Calculate PICTURE OPERATION

import cv2

# read image
cat = cv2.imread("../Data/cat.jpg")
dog = cv2.imread("../Data/dog.jpg")

# all pixel add value
# why is 0? RGB(GBR)
newCat = cat + 10

print(cat[:5, :, 0])
print("\n")
print(newCat[:5, :, 0])
print("\n")

# overflow add picture used in uint8
# uint8 is 0 - 255, 256 values
overflowCat = cat + newCat

print(overflowCat[:5, :, 0])
print("\n")

# add function method
# overflow 255, used 255
addMethodCat = cv2.add(cat, newCat)

print(addMethodCat[:5, :, 0])
print("\n")




