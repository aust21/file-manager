import fpdf
from fpdf import FPDF
import os
class PDF(FPDF):
	# def header(self, title) -> None:
	# 	self.set_font("times", "", 14)
	# 	title_width = self.get_string_width(title)
	# 	doc_width = self.w
	# 	self.set_x((doc_width - title_width) // 2)
	# 	self.set_fill_color(0, 80, 180)
	# 	self.set_text_color(220, 50, 50)
	# 	self.set_line_width(1)
	# 	self.cell(title_w, 10, title, border=False, align="C")
	# 	self.ln(14)


	def chapter_body(self, name) -> None:
		try:
			with open(name, "rb") as fh:
				txt = fh.read().decode("latin-1")
				self.set_font("times", "", 12)
				self.multi_cell(0, 5, txt)
		except PermissionError:
			print("Permission denied"); return
