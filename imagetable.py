from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.platypus.flowables import Image
pdf = SimpleDocTemplate('imagetable.pdf')
story = []
img_data = Image('index.png', 100, 100)
data = [[img_data for i in range(4)]]
tablestyle = TableStyle([('GRID', (0,0),(-1,-1), .5,colors.green)])
table = Table(data, style=tablestyle)
story.append(table)
pdf.build(story)