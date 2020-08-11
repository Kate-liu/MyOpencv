# encoding: utf-8

import argparse
import dlib
import cv2
import numpy as np
import multiprocessing
from TargetTracking.MobileNetSSDMultiTracker.Utils import FPS

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]


def get_parameters():
    arg = argparse.ArgumentParser()
    arg.add_argument("-p", "--prototxt", type=str, required=True, help="Input the caffe protoxt path")
    arg.add_argument("-m", "--model", type=str, required=True, help="Input the caffe model path")
    arg.add_argument("-v", "--video", type=str, required=True, help="Input the video data path")
    arg.add_argument("-o", "--output", type=str, help="Input the output video data path")
    arg.add_argument("-c", "--confidence", type=float, default=0.2,
                     help="minimum probability to filter weak detections")
    arguments = vars(arg.parse_args())
    return arguments


def load_caffe_model(arguments):
    print("Start load caffe model")
    return cv2.dnn.readNetFromCaffe(arguments.get("prototxt") or arguments.get("p"),
                                    arguments.get("model") or arguments.get("m"))


def read_video(arguments):
    return cv2.VideoCapture(arguments.get("video") or arguments.get("v"))


def start_process_tracker(boxXY, label, frame_rgb, in_queue, out_queue):
    # use dlib
    # dlib.correlation_tracker: http://dlib.net/python/index.html#dlib.correlation_tracker
    track = dlib.correlation_tracker()
    rectangle = dlib.rectangle(int(boxXY[0]), int(boxXY[1]), int(boxXY[2]), int(boxXY[3]))
    track.start_track(frame_rgb, rectangle)

    while True:
        frame_rgb = in_queue.get()
        if frame_rgb is not None:
            # update
            track.update(frame_rgb)
            position = track.get_position()
            # get point
            startX = int(position.left())
            startY = int(position.top())
            endX = int(position.right())
            endY = int(position.bottom())
            out_queue.put((label, (startX, startY, endX, endY)))


def tracker_object(cap_video, arguments, net, fps):
    writer = None
    input_queues = []
    output_queues = []
    while True:
        frame = cap_video.read()[1]
        if frame is None:
            break
        # resize
        h, w = frame.shape[:2]
        width = 600
        rate = width / float(w)
        dim = (width, int(h * rate))
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        # convert to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the video to output path
        if (arguments.get("output") or arguments.get("o")) is not None and writer is None:
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            writer = cv2.VideoWriter(arguments.get("output") or arguments.get("o"),
                                     fourcc, 30,
                                     (frame.shape[1], frame.shape[0]),
                                     True)
        # check object
        if len(input_queues) == 0:
            h, w = frame.shape[:2]
            # Creates 4-dimensional blob from image.
            blob = cv2.dnn.blobFromImage(frame, 0.007843, (w, h), 127.5)
            # check and detections
            net.setInput(blob)
            detections = net.forward()
            # get check person object
            for i in np.arange(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                # filter
                if confidence > (arguments.get("confidence") or arguments.get("c")):
                    # get check object label
                    index = int(detections[0, 0, i, 1])
                    label = CLASSES[index]
                    # get people object
                    if label != "person":
                        continue
                    # label is person, get box
                    print(detections[0, 0, i, 3:7])
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    boxXY = (startX, startY, endX, endY)
                    # create multiprocessing Queue
                    in_queue = multiprocessing.Queue()
                    out_queue = multiprocessing.Queue()
                    input_queues.append(in_queue)
                    output_queues.append(out_queue)
                    # start process
                    pro = multiprocessing.Process(target=start_process_tracker,
                                                  args=(boxXY, label, frame_rgb, in_queue, out_queue))
                    pro.daemon = True
                    pro.start()

                    # draw object
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    cv2.putText(frame, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
        # just start tracker
        else:
            # in
            for in_queue in input_queues:
                in_queue.put(frame_rgb)
            # out
            for out_queue in output_queues:
                (label, (startX, startY, endX, endY)) = out_queue.get()
                # draw object
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(frame, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
        # save the track object frame
        if writer is not None:
            writer.write(frame)
        # show
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF
        # exit
        if key == 27:
            break
        # add one frame
        fps.update()
    # close sources
    if writer is not None:
        writer.release()
    cap_video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # param
    # --prototxt MobileNetSSDModel/MobileNetSSD_deploy.prototxt
    # --model MobileNetSSDModel/MobileNetSSD_deploy.caffemodel
    # --video VideoData/race.mp4
    arguments = get_parameters()
    # load caffe model
    net = load_caffe_model(arguments)
    # read video
    cap_video = read_video(arguments)
    # tracker
    fps = FPS().start()
    tracker_object(cap_video, arguments, net, fps)
    fps.stop()
    # time print
    print("Elapsed time: {:.2f}".format(fps.elapsed()))
    print("Approx. FPS: {:.2f}".format(fps.fps()))
