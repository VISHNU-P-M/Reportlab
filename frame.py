from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
style = getSampleStyleSheet()
stylen = style['Normal']
styleh = style['Heading1']
story = []
story.append(Paragraph('This is the Heading', styleh))
story.append(Paragraph('This is a <b>sample</b> <br/> paragraph..<u>undrelined</u> and <strike>striked</strike>', stylen))
pdf = canvas.Canvas('frame.pdf')
f = Frame(inch, inch, 6*inch, 10*inch, showBoundary=1)
f.addFromList(story,pdf)
pdf.save()