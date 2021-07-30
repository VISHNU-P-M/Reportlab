from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
style = getSampleStyleSheet()
p = Paragraph('This is a testing of flowable', style['BodyText'])
pdf = canvas.Canvas('flowable.pdf')
aw = 460
ah = 800
w, h = p.wrap(aw,ah)
if w<=aw and h<=ah:
    p.drawOn(pdf,0,ah)
    pdf.save()
else:
    raise ValueError