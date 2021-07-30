from reportlab.graphics.shapes import *
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.platypus import SimpleDocTemplate
story = []
drawing = Drawing(400, 200)
data = [
        (13, 5, 20, 22, 37, 45, 19, 4),            
        (14, 6, 21, 23, 38, 46, 20, 5)
        ]
bar = VerticalBarChart()
bar.x = 50
bar.y = 60
bar.height = 150
bar.width = 300
bar.data = data
bar.strokeColor = colors.black
bar.valueAxis.valueMin = 0
bar.valueAxis.valueMax = 50
bar.valueAxis.valueStep = 10
bar.categoryAxis.labels.boxAnchor = 'ne'
bar.categoryAxis.labels.dx = 8
bar.categoryAxis.labels.dy = -2
bar.categoryAxis.labels.angle = 30
bar.categoryAxis.categoryNames = [
                                    'Jan-99','Feb-99','Mar-99',           
                                    'Apr-99','May-99','Jun-99', 
                                    'Jul-99','Aug-99'
                                ]
drawing.add(bar)
story.append(drawing)
pdf = SimpleDocTemplate('barchart.pdf')
pdf.build(story)