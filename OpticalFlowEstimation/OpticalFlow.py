# encoding: utf-8

import cv2
import numpy as np

# params
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7)
lk_params = dict(winSize=(15, 15), maxLevel=2)

# random color
color = np.random.randint(0, 255, (100, 3))

# read video
cap = cv2.VideoCapture("../Data/test.avi")

ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)  # gray

# Determines strong corners on an image.
# image, maxCorners, qualityLevel, minDistance, corners=None, mask=None, blockSize=None, useHarrisDetector=None, k=None
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# create mask
mask = np.zeros_like(old_frame)

while (True):
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # use optical flow
    # Calculates an optical flow for a sparse feature set using the iterative Lucas-Kanade method with  pyramids.
    # prevImg, nextImg, prevPts, nextPts, status=None, err=None, winSize=None,
    # maxLevel=None, criteria=None, flags=None, minEigThreshold=None
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # status == 1
    good_new = nextPts[status == 1]
    good_old = p0[status == 1]

    # draw line
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
        frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)

    img = cv2.add(frame, mask)

    cv2.imshow('frame', img)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

cap.release()
cv2.destroyAllWindows()
