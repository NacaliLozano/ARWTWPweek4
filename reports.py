"""This script generates a report PDF file with the parameters attachment_path, title and paragraph"""
#!/usr/bin/env python3
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from datetime import date
import os

def generate_report(attachment_path, title, paragraph):
    """Generates a PDF in the attachment_path"""
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(paragraph, styles["Normal"])
    report = SimpleDocTemplate(attachment_path)
    report.build([report_title, report_body])

if __name__ == "__main__":
    """Pre-processes the data in order to call generate_report"""
    styles = getSampleStyleSheet()
    title = "Processed Update on " + date.today().strftime("%B %d, %Y")
    os.chdir("/supplier-data/descriptions")
    paragraph = "<br/>"
    for file in os.listdir():
        try:
            with open(file) as f:
                lines = f.readlines()
                paragraph.append("name: " + str(lines[0]).strip() + "<br/>")
                paragraph.append("weight: " + str(lines[1]).strip() + "<br/><br/>")
        except OSError:
            print("Error opening {}.".format(file))
    generate_report("/tmp/processed.pdf", title, paragraph)