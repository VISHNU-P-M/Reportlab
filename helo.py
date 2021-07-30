from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
pdf = canvas.Canvas('sample.pdf')
pdf.translate(inch,inch)
pdf.setFont("Helvetica", 14)
pdf.setStrokeColorRGB(0.2,0.5,0.3)
pdf.setFillColorRGB(1,0,1)
pdf.line(0,0,0,1.7*inch)
pdf.line(0,0,1*inch,0)
pdf.rect(0.2*inch, 0.2*inch, 1*inch, 1.5*inch, fill= 1)
pdf.rotate(90)
pdf.setFillColorRGB(0,0,0.77)
pdf.drawString(0.3*inch, -inch, "Hello World")
pdf.save()