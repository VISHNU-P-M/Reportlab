from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, ParaFrag
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.platypus.paragraph import Paragraph

story = []
style = getSampleStyleSheet()
story.append(Paragraph('halloo', style['Normal']))
canv = SimpleDocTemplate('example.pdf')
d= Drawing(400, 200)
d.add(Rect(50, 50, 300, 100, fillColor=colors.yellow))
d.add(String(150, 100, 'hello World', fontSize=20, fillColor=colors.red))
d.add(String(180,86, 'Special characters \\xc2\xa2\xc2\xa9\xc2\xae\xc2\xa3\xce\xb1\xce\xb2',                 
            fillColor=colors.red))
story.append(d)
canv.build(story)