from typing import List

from fpdf import FPDF



# EXAMPLE... TO GEN A NEW PDF... CREATE A NEW CLASS
class PdfGenerator(FPDF):

    def __init__(self, orientation, two_days_ago, yesterday, today):
        super().__init__(orientation)
        self.two_days_ago = two_days_ago
        self.yesterday = yesterday
        self.today = today

    def header(self):
        self.image("logo", x=5, y=5)
        self.set_font("courier", "B", 14)
        self.cell(txt=f"")
        self.ln(5)
        self.cell(txt=""
                      f"    RUN DATE {self.today.date().strftime('%d/%m/%Y')}")
        self.ln(5)
        self.cell(txt=f""
                      f"          RUN TIME   {self.today.time().strftime('%H:%M:%S')}")
        self.ln(5)
        self.cell(txt=f"                                   As At {self.yesterday.strftime('%d/%m/%Y')}")
        self.ln(10)

    def render_table_header(self, col_names: List[str]):
        self.set_font(style="B")
        self.set_fill_color(255, 165, 0)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "B", 10)
        # Printing page number:
        self.cell(0, 10, f"REPORT PAGE HOLDER", align="L")
        self.ln(5)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, "COMPANY PAGE HOLDER", align="L")
