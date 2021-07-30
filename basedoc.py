from reportlab.platypus import PageTemplate, BaseDocTemplate, NextPageTemplate
from reportlab.platypus.flowables import PageBreak
from reportlab.platypus.frames import Frame
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize

def headerFooterLayout(canvas, doc):
    canvas.saveState()
    canvas.drawImage('logo2.png',200, 200, 100, 100)
    # canvas.setPageSize(defaultPageSize)
    # add header/footer
    canvas.restoreState()

def emptyLayout(canvas, doc):
    canvas.saveState()
    canvas.line(100,100,500,100)
    # canvas.setPageSize(self.pagesize)
    canvas.restoreState()

pHeight, pWidth = defaultPageSize
style = getSampleStyleSheet()
myFrame = Frame(0, 0, pHeight, pWidth, id='myFrame')

headerFooterTemplate = PageTemplate(id='headerFooterTemplate',
                                    frames=[myFrame],
                                    onPage=headerFooterLayout)

emptyTemplate = PageTemplate(id='emptyTemplate',
                             frames=[myFrame],
                             onPage=emptyLayout)

elements = []
elements.append(Paragraph('blah', style['Normal']))
elements.append(NextPageTemplate('emptyTemplate'))
elements.append(PageBreak())
elements.append(Paragraph('last page', style['Normal']))
elements.append(PageBreak())
elements.append(Paragraph('last page', style['Normal']))

doc = BaseDocTemplate('base.pdf',
                      rightMargin=72,
                      leftMargin=72,
                      topMargin=72,
                      bottomMargin=72)

doc.addPageTemplates([headerFooterTemplate, emptyTemplate])

doc.build(elements)