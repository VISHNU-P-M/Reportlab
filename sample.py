from reportlab.platypus import Paragraph
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from datetime import date
page_width = defaultPageSize[0]
page_height = defaultPageSize[1]
canva = canvas.Canvas('pdf.pdf')

# canva.saveState()
canva.drawImage('cover.png',0,0,210*mm,297*mm)
canva.setFont('Times-Roman',28)
title = 'PROPOSAL'
canva.drawCentredString(page_width/2.0, page_height-300,title)
canva.setFontSize(18)
canva.drawCentredString(page_width/2.0, page_height-330,'For')
canva.setFontSize(40)
client_name = '<CLIENT NAME>'
canva.drawCentredString(page_width/2.0, page_height-400,client_name)
canva.setFontSize(10)
today = date.today()
today = str(today.day) + '-' + str(today.month) + '-' + str(today.year)
canva.drawCentredString(page_width/2.0, page_height-450, today)
canva.save()
# canva.restoreState()