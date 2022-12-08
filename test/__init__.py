from src.image_ops import show_img
from src.image_ops.morphology import morph_open
from src.mask_color import mask_color


def test_color_masking(img, lower_bgr=None, upper_bgr=None):
    if upper_bgr is None:
        upper_bgr = [100, 200, 255]
    if lower_bgr is None:
        lower_bgr = [0, 25, 50]
    morphed_img = morph_open(img, kernel_size=9)
    show_img('result', mask_color(morphed_img, lower_bgr, upper_bgr))
