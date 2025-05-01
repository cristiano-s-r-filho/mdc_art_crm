import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO

def export_to_csv(data: List[Dict], filename: str):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def export_to_excel(data: List[Dict], filename: str):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def export_to_pdf(data: List[Dict], filename: str):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [list(data[0].keys())] + [list(row.values()) for row in data]
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), (0.8,0.8,0.8)),
        ('TEXTCOLOR', (0,0), (-1,0), (0,0,0)),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTSIZE', (0,0), (-1,0), 14),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ]))
    doc.build([table])
    buffer.seek(0)
    return buffer