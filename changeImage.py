#!/usr/bin/env python3
"""This script iterates through all the images in a direxctory and modifies the format, size and extension."""
import os
from PIL import Image
dir_path = "./supplier-data/images"
os.chdir(dir_path)
for item in os.listdir():
    if item.endswith(".tiff"):
        with Image.open(item) as im:
            if im.mode != 'RGB':
                im = im.convert('RGB')
                im.resize((600,400)).save(item[:-5] + ".jpeg")
