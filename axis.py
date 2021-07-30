from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.axes import XCategoryAxis, YValueAxis

story = []
drawing = Drawing(400, 200)
data = [(10, 20, 30, 40), (20, 22, 37, 42)]

xaxis = XCategoryAxis()
xaxis.setPosition(75, 75, 300)
xaxis.configure(data)
xaxis.categoryNames = ['Beer', 'Wine', 'Meat', 'Cannelloni']
xaxis.labels.boxAnchor = 'n'
yaxis = YValueAxis()
yaxis.setPosition(75, 75, 125)
yaxis.configure(data)
drawing.add(xaxis)
drawing.add(yaxis)
story.append(drawing)
pdf = SimpleDocTemplate('axis.pdf')
pdf.build(story)