import math


def mask_color_point(img, color_bgr, tolerance):
    for r, row in enumerate(img):
        for p, pix in enumerate(row):
            if math.dist(pix, color_bgr) > tolerance:
                img[r][p] = [0, 0, 0]
    return img
