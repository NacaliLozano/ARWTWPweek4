"""This script generates a report PDF file with the parameters attachment_path, title and paragraph"""
#!/usr/bin/env python3
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate

def generate_report(attachment_path, title, paragraph):
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(paragraph, styles["Normal"])
    report = SimpleDocTemplate(attachment_path)
    report.build([report_title, report_body])