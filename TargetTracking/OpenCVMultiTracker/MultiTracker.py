# encoding: utf-8

import argparse
import cv2

# Object Tracking Algorithms
# link: https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/
OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,
    "tld": cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,
    "mosse": cv2.TrackerMOSSE_create
}


def get_parameters():
    arg = argparse.ArgumentParser()
    arg.add_argument("-v", "--video", type=str, required=True, help="Input the video data path")
    arg.add_argument("-t", "--tracker", type=str, default="kcf", required=True, help="Input the tracker method")
    arguments = vars(arg.parse_args())
    return arguments


def get_MultiTracker():
    return cv2.MultiTracker_create()


def read_video(arguments):
    return cv2.VideoCapture(arguments.get("video") or arguments.get("v"))


def start_tracker(video, trackers, track_method):
    while True:
        frame = video.read()[1]
        if frame is None:
            break
        # resize
        h, w = frame.shape[:2]
        width = 600
        rate = width / float(w)
        dim = (width, int(h * rate))
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        # track roi
        # this is track preview frame and then use the current frame
        sucess, boxes = trackers.update(frame)
        # draw area
        for box in boxes:
            x, y, w, h = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # show
        cv2.imshow("frame", frame)
        key = cv2.waitKey(100) & 0xFF
        if key == ord("a"):  # press the keyboard `a`, then select roi area
            box = cv2.selectROI("frame", frame, fromCenter=False, showCrosshair=True)
            tracker = OPENCV_OBJECT_TRACKERS[track_method]()
            trackers.add(tracker, frame, box)
        elif key == 27:
            break
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # param
    # --video VideoData/soccer_01.mp4
    # --tracker kcf
    arguments = get_parameters()
    # get MultiTracker
    trackers = get_MultiTracker()
    # read video
    cap_video = read_video(arguments)
    # tracker
    start_tracker(cap_video, trackers, arguments.get("tracker") or arguments.get("t"))
