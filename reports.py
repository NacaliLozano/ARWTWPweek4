"""This script generates a report PDF file with the parameters attachment_path, title and paragraph"""
#!/usr/bin/env python3
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from datetime import date

def generate_report(attachment_path, title, paragraph):
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(paragraph, styles["Normal"])
    report = SimpleDocTemplate(attachment_path)
    report.build([report_title, report_body])

if __name__ == "__main__":
    styles = getSampleStyleSheet()
    title = "Processed Update on " + today.strftime("%B %d, %Y")
    os.chdir("/supplier-data/descriptions")
    paragraph = ""
    <br/>", styles["Normal"])]
    for file in os.listdir():
        try:
            with open(file) as f:
                lines = f.readlines()
                report_body.append(Paragraph("name: " + str(lines[0]).strip() + "<br/>", styles["Normal"]))
                report_body.append(Paragraph("weight: " + str(lines[1]).strip() + "<br/>", styles["Normal"]))
                report_body.append(Paragraph("<br/>", styles["Normal"])