from reportlab.pdfgen import canvas
pdf = canvas.Canvas('new.pdf', bottomup=0)
y = 40
text_obj = pdf.beginText()
text_obj.setTextOrigin(20,20)
for line in open('hello.txt', 'r'):
    text_obj.textLine(line.strip())
pdf.drawText(text_obj)
pdf.save()