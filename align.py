from reportlab.pdfgen import canvas
pdf=canvas.Canvas('align.pdf', bottomup=0)
pdf.setFont("Helvetica-Oblique", 10)
pdf.drawString(55,10,"normal text")
pdf.drawRightString(55,20,"right aligned")
pdf.drawAlignedString(55,30,"aligned string")
pdf.save()