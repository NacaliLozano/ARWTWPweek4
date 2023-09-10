#!/usr/bin/env python3
"""From here we will call generate_email and send_email methods in order to send the email."""
import emails
if __name__ == "__main__":
    email = generate_email("automation@example.com", 
                           "<USERNAME>@example.com", 
                           "Upload Completed - Online Fruit Store", 
                           "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", 
                           "/tmp/processed.pdf")
    send_email(email)