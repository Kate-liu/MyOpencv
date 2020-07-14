# Pyramid PICTURE OPERATION

import cv2
import numpy as np


def showImg(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# original
AM = cv2.imread('..\Data\AM.png')

print('original')
print(AM.shape)
showImg('AM', AM)

# Gaussian Pyramid up
upAM = cv2.pyrUp(AM)
print('Gaussian Pyramid up')
print(upAM.shape)
showImg('upAM', upAM)

upAM2 = cv2.pyrUp(upAM)
print('Gaussian Pyramid up 2')
print(upAM2.shape)
showImg('upAM2', upAM2)

# Gaussian Pyramid down
downAM = cv2.pyrDown(AM)
print('Gaussian Pyramid down')
print(downAM.shape)
showImg('downAM', downAM)

downAM2 = cv2.pyrDown(downAM)
print('Gaussian Pyramid down 2')
print(downAM2.shape)
showImg('downAM2', downAM2)

# compare original picture and (first up, then down)
upAMCompare = cv2.pyrUp(AM)
downAMCompare = cv2.pyrDown(upAMCompare)

compareAM = np.hstack((AM, downAMCompare))
print('Compare AM')
print(AM.shape)
print(downAMCompare.shape)
showImg('Compare AM', compareAM)


####################################### Laplacian Pyramid ################################
# Laplacian Pyramid
downAMLaplacian = cv2.pyrDown(AM)
upDownAMLaplacian = cv2.pyrUp(downAMLaplacian)

showLaplacianPyramid = AM - upDownAMLaplacian
showImg('show Laplacian Pyramid', showLaplacianPyramid)

# Compare Laplacian (original - up(down(original)))
# use (original - down(up(original)))
upAMCompare = cv2.pyrUp(AM)
downAMCompare = cv2.pyrDown(upAMCompare)

compareLaplacian = AM - downAMCompare
showImg('show Compare Laplacian Laplacian Pyramid', compareLaplacian)

compareResult = np.hstack((AM, showLaplacianPyramid, compareLaplacian))
showImg('show Compare result', compareResult)
