from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import pink, white, green, brown
c = canvas.Canvas('bars.pdf')
x = 0
dx = 0.4*inch
for i in range(4):
    for color in (pink,brown,green):
        c.setFillColor(color)
        c.rect(x, 0, dx, 3*inch, fill=1, stroke=0)
        x += dx
c.setFillColor(white)
c.setStrokeColor(white)
c.setFont('Helvetica-Bold', 85)
c.drawCentredString(2.5*inch, 1*inch, "VISHNU")
c.save()

