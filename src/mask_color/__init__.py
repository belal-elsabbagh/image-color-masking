import math

import cv2
import numpy as np


def mask_color(img, _lower_bgr, _upper_bgr=None):
    lower_color = np.array(_lower_bgr)
    if _upper_bgr is None:
        _upper_color = _lower_bgr
    upper_color = np.array(_upper_bgr)
    mask = cv2.inRange(img, lower_color, upper_color)
    return cv2.bitwise_and(img, img, mask=mask)


def mask_color_single(img, color_bgr, tolerance):
    for r, row in enumerate(img):
        for p, pix in enumerate(row):
            if math.dist(pix, color_bgr) > tolerance:
                img[r][p] = [0,0,0]
    return img

