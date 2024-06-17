from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF("P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


for index, line in df.iterrows():
    k = line["Pages"]
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=50)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=line["Topic"], align="L",
             ln=1, border=0)
    pdf.line(10,33, 200, 33)

    pdf.ln(250)

    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10, txt=line["Topic"], align="R")

    for i in range(30):
        pdf.ln(10)
        pdf.line(10, 33+(i*10), 200, 33+(i*10))

    while k > 1:
        pdf.add_page()
        pdf.ln(266)

        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=line["Topic"], align="R")
        k=-1

        for i in range(30):
            pdf.ln(10)
            pdf.line(10, 33 + (i * 10), 200, 33 + (i * 10))

pdf.output("output.pdf")