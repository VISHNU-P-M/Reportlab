from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
pdf = canvas.Canvas('table.pdf')
# pdf = SimpleDocTemplate('table.pdf')
# story = []
tablestyle = TableStyle([('BOX',(0,0),(-1,-1),1,colors.red),
                        ('BACKGROUND',(0,0),(-1,-1),colors.lightblue),
                        ('FONT',(0,0),(-1,-1),"Times-Italic"),
                        ('TEXTCOLOR',(0,0),(-1,-1),colors.gray)])
data = [['No', 'Name', 'district', 'Phone'],[str(i) for i in range(4)],['2','sreedevi','pkd', 'asdf']]
table = Table(data, colWidths=1*inch, rowHeights=.3*inch)
table.setStyle(tablestyle)
table.wrapOn(pdf,500, 500)
table.drawOn(pdf,20,700)
pdf.save()
# story.append(table)
# pdf.build(story)