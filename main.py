from src.image_ops import read_img
from test import test_color_masking

if __name__ == '__main__':
    rainbow_path = r'data\rainbow.png'
    color_pencils_path = r'data\color_pencils.jpeg'

    rainbow_img = read_img(rainbow_path)
    color_pencils_img = read_img(color_pencils_path)

    orange_bgr = [0,120,255]

    test_color_masking(rainbow_img[:,:,:3], orange_bgr, 82.5)
    test_color_masking(color_pencils_img, orange_bgr, 70)
