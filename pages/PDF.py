from  fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P" , unit="mm" , format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial" , size=12 , style="B")
    pdf.set_text_color(100 , 100 , 100)
    pdf.cell(0 , 12 , txt=row["Topic"] , align="L" , ln= 1 )
    pdf.line(10,21,200,21)

    for i in range(row["Pages"] - 1):
        pdf.add_page()



pdf.output("pdf.pdf")