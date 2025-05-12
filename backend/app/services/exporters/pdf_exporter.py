from reportlab.pdfgen import canvas

def export_pdf(shopping_list: dict) -> bytes:
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    # PDF generation logic
    p.save()
    return buffer.getvalue()
