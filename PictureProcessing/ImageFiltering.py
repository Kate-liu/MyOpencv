# FILTERING PICTURE OPERATION


import cv2
import numpy as np


def showImg(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# lena
img = cv2.imread('..\Data\lena.jpg')
showImg('lena', img)

# lena noise
noiseImg = cv2.imread('..\Data\lenaNoise.png')
showImg('lena', noiseImg)

########################################## blur #################################################
# mean filtering
# \f[\texttt{K} =  \frac{1}{\texttt{ksize.width*ksize.height}} \begin{bmatrix} 1 & 1 & 1 &
# \cdots & 1 & 1  \\ 1 & 1 & 1 &  \cdots & 1 & 1  \\ \hdotsfor{6} \\ 1 & 1 & 1 &  \cdots & 1 & 1
# \\ \end{bmatrix}\f]
blur = cv2.blur(noiseImg, (3, 3))
showImg('mean filtering', blur)

########################################## boxFilter ##############################################
# box filtering
# chose normalize true == mean filtering
box = cv2.boxFilter(noiseImg, -1, (3, 3), normalize=True)
showImg('box filtering', box)

# chose normalize false != mean filtering
# overflow 255
boxOverflow = cv2.boxFilter(noiseImg, -1, (3, 3), normalize=False)
showImg('boxOverflow filtering', boxOverflow)

########################################## GaussianBlur ##############################################
# gaussianBlur filtering
# sorted the 5 * 5 data value, chose the middle value
gaussianBlur = cv2.GaussianBlur(noiseImg, (5, 5), 1)
showImg("gaussianBlur filtering", gaussianBlur)

########################################## medianBlur ##############################################
# medianBlur filtering
medianBlur = cv2.medianBlur(noiseImg, 5)
showImg("medianBlur filtering", medianBlur)

########################################## Show all filtering ##############################################
# use numpy show all filtering picture data
# Use hstack or vstack
allImg = np.hstack((blur, box, gaussianBlur, medianBlur))
print(allImg)
showImg('All filter picture', allImg)
