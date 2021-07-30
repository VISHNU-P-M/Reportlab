from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
item = canvas.Canvas('font.pdf')
available_fonts = item.getAvailableFonts()
item.translate(inch,inch)
y = 800
for font in available_fonts:
    item.setFont(font,23)
    item.setFillColorRGB(1,0,0)
    item.drawString(10,y, font)
    y -= 20
item.save()