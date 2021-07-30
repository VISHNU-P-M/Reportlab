from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.flowables import Image
from reportlab.lib.units import inch
class RotateImage(Image):
    
    def wrap(self, availWidth, availHeight):
        h, w = Image.wrap(self,availWidth, availHeight)
        return w, h
    
    def draw(self):
        self.canv.rotate(90)

pdf = SimpleDocTemplate('rotate.pdf')   
obj = RotateImage('logo2.png', 1*inch, 1*inch)
image = obj.wrap(100,100)
print(image)
story = []
story.append(obj)
pdf.build(story)