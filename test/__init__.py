from src.image_ops import show_img
from src.mask_color import mask_color_point


def test_color_masking(img, color, tolerance):
    show_img('result', mask_color_point(img, color, tolerance))
