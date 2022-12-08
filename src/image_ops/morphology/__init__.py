import cv2
import numpy as np


def morph(img, mode, kernel=None, kernel_size=None):
    if kernel is None and kernel_size is not None:
        kernel = default_kernel(kernel_size)
    return cv2.morphologyEx(img, mode, kernel)


def default_kernel(kernel_size):
    return np.ones(kernel_size, dtype=np.uint8)


def morph_open(img, kernel=None, kernel_size=None):
    return morph(img, cv2.MORPH_OPEN, kernel, kernel_size)


def morph_close(img, kernel=None, kernel_size=None):
    return morph(img, cv2.MORPH_CLOSE, kernel, kernel_size)


def morph_gradient(img, kernel=None, kernel_size=None):
    return morph(img, cv2.MORPH_GRADIENT, kernel, kernel_size)
