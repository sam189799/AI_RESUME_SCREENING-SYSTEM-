from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filepath, score, feedback, rating,
                    matched, missing,
                    strengths, weaknesses,
                    suggestions):

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Screening Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {score}%", styles["Normal"]))
    story.append(Paragraph(f"<b>Feedback:</b> {feedback}", styles["Normal"]))
    story.append(Paragraph(f"<b>Resume Rating:</b> {rating}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Matched Skills</b>", styles["Heading2"]))
    for i in matched:
        story.append(Paragraph("• " + i, styles["Normal"]))

    story.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))
    for i in missing:
        story.append(Paragraph("• " + i, styles["Normal"]))

    story.append(Paragraph("<br/><b>Strengths</b>", styles["Heading2"]))
    for i in strengths:
        story.append(Paragraph("• " + i, styles["Normal"]))

    story.append(Paragraph("<br/><b>Weaknesses</b>", styles["Heading2"]))
    for i in weaknesses:
        story.append(Paragraph("• " + i, styles["Normal"]))

    story.append(Paragraph("<br/><b>Suggestions</b>", styles["Heading2"]))
    for i in suggestions:
        story.append(Paragraph("• " + i, styles["Normal"]))

    doc.build(story)