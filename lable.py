from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import *
story = []
d = Drawing(400, 200)
lable = Label()
lable.setOrigin(100, 190)
lable.boxAnchor='ne'
lable.boxStrokeColor = colors.red
lable.dx=0
lable.dy=-20
lable.setText('SomeMulti-LineLabel')
d.add(lable)
story.append(d)
pdf = SimpleDocTemplate('lable.pdf')
pdf.build(story)