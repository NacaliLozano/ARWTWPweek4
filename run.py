#!/usr/bin/env python3
"""This script processes all the data stored in text files into a JSON dictionary"""
import os
import requests
os.chdir("/supplier-data/descriptions")
for file in os.listdir():
    try:
        with open(file) as f:
            lines = f.readlines()
            dictionary = {}
            dictionary["name"] = str(lines[0]).strip()
            dictionary["weigh"] = int(str(lines[1]).strip()[:-4])
            dictionary["description"] = str(lines[2:]).strip()
            dictionary["image_name"] = file[:-4] + ".jpeg"
            response = requests.post("http://[linux-instance-external-IP]/fruits", json=dictionary)
            print(response.status_code)
            print(response.request.body)
    except OSError:
        print("Error opening {}.".format(file))