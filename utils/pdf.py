from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def export_to_pdf(report_text: str, output_path: str) -> str:
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = [Paragraph("Deep Research AI Report", styles["Title"]), Spacer(1, 12)]

    for paragraph in report_text.split("\n"):
        if paragraph.strip():
            story.append(Paragraph(paragraph, styles["BodyText"]))
            story.append(Spacer(1, 6))

    doc.build(story)
    return output_path
