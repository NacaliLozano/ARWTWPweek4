#!/usr/bin/env python3
"""This script will check for the health of the system every 60 seconds and send an automated email if the condition is bad."""
import shutil, psutil, time, socket
from emails import generate_email, send_email

username = "<USERNAME>@example.com"

#Check CPU usage
cpu_percent = psutil.cpu_percent()
if cpu_percent > 80:
    email = generate_email("automation@example.com", 
                           username, 
                           "Error - CPU usage is over 80%", 
                           "Please check your system and resolve the issue as soon as possible.", 
                           "")
    send_email(email)

#Check disk available
disk_total, disk_used, disk_free = shutil.disk_usage("/")
if disk_free / disk_total < 0.2:
    email = generate_email("automation@example.com", 
                           username, 
                           "Error - Available disk space is less than 20%", 
                           "Please check your system and resolve the issue as soon as possible.", 
                           "")
    send_email(email)
    
#Check RAM available
ram_info = psutil.virtual_memory()
if ram_info.available < 500 * 1024 * 1024:
    email = generate_email("automation@example.com", 
                           username, 
                           "Error - Available memory is less than 500MB", 
                           "Please check your system and resolve the issue as soon as possible.", 
                           "")
    send_email(email)
    
#Check localhost
if socket.gethostbyname("localhost") != "127.0.0.1":
    email = generate_email("automation@example.com", 
                           username, 
                           "Error - localhost cannot be resolved to 127.0.0.1", 
                           "Please check your system and resolve the issue as soon as possible.", 
                           "")
    send_email(email)
