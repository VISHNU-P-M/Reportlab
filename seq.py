from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.flowables import Spacer
style = getSampleStyleSheet()
pdf = SimpleDocTemplate('seq.pdf')
story = []
string = ['manoharan', 'Sreedevi', 'Vishnu', 'Vidya']
for name in string:
    text = '<font name="Times-Italic" size=50 color=Red><seq id="section-id">.%s</font>' %name
    para = Paragraph(text, style=style['Normal'])
    story.append(para)
    story.append(Spacer(1,30))
pdf.build(story)