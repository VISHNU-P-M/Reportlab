from reportlab.graphics.shapes import *
from reportlab.graphics.charts.piecharts import Pie
from reportlab.platypus import SimpleDocTemplate

story = []
d = Drawing(400,400)
pc = Pie()
pc.x = 150
pc.y = 50
pc.data = [10, 20, 30, 40, 50, 60]
pc.labels = ['a', 'b', 'c', 'd', 'e', 'f']
pc.sideLabels = 1
pc.slices.strokeWidth = 0.5
pc.slices[3].popout = 10
pc.slices[3].labelRadius = 1.75
pc.slices[3].fontColor = colors.red
d.add(pc)
story.append(d)
pdf = SimpleDocTemplate('pie.pdf')
pdf.build(story)
