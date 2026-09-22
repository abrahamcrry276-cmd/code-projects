#python JPGtoPNGConverter.py  dir_with_images  choose_new_dir_name
import sys
import os
from PIL import Image

first = sys.argv[0]
image_dir = sys.argv[1]
new_png_dir = sys.argv[2]

if not os.path.exists(new_png_dir):
    os.mkdir(new_png_dir)

for file in os.listdir(image_dir):
    if os.path.isfile(os.path.join(image_dir, file)):
        clean_name = os.path.splitext(file)[0]
        img = Image.open(f'{image_dir}/{file}')
        img.save(f'{new_png_dir}/{clean_name}.png', 'png')
    else:
        continue
