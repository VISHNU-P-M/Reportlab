from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from math import pi, sin, cos
pdf = canvas.Canvas('star.pdf')
radius = inch / 3.0
xcenter = 2.74*inch
ycenter = 1.5*inch
p = pdf.beginPath()
p.moveTo(xcenter, ycenter+radius)
angle = (2*pi)*2/5.0
startangle = pi/2.0
for vertex in range(5):
    nextangle = angle*(vertex+1)+startangle
    x = xcenter + radius*cos(nextangle)
    y = ycenter + radius*sin(nextangle)
    p.lineTo(x,y)
p.close
pdf.drawPath(p)
pdf.save()
