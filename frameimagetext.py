from reportlab.lib import styles
from reportlab.platypus import Paragraph, Frame
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
pdf = canvas.Canvas('frameimage.pdf')
pdf.drawImage('index.png', 25, 480, width=200, height=200)
story = []
style = getSampleStyleSheet()
text = '''
        This is a text in frame
'''
para = Paragraph(text, style['Normal'])
story.append(para)
frame = Frame(20, 400, 500, 300, showBoundary=1)
frame.addFromList(story, pdf)
pdf.save()