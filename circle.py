from re import S
from reportlab.lib import pagesizes
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
pdf = canvas.Canvas('circle.pdf', bottomup=0, pagesize=A4)
pdf.translate(inch, inch)
pdf.setFillColor(colors.gray)
pdf.ellipse(0, 0, 200, 150, stroke=0, fill=1)
pdf.setFillColorCMYK(0,0,0,1)
pdf.circle(50, 50, 30, stroke=0, fill=1)
pdf.circle(150, 50, 30, stroke=0, fill=1)
pdf.setFillColor(colors.gray)
pdf.circle(50,50, 20, stroke=0, fill=1)
pdf.circle(150,50, 20, stroke=0, fill=1)
pdf.setFillColor(colors.black)
pdf.setStrokeColor(colors.white)
pdf.circle(55, 40, 10, stroke=1, fill=1)
pdf.circle(145, 40, 10, stroke=1, fill=1)
pdf.wedge(90, 40, 110, 80, 50, 80, stroke=0, fill=1)
pdf.setFillColorRGB(1, 0, 0)
pdf.ellipse(50, 90, 150, 120, stroke=0, fill=1)
pdf.setStrokeColor(colors.black)
pdf.line(50,105, 150, 105)
pdf.save()