import cv2
import numpy as np

from src.image_ops import show_img


def mask_color(img, _lower_hsv, _upper_hsv=None):
    lower_color = np.array(_lower_hsv)
    if _upper_hsv is None:
        _upper_color = _lower_hsv
    upper_color = np.array(_upper_hsv)
    mask = cv2.inRange(img, lower_color, upper_color)
    return cv2.bitwise_and(img, img, mask=mask)