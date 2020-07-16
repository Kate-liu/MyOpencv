# Histogram PICTURE OPERATION

import cv2
import matplotlib.pyplot as plt
import numpy as np


def showImg(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


############################ matplotlib show gray hist ####################################
cat = cv2.imread('../Data/cat.jpg', 0)

# calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) -> hist
# - images: 原图像图像格式为 uint8 或 ﬂoat32。当传入函数时应 用中括号 [] 括来例如[img]
# - channels: 同样用中括号括来它会告函数我们统幅图 像的直方图。如果入图像是灰度图它的值就是 [0]如果是彩色图像 的传入的参数可以是 [0][1][2] 它们分别对应着 BGR。
# - mask: 掩模图像。统整幅图像的直方图就把它为 None。但是如 果你想统图像某一分的直方图的你就制作一个掩模图像并 使用它。
# - histSize:BIN 的数目。也应用中括号括来
# - ranges: 像素值范围常为 [0, 256]
histCat = cv2.calcHist([cat], [0], None, [256], [0, 256])

print(cat.shape)
print(histCat.shape)
# plt show hist
plt.hist(cat.ravel(), 256)
plt.show()

############################ cv2 show color hist ####################################
colorCat = cv2.imread('../Data/cat.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histCol = cv2.calcHist([colorCat], [i], None, [256], [0, 256])

    plt.plot(histCol, color=col)
    plt.xlim([0, 256])

plt.show()

############################ use mask ####################################
colorCat = cv2.imread('../Data/cat.jpg')

mask = np.zeros(colorCat.shape[:2], np.uint8)
print(mask.shape)

mask[100:300, 100:400] = 255
showImg('mask', mask)

showImg('cat', cat)

# computes bitwise conjunction of the two arrays (dst = src1 & src2)
maskedCat = cv2.bitwise_and(cat, cat, mask=mask)
showImg('maskedCat', maskedCat)

histFull = cv2.calcHist([cat], [0], None, [256], [0, 256])
histMask = cv2.calcHist([cat], [0], mask, [256], [0, 256])  # use mask

# show all result
plt.subplot(221), plt.imshow(cat, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(maskedCat, 'gray')
plt.subplot(224), plt.plot(histFull), plt.plot(histMask)

plt.xlim([0, 266])
plt.show()
