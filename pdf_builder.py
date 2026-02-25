from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def create_pdf(story, image_paths):
    pdf_path = "fableforge_book.pdf"
    doc = SimpleDocTemplate(pdf_path)
    elements = []
    styles = getSampleStyleSheet()

    for i, page in enumerate(story["pages"]):
        elements.append(Paragraph(page["text"], styles["Normal"]))
        elements.append(Spacer(1, 0.3 * inch))
        elements.append(Image(image_paths[i], width=4*inch, height=4*inch))
        elements.append(Spacer(1, 0.5 * inch))

    doc.build(elements)
    return pdf_path
