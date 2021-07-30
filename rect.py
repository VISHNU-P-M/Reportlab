from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
pdf = canvas.Canvas('rect.pdf', bottomup=0)
pdf.translate(inch, inch)
pdf.setFillColorCMYK(0,0,0,1, alpha=.8)
pdf.rect(8, 25, 100, 150, fill=1, stroke=0)
pdf.setFillColorCMYK(1, .2, .1, 0)
pdf.rect(50, 50, 10, 100, fill=1, stroke=0)
pdf.setFillColorCMYK(0.5, .3, .1, .1, alpha=.5)
pdf.rect(30, 80, 50, 10, fill=1, stroke=0)
pdf.save()