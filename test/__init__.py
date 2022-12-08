from src.image_ops import show_img
from src.image_ops.morphology import morph_open, morph_close
from src.mask_color import mask_color, mask_color_single


def test_color_masking(img, color, tolerance):
    morphed_img = morph_close(img, kernel_size=13)
    show_img('result', mask_color_single(morphed_img, color, tolerance))
