#!/usr/bin/env python3
"""This script processes all the data stored in text files into a JSON dictionary and posts it in a specified URL."""
import os
import requests
os.chdir("/supplier-data/descriptions")
for file in os.listdir():
    try:
        with open(file) as f:
            #Pre-proceses the data into a dictionary
            lines = f.readlines()
            dictionary = {}
            dictionary["name"] = str(lines[0]).strip()
            dictionary["weight"] = int(str(lines[1]).strip()[:-5])
            dictionary["description"] = str(lines[2:]).strip()
            dictionary["image_name"] = file[:-5] + ".jpeg"
            #Post the dictionary
            response = requests.post("http://[linux-instance-external-IP]/fruits", json=dictionary)
            print(response.status_code)
            print(response.request.body)
    except OSError:
        print("Error opening {}.".format(file))