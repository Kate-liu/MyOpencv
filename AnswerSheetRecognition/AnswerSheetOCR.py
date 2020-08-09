# -*- coding:utf-8 -*-
import time

import cv2
import argparse
import numpy as np


def get_parameters():
    arg = argparse.ArgumentParser()
    arg.add_argument("-i", "--image", required=True, help="Input the picture data path")
    arguments = vars(arg.parse_args())
    return arguments


def show_img(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def sort_contours(contours, method='left-to-right'):
    """
    According the method to sort the contours.
    :param contours:
    :param method:
    :return:
    """
    reverse = False
    i = 0
    # judge method
    if method == 'right-to-left' or method == 'right-to-left':
        reverse = True
    if method == 'top-to-bottom' or method == 'bottom-to-top':
        i = 1

    # Calculates the up-right bounding rectangle
    bounding_box = [cv2.boundingRect(con) for con in contours]

    contours, bounding_box = zip(*sorted(zip(contours, bounding_box), key=lambda b: b[1][i], reverse=reverse))

    return contours, bounding_box


def get_answer_sheet(data_path):
    original_img = cv2.imread(data_path)
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    edged_img = cv2.Canny(blur_img, 75, 200)

    show_img("original_img", original_img)
    show_img("gray_img", gray_img)
    show_img("blur_img", blur_img)
    show_img("edged_img", edged_img)
    return original_img, gray_img, blur_img, edged_img


def get_contours(original_img, edged_img):
    original_img_copy = original_img.copy()
    edged_img_copy = edged_img.copy()
    contours = cv2.findContours(edged_img_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
    cv2.drawContours(original_img_copy, contours, -1, (0, 0, 255), 3)
    show_img("original_img_copy", original_img_copy)

    # make sure answer sheet is the contour
    answer_contour = None
    if len(contours) > 0:
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        for cn in contours:
            length = cv2.arcLength(cn, True)
            approx = cv2.approxPolyDP(cn, 0.02 * length, True)

            if len(approx) == 4:
                answer_contour = approx
                break
    return answer_contour


def get_point(pts):
    rect = np.zeros((4, 2), dtype="float32")

    # find the coordinate, sorted: top_left, top_right, bottom_right, bottom_left
    # ps: here is used the picture different point  height + weight and height - weight value is different
    # top_left, bottom_right
    sums = pts.sum(axis=1)
    rect[0] = pts[np.argmin(sums)]
    rect[2] = pts[np.argmax(sums)]
    # top_right, bottom_left
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def perspective_transform(gray_img, pts):
    rectangle = get_point(pts)  # sort the rectangle point
    (top_left, top_right, bottom_right, bottom_left) = rectangle

    # get max width and height
    # ps: used the two point distance function method
    widthA = np.sqrt(((bottom_right[0] - bottom_left[0]) ** 2) + ((bottom_right[1] - bottom_left[1]) ** 2))
    widthB = np.sqrt(((top_right[0] - top_left[0]) ** 2) + ((top_right[1] - top_left[1]) ** 2))
    max_width = max(int(widthA), int(widthB))
    heighA = np.sqrt(((top_right[0] - bottom_right[0]) ** 2) + ((top_right[1] - bottom_right[1]) ** 2))
    heighB = np.sqrt(((top_left[0] - bottom_left[0]) ** 2) + ((top_left[1] - bottom_left[1]) ** 2))
    max_height = max(int(heighA), int(heighB))

    # perspective transform result point position
    dst = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]], dtype="float32")

    # perspective transform
    # \f[\begin{bmatrix} t_i x'_i \\ t_i y'_i \\ t_i \end{bmatrix} =
    # \texttt{map_matrix} \cdot \begin{bmatrix} x_i \\ y_i \\ 1 \end{bmatrix}\f]
    # link: https://blog.csdn.net/geduo_feng/article/details/81478672
    # link: https://zhuanlan.zhihu.com/p/36082864
    M = cv2.getPerspectiveTransform(rectangle, dst)
    warped = cv2.warpPerspective(gray_img, M, (max_width, max_height))

    threshold = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]  # threshold

    show_img('gray_img', gray_img)
    show_img('warped', warped)
    show_img('threshold', threshold)

    return warped, threshold


def find_answer_circle(threshold):
    # find
    contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
    threshold_copy = threshold.copy()
    # draw
    cv2.drawContours(threshold_copy, contours, -1, (0, 0, 255), 3)
    show_img("threshold_copy", threshold_copy)
    # match circle
    circles = []
    for con in contours:
        (x, y, w, h) = cv2.boundingRect(con)
        rate = w / float(h)
        # circle size and match
        if w >= 20 and h >= 20 and rate >= 0.9 and rate <= 1.1:
            circles.append(con)
    # sort top to bottom
    finally_contours = sort_contours(circles, "top-to-bottom")[0]
    return finally_contours


def get_answer_sheet_score(finally_contours, threshold, ANSWER_KEY):
    correct_answer = 0
    for (answer, i) in enumerate(np.arange(0, len(finally_contours), 5)):
        # sort left to right
        line_contours = sort_contours(finally_contours[i:i + 5])[0]
        # calculate every line contour
        bubbled = None
        for (contour, j) in enumerate(line_contours):
            # mask
            mask = np.zeros(threshold.shape, dtype="uint8")
            cv2.drawContours(mask, [j], -1, 255, -1)
            show_img("mask", mask)
            # Counts non-zero array elements
            mask = cv2.bitwise_and(threshold, threshold, mask=mask)
            total = cv2.countNonZero(mask)
            # use threshold method get answer contour
            if bubbled is None or total > bubbled[0]:
                bubbled = (total, contour)

        # get correct answer
        color = (0, 0, 255)
        key = ANSWER_KEY[answer]
        # judge answer
        if key == bubbled[1]:
            color = (0, 255, 0)
            correct_answer += 1
        cv2.drawContours(warped, [line_contours[key]], -1, color, 3)

    return correct_answer


def get_score(correct_answer, warped):
    score = (correct_answer / 5) * 100
    print("score: {:.2f}%".format(score))
    cv2.putText(warped, "{:.2f}%".format(score), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    cv2.imshow("result", warped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # param : correct answer { }
    ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}
    # parameters
    # add : `--image Data/test_01.png` to configurations
    arguments = get_parameters()
    # read
    original_img, gray_img, blur_img, edged_img = get_answer_sheet(arguments.get("i") or arguments.get("image"))
    # contours
    answer_contour = get_contours(original_img, edged_img)
    # four point transform
    warped, threshold = perspective_transform(gray_img, answer_contour.reshape(4, 2))
    # find answer circle
    finally_contours = find_answer_circle(threshold)
    # get correct answer
    correct_answer = get_answer_sheet_score(finally_contours, threshold, ANSWER_KEY)
    #  get score
    get_score(correct_answer, warped)
