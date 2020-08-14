# encoding: utf-8
import argparse
import numpy as np
from skimage.exposure import rescale_intensity

import cv2


def get_parameters():
    arg = argparse.ArgumentParser()
    arg.add_argument("-i", "--image", required=True, help="Input the picture data path")
    arguments = vars(arg.parse_args())
    return arguments


def get_kernels():
    smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
    largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))
    sharpen = np.array((
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]), dtype="int")

    laplacian = np.array((
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]), dtype="int")

    sobelX = np.array((
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]), dtype="int")

    sobelY = np.array((
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]), dtype="int")
    return (
        ("small_blur", smallBlur),
        ("large_blur", largeBlur),
        ("sharpen", sharpen),
        ("laplacian", laplacian),
        ("sobel_x", sobelX),
        ("sobel_y", sobelY)
    )


def get_image(img_path):
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img


def convolutional(image, kernel):
    # 输入图像和核的尺寸
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    # 选择pad，卷积后图像大小不变
    pad = (kW - 1) // 2
    # 重复最后一个元素，top, bottom, left, right
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")

    # 卷积操作
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # 提取每一个卷积区域
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

            # 内积运算
            k = (roi * kernel).sum()

            # 保存相应的结果
            output[y - pad, x - pad] = k

    # 将得到的结果放缩到[0, 255]
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

    return output


def kernels_convolutional(gray_img, kernels):
    for kernel_name, kernel in kernels:
        print("applying the {} kernel.".format(kernel_name))
        self_result = convolutional(gray_img, kernel)
        opencv_result = cv2.filter2D(gray_img, ddepth=-1, kernel=kernel)

        # show
        cv2.imshow("gray_img", gray_img)
        cv2.imshow("self_result", self_result)
        cv2.imshow("opencv_result", opencv_result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    # parameters
    # add : `--image Data/lanpangzi.jpg` to configurations
    arguments = get_parameters()
    # get different kernel
    kernels = get_kernels()
    # get image
    gray_img = get_image(arguments.get("i") or arguments.get("image"))
    # use different kernel convolutional
    kernels_convolutional(gray_img, kernels)
