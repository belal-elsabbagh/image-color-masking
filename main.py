from src.image_ops import show_img, read_img, read_img_color
from src.mask_color import mask_color

if __name__ == '__main__':
    rainbow_path = r'data\rainbow.png'
    color_pencils_path = r'data\color_pencils.jpeg'
    rainbow_img = read_img(color_pencils_path)
    show_img('result', mask_color(rainbow_img, [0,0,50], [100,255,255]))