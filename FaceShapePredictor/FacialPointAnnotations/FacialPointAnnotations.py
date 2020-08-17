# encoding: utf-8
import argparse
from collections import OrderedDict
import dlib
import cv2
import numpy as np

FACIAL_LANDMARKS_68_IDXS = OrderedDict([
    ("mouth", (48, 68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 36)),
    ("jaw", (0, 17))
])

FACIAL_LANDMARKS_5_IDXS = OrderedDict([
    ("right_eye", (2, 3)),
    ("left_eye", (0, 1)),
    ("nose", (4))
])


def get_parameters():
    """
    warning: if arguments use `-`, It can be default change to `_`.
    source code: dest = dest.replace('-', '_')
    :return:
    """
    arg = argparse.ArgumentParser()
    arg.add_argument("-p", "--shape_predictor", required=True, help="Input the shape predictor data path")
    arg.add_argument("-i", "--image", required=True, help="Input the picture data path")
    arguments = vars(arg.parse_args())
    return arguments


def get_face_handler(arguments):
    detector = dlib.get_frontal_face_detector()
    arg = arguments.get("shape_predictor")
    predictor = dlib.shape_predictor(arg)
    return detector, predictor


def self_resize(img, new_width):
    (h, w) = img.shape[:2]
    ratio = new_width / float(w)
    dim = (new_width, int(h * ratio))
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return img


def get_img(arguments):
    img = cv2.imread(arguments.get("image") or arguments.get("i"))
    img = self_resize(img, 500)  # resize

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, gray_img


def shape_to_np(shape, dtype="int"):
    # 创建68*2
    coords = np.zeros((shape.num_parts, 2), dtype=dtype)
    # 遍历每一个关键点
    # 得到坐标
    for i in range(0, shape.num_parts):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords


def show_img(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def visualize_facial_landmarks(image, shape, colors=None, alpha=0.75):
    # 创建两个copy
    # overlay and one for the final output image
    overlay = image.copy()
    output = image.copy()
    # 设置一些颜色区域
    if colors is None:
        colors = [(19, 199, 109), (79, 76, 240), (230, 159, 23), (168, 100, 168),
                  (158, 163, 32), (163, 38, 32), (180, 42, 220)]
    # 遍历每一个区域
    for (i, name) in enumerate(FACIAL_LANDMARKS_68_IDXS.keys()):
        # 得到每一个点的坐标
        (j, k) = FACIAL_LANDMARKS_68_IDXS[name]
        pts = shape[j:k]
        # 检查位置
        if name == "jaw":
            # 用线条连起来
            for l in range(1, len(pts)):
                ptA = tuple(pts[l - 1])
                ptB = tuple(pts[l])
                cv2.line(overlay, ptA, ptB, colors[i], 2)
        # 计算凸包
        else:
            hull = cv2.convexHull(pts)
            cv2.drawContours(overlay, [hull], -1, colors[i], -1)
    # 叠加在原图上，可以指定比例
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
    return output


def get_facial_point(detector, predictor, img, gray_img):
    # get face
    rects = detector(gray_img, 1)

    for (i, rect) in enumerate(rects):
        # get face point
        shapes = predictor(gray_img, rect)
        shapes = shape_to_np(shapes)  # convert

        for (name, (i, j)) in FACIAL_LANDMARKS_68_IDXS.items():
            clone = img.copy()
            cv2.putText(clone, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # draw point
            for (x, y) in shapes[i:j]:
                cv2.circle(clone, (x, y), 3, (0, 0, 255), -1)

            # get roi area
            (x, y, w, h) = cv2.boundingRect(np.array([shapes[i:j]]))
            roi = img[y:y + h, x:x + w]
            roi = self_resize(roi, 250)  # resize
            cv2.imshow("roi", roi)
            cv2.imshow("image", clone)
            cv2.waitKey(0)
        output = visualize_facial_landmarks(img, shapes)
        show_img("image", output)


if __name__ == '__main__':
    # parameters
    # --shape_predictor ../Data/shape_predictor_68_face_landmarks.dat
    # --image ../Data/liudehua.jpg
    arguments = get_parameters()
    # get face key point handler
    detector, predictor = get_face_handler(arguments)
    # get img and preprocess
    img, gray_img = get_img(arguments)
    # get facial point detector
    get_facial_point(detector, predictor, img, gray_img)
