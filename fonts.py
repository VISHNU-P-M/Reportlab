from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate('fonts.pdf')
story = []
style = getSampleStyleSheet()
text ='''<font name="Symbol" size=20 color="Red"> hai helo who are you</font>'''
para = Paragraph(text, style=style['Normal'])
story.append(para)
pdf.build(story)