# Contour PICTURE OPERATION

import cv2


def showImg(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


######################################## 轮廓绘制 #######################################

# color
colorCounter = cv2.imread('..\Data\contours.png')
# gray
grayCounter = cv2.cvtColor(colorCounter, cv2.COLOR_BGR2GRAY)
showImg('gray', grayCounter)

# use binary picture, improve precision
ret, thresh = cv2.threshold(grayCounter, 127, 255, cv2.THRESH_BINARY)
showImg('threshold', thresh)

# Finds contours in a binary image. (image, mode, method)
# mode:轮廓检索模式
# - RETR_EXTERNAL ：只检索最外面的轮廓；
# - RETR_LIST：检索所有的轮廓，并将其保存到一条链表当中；
# - RETR_CCOMP：检索所有的轮廓，并将他们组织为两层：顶层是各部分的外部边界，第二层是空洞的边界;
# - RETR_TREE：检索所有的轮廓，并重构嵌套轮廓的整个层次;(常用)
# method:轮廓逼近方法
# - CHAIN_APPROX_NONE：以Freeman链码的方式输出轮廓，所有其他方法输出多边形（顶点的序列）。
# - CHAIN_APPROX_SIMPLE:压缩水平的、垂直的和斜的部分，也就是，函数只保留他们的终点部分。
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# draw contour
# need use copy, get another image, otherwise the original picture will be change.
# image, contours, contourIdx, color, thickness=None
# contourIdx: -1:all, 0, 1, 2 ...
# color: (0,0,255): BGR -> red
# thickness：the line weight
drawImg = colorCounter.copy()
drawResult = cv2.drawContours(drawImg, contours, -1, (0, 0, 255), 2)
showImg('Draw Img', drawResult)
showImg('color', colorCounter)

# Don't copy, then change original picture
drawResult = cv2.drawContours(colorCounter, contours, -1, (0, 0, 255), 2)
showImg('Draw Img', drawResult)
showImg('color', colorCounter)

######################################## 轮廓特征 #######################################

# get one counter
# the list data
con = contours[0]

# calculate area
print('area')
print(cv2.contourArea(con))

# calculate length
# True: closed
print('length')
print(cv2.arcLength(con, True))

######################################### 轮廓近似 ######################################

# color
colorCounter2 = cv2.imread('..\Data\contours2.png')
# gray
grayCounter2 = cv2.cvtColor(colorCounter2, cv2.COLOR_BGR2GRAY)
showImg('gray2', grayCounter2)

# use binary picture, improve precision
ret2, thresh2 = cv2.threshold(grayCounter2, 127, 255, cv2.THRESH_BINARY)
showImg('threshold2', thresh2)

contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# get one contour
con2 = contours2[0]

# draw one contour
drawImg2 = colorCounter2.copy()
drawResult2 = cv2.drawContours(drawImg2, [con2], -1, (0, 0, 255), 2)
showImg('Draw Img', drawResult2)
showImg('color', colorCounter2)

# approx Counter
# change 0.01, 0.1, 0.15, 0.2
epsilon = 0.01 * cv2.arcLength(con2, True)
# epsilon Parameter specifying the approximation accuracy. This is the maximum distance
# between the original curve and its approximation.
approx = cv2.approxPolyDP(con2, epsilon, True)

drawImg3 = colorCounter2.copy()
drawResult3 = cv2.drawContours(drawImg3, [approx], -1, (0, 0, 255), 2)
showImg('Draw Img', drawResult3)
showImg('color', colorCounter2)

############################################# 边界矩阵 #######################################

# color
colorCounter3 = cv2.imread('..\Data\contours.png')
# gray
grayCounter3 = cv2.cvtColor(colorCounter3, cv2.COLOR_BGR2GRAY)
showImg('gray2', grayCounter3)

# use binary picture, improve precision
ret3, thresh3 = cv2.threshold(grayCounter3, 127, 255, cv2.THRESH_BINARY)
showImg('threshold3', thresh3)

contours3, hierarchy3 = cv2.findContours(thresh3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# get one contour
con3 = contours3[0]

# Calculates the up-right bounding rectangle of a point set or non-zero pixels of gray-scale image.
# x：point
# y: point
# w: to right length
# h: to button length
x, y, w, h = cv2.boundingRect(con3)
# img, pt1, pt2, color, thickness=None,
# Draws a simple, thick, or filled up-right rectangle.
drawImg4 = colorCounter3.copy()
rectImg = cv2.rectangle(drawImg4, (x, y), (x + w, y + h), (0, 255, 0), 2)
showImg('rectangle image', rectImg)

# Calculates a contour area.
area = cv2.contourArea(con3)
# Calculates a chose contour area.
rectArea = w * h
extent = float(area) / rectArea
print("The counter / counter rectangle = ", extent)

############################################# 外接圆 #######################################

(x, y), radius = cv2.minEnclosingCircle(con3)

center = (int(x), int(y))
radius = int(radius)

drawImg5 = colorCounter3.copy()
radiusImage = cv2.circle(drawImg5, center, radius, (0, 255, 0), 2)
showImg("radius Image", radiusImage)
