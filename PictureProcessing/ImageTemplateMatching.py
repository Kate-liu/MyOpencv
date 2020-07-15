# Template matching PICTURE OPERATION


import cv2
import matplotlib.pyplot as plt
import numpy as np

lena = cv2.imread('..\Data\lena.jpg', 0)
lenaTemplate = cv2.imread('..\Data\\face.jpg', 0)

height, weight = lenaTemplate.shape[:2]

print(lena.shape)
print(lenaTemplate.shape)
print(height)
print(weight)

# https://docs.opencv.org/3.3.1/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d
# - TM_SQDIFF：计算平方不同，计算出来的值越小，越相关
# - TM_CCORR：计算相关性，计算出来的值越大，越相关
# - TM_CCOEFF：计算相关系数，计算出来的值越大，越相关
# - TM_SQDIFF_NORMED：计算归一化平方不同，计算出来的值越接近0，越相关
# - TM_CCORR_NORMED：计算归一化相关性，计算出来的值越接近1，越相关
# - TM_CCOEFF_NORMED：计算归一化相关系数，计算出来的值越接近1，越相关
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# (image, templ, method, result=None, mask=None)
# If image is \f$W \times H\f$ and templ is \f$w \times h\f$ ,
# then result is \f$(W-w+1) \times (H-h+1)\f$ .
# 263 - 110 + 1 = 154
matchResult = cv2.matchTemplate(lena, lenaTemplate, cv2.TM_SQDIFF)
print(matchResult.shape)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(matchResult)
print(minVal)
print(maxVal)
print(minLoc)
print(maxLoc)

############################################# VS more methods #######################################

for methodString in methods:
    lenaImg = lena.copy()

    method = eval(methodString)
    print(method)
    print(methodString)

    matchRes = cv2.matchTemplate(lenaImg, lenaTemplate, method)

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(matchRes)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = minLoc
    else:
        top_left = maxLoc

    bottomRight = (top_left[0] + weight, top_left[1] + height)

    # draw
    cv2.rectangle(lenaImg, top_left, bottomRight, 255, 2)

    # show
    plt.subplot(121)
    plt.imshow(matchRes, cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122)
    plt.imshow(lenaImg, cmap='gray')
    plt.xticks([])
    plt.yticks([])

    plt.suptitle(methodString)
    plt.show()

############################################# match more object #######################################

colorMario = cv2.imread('../Data/mario.jpg')
grayMario = cv2.cvtColor(colorMario, cv2.COLOR_BGR2GRAY)

templateMario = cv2.imread('../Data/mario_coin.jpg', 0)

h, w = templateMario.shape[:2]

matchR = cv2.matchTemplate(grayMario, templateMario, cv2.TM_CCOEFF_NORMED)
threshold = 0.8

# threshold > 80%
location = np.where(matchR >= threshold)

for lo in zip(*location[:: -1]):
    bottom_right = (lo[0] + w, lo[1] + h)
    cv2.rectangle(colorMario, lo, bottom_right, (0, 0, 255), 2)

cv2.imshow('mario Image', colorMario)
cv2.waitKey(0)
cv2.destroyAllWindows()
