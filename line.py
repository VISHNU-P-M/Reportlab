from reportlab.pdfgen import canvas
from reportlab.lib import colors
pdf = canvas.Canvas('line.pdf', bottomup=0)
pdf.setLineWidth(5)
pdf.setStrokeColor(colors.blueviolet)
y = 10
for i in range(15):
    pdf.line(0, y, 100, y)
    y += 10
pdf.rotate(15)
y = 10
for i in range(15):
    pdf.line(0, y, 100, y)
    y += 10
pdf.save()