# encoding: utf-8
import argparse
import time
from collections import OrderedDict
import dlib
import cv2
import numpy as np
from scipy.spatial import distance as dist

FACIAL_LANDMARKS_68_IDXS = OrderedDict([
    ("mouth", (48, 68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 36)),
    ("jaw", (0, 17))
])
# 分别取两个眼睛区域
(lStart, lEnd) = FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = FACIAL_LANDMARKS_68_IDXS["right_eye"]

# 设置判断参数m
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3


def get_parameters():
    """
    warning: if arguments use `-`, It can be default change to `_`.
    source code: dest = dest.replace('-', '_')
    :return:
    """
    arg = argparse.ArgumentParser()
    arg.add_argument("-p", "--shape_predictor", required=True, help="Input the shape predictor data path")
    arg.add_argument("-v", "--video", type=str, default='', help="Input the video data path")
    arguments = vars(arg.parse_args())
    return arguments


def get_face_handler(arguments):
    detector = dlib.get_frontal_face_detector()
    arg = arguments.get("shape_predictor")
    predictor = dlib.shape_predictor(arg)
    return detector, predictor


def shape_to_np(shape, dtype="int"):
    # 创建68*2
    coords = np.zeros((shape.num_parts, 2), dtype=dtype)
    # 遍历每一个关键点
    # 得到坐标
    for i in range(0, shape.num_parts):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords


def self_resize(img, new_width):
    (h, w) = img.shape[:2]
    ratio = new_width / float(w)
    dim = (new_width, int(h * ratio))
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return img


def eye_aspect_ratio(eye):
    # 计算距离，竖直的
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    # 计算距离，水平的
    C = dist.euclidean(eye[0], eye[3])
    # ear值
    ear = (A + B) / (2.0 * C)
    return ear


def get_video(arguments):
    # parameter
    counter = 0
    total = 0
    # video capture
    cap = cv2.VideoCapture(arguments.get("video") or arguments.get("v"))
    time.sleep(1.0)

    while True:
        frame = cap.read()[1]
        if frame is None:
            break

        frame = self_resize(frame, 1200)  # resize
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # gray

        # get face
        rects = detector(gray_img, 0)

        for (i, rect) in enumerate(rects):
            # get face point
            shapes = predictor(gray_img, rect)
            shapes = shape_to_np(shapes)  # convert

            leftEye = shapes[lStart:lEnd]
            rightEye = shapes[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)  # algorithm
            rightEAR = eye_aspect_ratio(rightEye)

            ear = (leftEAR + rightEAR) / 2.0  # average

            # draw eyes area
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            if ear < EYE_AR_THRESH:
                counter += 1
            else:
                if counter >= EYE_AR_CONSEC_FRAMES:
                    total += 1
                counter = 0
            cv2.putText(frame, "Blinks: {}".format(total), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        # show
        cv2.imshow("frame", frame)
        key = cv2.waitKey(10) & 0xFF
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # parameters
    # --shape_predictor ../Data/shape_predictor_68_face_landmarks.dat
    # --video ../Data/test.mp4
    arguments = get_parameters()
    # get face key point handler
    detector, predictor = get_face_handler(arguments)
    # get video and Fatigue Monitoring
    get_video(arguments)
