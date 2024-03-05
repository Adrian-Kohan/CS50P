from fpdf import FPDF

name = input("Name: ")
shirt_text = f"{name} took CS50"

pdf = FPDF(orientation="Portrait", format="A4")
pdf.add_page()
pdf.set_font('helvetica', size=44)
pdf.cell(60, 35, center=True, text="CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=15, y=55, h=200, w=180)
pdf.set_font('helvetica', size=25)
pdf.set_text_color(255, 255, 255)
pdf.cell(72, 250, center=True, text=shirt_text, align="C")
pdf.output("shirtificate.pdf")