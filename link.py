from reportlab.lib import styles
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
pdf = SimpleDocTemplate('link.pdf')
style = getSampleStyleSheet()
story = []
text = '''If you want to be get my profile,
           click <a href=http://vishnu-pm.xyz/ color="blue">here</a>'''
para = Paragraph(text, style['Normal'])
story.append(para)
pdf.build(story)