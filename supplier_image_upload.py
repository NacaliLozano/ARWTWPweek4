#!/usr/bin/env python3
"""This script uploads all the files with the .jpeg extention in a given directory to a given URL."""
import requests
import os
url = "http://localhost/upload/"
dir_path = "~/supplier-data/images"
os.chdir(dir_path)
for item in os.listdir():
    if item.endswith(".jpeg"):
        with open(item, "rb") as f:
            r = requests.post(url, files={"file": f})