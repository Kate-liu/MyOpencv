# Histogram EQUALIZATION PICTURE OPERATION

import cv2
import matplotlib.pyplot as plt
import numpy as np


def showImg(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


statue = cv2.imread('../Data/clahe.jpg', 0)

plt.hist(statue.ravel(), 256)
plt.show()

# The function equalizes the histogram of the input image using the following algorithm:
# - Calculate the histogram \f$H\f$ for src .
# - Normalize the histogram so that the sum of histogram bins is 255.
# - Compute the integral of the histogram:
# \f[H'_i =  \sum _{0  \le j < i} H(j)\f]
# - Transform the image using \f$H'\f$ as a look-up table: \f$\texttt{dst}(x,y) = H'(\texttt{src}(x,y))\f$
# The algorithm normalizes the brightness and increases the contrast of the image.
statueEqu = cv2.equalizeHist(statue)
plt.hist(statueEqu.ravel(), 256)
plt.show()

allHist = np.hstack((statue, statueEqu))
showImg('all hist', allHist)

# Creates a smart pointer to a cv::CLAHE class and initializes it.
# Adaptive histogram equalization
calhe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
resultStatue = calhe.apply(statue)

calheHist = np.hstack((statue, statueEqu, resultStatue))
showImg('all hist', calheHist)
