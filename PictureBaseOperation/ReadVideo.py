# READ VIDEO OPERATION


import cv2

vc = cv2.VideoCapture('..\Data\\test.mp4')

# check video data
if vc.isOpened():
    canOpen, frame = vc.read()
else:
    canOpen = False

# open video
while canOpen:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        grayPicture = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('OpenVideo', grayPicture)

        if cv2.waitKey(100) & 0xFF == 27:
            break

vc.release()
cv2.destroyAllWindows()







