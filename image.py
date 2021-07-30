from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
pdf = canvas.Canvas('image.pdf')
pdf.translate(cm,cm)
pdf.drawImage("logo2.png", 100, 500, width=200, height=100)
pdf.setFont('Helvetica', 50)
pdf.setStrokeColor(colors.mintcream)
pdf.drawString(100, 400, "Vishnu")
pdf.showPage()
pdf.drawImage("index.png", 100, 100, width=400, height=400)
pdf.save()