from PIL import Image
import sys


def generate_images_and_icon(image_name):
    im = Image.open(image_name)
    print("image_size :", im.size)
    liste_size_windows = [64, 48, 32, 24, 16]
    ico = im.resize((24,24))
    ico.save('Icon.ico')
    for size in liste_size_windows:
        new_im = im.resize((size, size))
        new_im.save(f'base/{size}.png')

    liste_size_linux_mac = [1024, 512, 265, 128]
    for size in liste_size_linux_mac:
        new_im = im.resize((size, size))
        new_im.save(f'linux/{size}.png')
        new_im.save(f'mac/{size}.png')


if __name__ == '__main__':
    image_name = sys.argv[1]
    generate_images_and_icon(image_name)