#!/usr/bin/env python3
from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
    """Returns an email message configured with the input parameters."""
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    if attachment_path != "":
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=os.path.basename(attachment_path))
    print(message)
    return message

def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP("localhost")
    mail_server.send_message(message)
    mail_server.quit()