# PROJECT: Document OCR recognition
import os
import time
import argparse
import cv2
import numpy as np
import pytesseract
from PIL import Image


def show_image(winname, mat):
    cv2.imshow(winname, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    According width and height resize picture.
    :param image:
    :param width:
    :param height:
    :param inter:
    :return:
    """
    dsize = None

    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dsize = (int(w * r), height)
    else:
        r = width / float(w)
        dsize = (width, int(h * r))

    resized = cv2.resize(image, dsize, interpolation=inter)
    return resized


def read_image(image_path):
    image = cv2.imread(image_path)
    show_image('image', image)

    ratio = image.shape[0] / 500.0  # change image ratio
    original_image = image.copy()

    resize_image = resize(original_image, height=500)  # resize
    show_image('resize_image', resize_image)

    return original_image, resize_image, ratio


def image_preprocess(resize_image):
    gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
    blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)  # filter
    canny_image = cv2.Canny(blur_image, 75, 200)  # edge detection
    show_image('canny_image', canny_image)
    return canny_image


def image_contour(resize_image, processing_image):
    contours = cv2.findContours(processing_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]  # all contour sorted by area, get five contour

    for c in contours:
        length = cv2.arcLength(c, True)
        # PictureProcessing/ImageContour.py -> line:90
        approx = cv2.approxPolyDP(c, 0.02 * length, True)

        # the outer contour is rectangle, so len is 4
        if len(approx) == 4:
            big_contour = approx
            break

    cv2.drawContours(resize_image, [big_contour], -1, (0, 255, 0), 2)
    show_image('contour image', resize_image)

    return big_contour


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


def perspective_transform(original_image, pts):
    rectangle = get_point(pts)
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
    warped = cv2.warpPerspective(original_image, M, (max_width, max_height))

    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)  # gray
    threshold = cv2.threshold(warped, 100, 255, cv2.THRESH_BINARY)[1]  # threshold

    cv2.imwrite('./OCRData/scan' + str(time.time()) + '.jpg', threshold)
    show_image('original_image', resize(original_image, height=650))
    show_image('threshold', resize(threshold, height=650))

    return threshold


def read_data(OCRData_path):
    image = cv2.imread(OCRData_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def preprocess_data(OCRData_preprocess, gray_image):
    preprocess_image = []
    if OCRData_preprocess == "thresh":
        preprocess_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    if OCRData_preprocess == "blur":
        preprocess_image = cv2.medianBlur(gray_image, 3)

    return preprocess_image


def pytesseract_image(preprocess_image, gray_image):
    filename = "./OCRResult/result{}.png".format(os.getpid())
    cv2.imwrite(filename, preprocess_image)

    text = pytesseract.image_to_string(Image.open(filename))  # get document string
    # print(text)
    os.remove(filename)

    file = open("./OCRResult/result{}.txt".format(os.getpid()), 'w', encoding="utf-8")  # flush to disk
    file.write(text)
    file.close()

    show_image("gray_image", gray_image)
    show_image("preprocess_image", preprocess_image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", required=True, help="The document OCR image path")
    args = vars(parser.parse_args())

    # read image
    original_image, resize_image, ratio = read_image(args.get('i') or args.get('image'))
    # processing image
    processing_image = image_preprocess(resize_image)
    # find document contour
    document_contour = image_contour(resize_image, processing_image)
    # perspective transform, change the angle of the document
    warped_threshold = perspective_transform(original_image, document_contour.reshape(4, 2) * ratio)

    # read Data method: use tesssract to get document text
    # OCRData_path = "./OCRData/scanDemo.jpg"
    # gray_image = read_data(OCRData_path)  # read
    # used already exist Data method:
    gray_image = warped_threshold

    OCRData_preprocess = 'blur'
    preprocess_image = preprocess_data(OCRData_preprocess, gray_image)  # preprocess

    pytesseract_image(preprocess_image, gray_image)  # pytesseract OCR
