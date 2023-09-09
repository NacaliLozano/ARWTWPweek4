    styles = getSampleStyleSheet()
    report_title = Paragraph("Processed Update on " + today.strftime("%B %d, %Y"), styles["h1"])
    os.chdir("/supplier-data/descriptions")
    report_body = [Paragraph("<br/>", styles["Normal"])]
    for file in os.listdir():
        try:
            with open(file) as f:
                lines = f.readlines()
                report_body.append(Paragraph("name: " + str(lines[0]).strip() + "<br/>", styles["Normal"]))
                report_body.append(Paragraph("weight: " + str(lines[1]).strip() + "<br/>", styles["Normal"]))
                report_body.append(Paragraph("<br/>", styles["Normal"])
