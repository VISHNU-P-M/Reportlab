from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.flowables import PageBreak, Spacer
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
page_height = defaultPageSize[1]
page_width = defaultPageSize[0]
styles = getSampleStyleSheet()

title = "Hello World"
pageinfo = 'platypus example'

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 16)
    canvas.drawCentredString(page_width/2.0, page_height-108, title)
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch,"First Page / %s" % pageinfo)
    canvas.drawImage('logo2.png',400,500,100,100)
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch,"Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

def go():
    doc = SimpleDocTemplate("phello.pdf")
    Story = [Spacer(1,2*inch)]
    style = styles["Normal"]
    for i in range(100):
        bogustext = ("Paragraph number %s. " % i) 
    p = Paragraph(bogustext, style)
    Story.append(p)
    Story.append(PageBreak())
    Story.append(Spacer(1,0.2*inch))
    Story.append(p)
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

if __name__ == "__main__":
    go()