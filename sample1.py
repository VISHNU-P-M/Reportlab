from reportlab.platypus import Paragraph
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import mm, inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import date
page_width = defaultPageSize[0]
page_height = defaultPageSize[1]
canva = canvas.Canvas('pdf1.pdf')

canva.setStrokeColor(colors.blue, alpha=.5)
canva.line(1*inch,page_height-50, page_width-1*inch,page_height-50)
canva.save()