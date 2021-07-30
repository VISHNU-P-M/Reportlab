from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import Spacer
pdf = SimpleDocTemplate('platypus.pdf')
story = []
style = getSampleStyleSheet()
text = "hello every one How are you! hello every one How are you! hello every one How are you! hello every one How are you! hello every one How are you! hello every one How are you! "
para = Paragraph(text,style['Normal'])
story.append(para)
story.append(Spacer(1,10))
story.append(para)
story.append(Spacer(1,10))
story.append(para)
pdf.build(story)