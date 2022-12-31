import math


def mask_color_point(img, color_bgr, tolerance):
    for r, row in enumerate(img):
        for p, pix in enumerate(row):
            img[r][p] = get_pixel_color(color_bgr, pix, tolerance)
    return img


def get_pixel_color(color_bgr, pix, tolerance):
    return pix if math.dist(pix, color_bgr) < tolerance else [0, 0, 0]
