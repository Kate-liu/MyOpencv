# Fourier transform PICTURE OPERATION

import cv2
import numpy as np
import matplotlib.pyplot as plt

lena = cv2.imread('../Data/lena.jpg', 0)

lenaFloat32 = np.float32(lena)

# Performs a forward or inverse Discrete Fourier transform of a 1D or 2D floating-point array.
# the frequency 0, in the left top
lenaDft = cv2.dft(lenaFloat32, flags=cv2.DFT_COMPLEX_OUTPUT)

# shift frequency 0 to the middle
lenaShift = np.fft.fftshift(lenaDft)

# convert complex to the 0~255 value
# lenaShift is the double channel data
# Calculates the magnitude of 2D vectors.
lenaMagnitude = 20 * np.log(cv2.magnitude(lenaShift[:, :, 0], lenaShift[:, :, :1]))

plt.subplot(121), plt.imshow(lena, cmap='gray')
plt.title('lena image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(lenaMagnitude, cmap='gray')
plt.title('lana magnitude'), plt.xticks([]), plt.yticks([])
plt.show()


############################ low pass filter  ####################################
# 低通滤波器：只保留低频，会使得图像模糊
lena2 = cv2.imread('../Data/lena.jpg', 0)

lenaFloat322 = np.float32(lena2)

lenaDft2 = cv2.dft(lenaFloat322, flags=cv2.DFT_COMPLEX_OUTPUT)

lenaShift2 = np.fft.fftshift(lenaDft2)

# low filter
rows, cols = lena2.shape
middleRow, middleCol = int(rows / 2), int(cols / 2)  # middle point

# mask
mask = np.zeros((rows, cols, 2), np.uint8)
mask[middleRow - 30:middleRow + 30, middleCol - 30:middleCol + 30] = 1

# new image
newLenaShift = lenaShift2 * mask

# ifftshift
lenaIfftshift = np.fft.ifftshift(newLenaShift)

# idft
lenaIdft = cv2.idft(lenaIfftshift)

lenaMagnitude2 = cv2.magnitude(lenaIdft[:, :, 0], lenaIdft[:, :, :1])

plt.subplot(121), plt.imshow(lena, cmap='gray')
plt.title('lena image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(lenaMagnitude2, cmap='gray')
plt.title('lana magnitude'), plt.xticks([]), plt.yticks([])
plt.show()


############################ high pass filter  ####################################
# 高通滤波器：只保留高频，会使得图像细节增强
lena3 = cv2.imread('../Data/lena.jpg', 0)

lenaFloat323 = np.float32(lena3)

lenaDft3 = cv2.dft(lenaFloat323, flags=cv2.DFT_COMPLEX_OUTPUT)

lenaShift3 = np.fft.fftshift(lenaDft3)

# high filter
rows3, cols3 = lena3.shape
middleRow3, middleCol3 = int(rows3 / 2), int(cols3 / 2)  # middle point

# mask
mask3 = np.ones((rows3, cols3, 2), np.uint8)
mask3[middleRow3 - 30:middleRow3 + 30, middleCol3 - 30:middleCol3 + 30] = 0

# new image
newLenaShift3 = lenaShift3 * mask3

# ifftshift
lenaIfftshift3 = np.fft.ifftshift(newLenaShift3)

# idft
lenaIdft3 = cv2.idft(lenaIfftshift3)

lenaMagnitude3 = cv2.magnitude(lenaIdft3[:, :, 0], lenaIdft3[:, :, :1])

plt.subplot(121), plt.imshow(lena, cmap='gray')
plt.title('lena image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(lenaMagnitude3, cmap='gray')
plt.title('lana magnitude'), plt.xticks([]), plt.yticks([])
plt.show()
