from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import PageTemplate, Frame
from reportlab.platypus.flowables import PageBreak
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate

# Define the PageTemplate with one-inch margins
page_margin = 72  # 1 inch = 72 points
page_template = PageTemplate(
    id='lab_results',
    frames=[Frame(page_margin, page_margin, letter[0] - 2*page_margin, letter[1] - 2*page_margin)],
)

# Create a SimpleDocTemplate with the specified PageTemplate
doc = BaseDocTemplate("lab_results.pdf", pageTemplates=[page_template])

# Define Paragraph Styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'Title',
    parent=styles['Title'],
    alignment=1,
    fontSize=16,
    spaceAfter=12,
    fontName='Helvetica-Bold'
)

centered_title_style = ParagraphStyle(
    'CenteredTitle',
    parent=styles['Title'],
    alignment=1,
    fontSize=14,
    spaceAfter=12,
    fontName='Helvetica-Bold'
)

header_style = ParagraphStyle(
    'Header',
    parent=styles['Normal'],
    fontSize=12,
    fontName='Helvetica-Bold'
)

# Create the content for the PDF
content = []

# Title
title = Paragraph("PATIENT RESULTS", title_style)
content.append(title)

# Centered Title "AE LABORATORY"
centered_title = Paragraph("KML LABORATORY", centered_title_style)
content.append(centered_title)

# Information Line 1
info_line1 = Paragraph("NAME:         AGE:        SEX:        ", header_style)
content.append(info_line1)

# Information Line 2
info_line2 = Paragraph("SAMPLE ID:      DATE:       ", header_style)
content.append(info_line2)

# Add some space
content.append(Spacer(1, 12))

# Centered "LIVER FUNCTION TEST"
liver_function_title = Paragraph("LIVER FUNCTION TEST", centered_title_style)
content.append(liver_function_title)

# Create a table for the parameter results
data = [["Parameter", "Result", "Unit", "Ref Range"],
        ["Total Bilirubun", "Result 1", "umol/L", "[3.0-22.0]"],
        ["Direct Bilirubin", "Result 2", "umol/L", "[0.0-5.0]"],
        ["AST", "Result 3", "U/L", "[10-35]"],
        ["ALT", "35", "U/L", "[10-45]"],
        ["ALP", "Result 3", "U/L", "[38-126]"],
        ["GGT", "Result 3", "U/L", "[12-58]"],
        ["TP", "Result 3", "g/L", "[63-82]"],
        ["ALB", "Result 3", "g/L", "[35-50]"]]

table = Table(data, colWidths=[160, 80, 80, 160])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

content.append(table)

# Build the PDF
doc.build(content)
