from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
style = getSampleStyleSheet()
pdf = SimpleDocTemplate('paraimage.pdf')
story = []
style['Normal'].spaceAfter=100
text = '''
        hai here my image, <img src="index.png" width="100" height="100"/>, Hope it not bad
    '''
para = Paragraph(text, style['Normal'])
story.append(para)
text = '''
        hai here my image, <img src="index.png" width="100" height="100"/>, Hope it not bad
    '''
para = Paragraph(text, style['Normal'])
story.append(para)
pdf.build(story)