#!/usr/bin/env python3
import os
from PIL import Image
dir_path = "~/supplier-data/images"
os.chdir(dir_path)
for item in os.listdir():
    with Image.open(item) as im:
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im.resize((600,400)).save(item + ".jpeg")