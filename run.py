#!/usr/bin/env python3
"""This script processes all the data stored in text files into a JSON dictionary and posts it in a specified URL."""
import os
import requests
os.chdir("./supplier-data/descriptions")
for file in os.listdir():
    try:
        with open(file, "rb") as f:
            #Pre-proceses the data into a dictionary
            lines = f.readlines()
            dictionary = {}
            dictionary["name"] = lines[0].strip()
            dictionary["weight"] = int(lines[1].strip()[:-4])
            dictionary["description"] = lines[2].strip()
            dictionary["image_name"] = file[:-4] + ".jpeg"
            print(dictionary)
            #Post the dictionary
            response = requests.post("http://34.16.169.122/fruits/", data=dictionary)
            print(response.status_code)
            print(response.request.body)
    except OSError:
        print("Error opening {}.".format(file))
