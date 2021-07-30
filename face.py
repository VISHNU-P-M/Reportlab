from reportlab.graphics import widgetbase
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.shapes import Drawing
story = []
drawing = Drawing(400, 200)
face = widgetbase.Face()
face.skinColor = colors.yellow
face.eyeColor = colors.green
face.mood = 'happy'
drawing.add(face)
story.append(drawing)
pdf = SimpleDocTemplate('face.pdf')
pdf.build(story)