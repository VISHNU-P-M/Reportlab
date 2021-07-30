from reportlab.graphics.shapes import *
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.platypus import SimpleDocTemplate

story = []
drawing = Drawing(400, 200)
data = [    
        (13, 5, 20, 22, 37, 45, 19, 4),    
        (5, 20, 46, 38, 23, 21, 6, 14)
        ]

lc = HorizontalLineChart()
lc.x = 50
lc.y = 50
lc.height = 150
lc.width = 300
lc.data = data
lc.joinedLines = 1
lc.categoryAxis.categoryNames = 'Jan Feb Mar Apr May Jun Jul Aug'.split(' ')
lc.categoryAxis.labels.boxAnchor = 'n'
lc.valueAxis.valueMax = 60
lc.valueAxis.valueMin = 0
lc.valueAxis.valueStep = 15
lc.lines[0].strokeWidth = 2
lc.lines[1].strokeWidth = 2
drawing.add(lc)
story.append(drawing)
pdf = SimpleDocTemplate('linechart.pdf')
pdf.build(story)