# Utils

import cv2


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
