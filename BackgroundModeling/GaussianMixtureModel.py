# encoding: utf-8

import cv2

# read video
cap = cv2.VideoCapture('../Data/test.avi')

# Returns a structuring element of the specified size and shape for morphological operations.
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# create MOG2
background = cv2.createBackgroundSubtractorMOG2()

while (True):
    ret, frame = cap.read()
    background_mask = background.apply(frame)

    # use morphology: MORPH_OPEN
    background_mask = cv2.morphologyEx(background_mask, cv2.MORPH_OPEN, kernel)

    # find contours
    contours, hierarchy = cv2.findContours(background_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # calculation length
        perimeter = cv2.arcLength(c, True)
        if perimeter > 188:  # length big is people
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),
                          2)  # Draws a simple, thick, or filled up-right rectangle.

    # show frame
    cv2.imshow('frame', frame)
    cv2.imshow('background_mask', background_mask)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
