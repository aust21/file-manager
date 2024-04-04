import sys, os
from fpdf import FPDF
sys.path.append(os.getcwd())
import text_operations.search_file as sf
import text_operations.pdf_handler as pdf

def set_path():
	return f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager"


def create_file_manager_dir(path):
	if not os.path.exists(path):
		os.mkdir(path)

def create_content():
	return input("Enter your file contents (Enter '\n' to go to a new line, \'\n\n' for a new paragraph)\n\n")

def create_txt_read_file(file_name, file_type, content):
	with open(f"{path}\\{file_name}", 'w') as fl:
		fl.write(content)


def write_to_file(valid_name, new_page, content, path):
	create_file_body = pdf.PDF("P", "mm", "Letter")
	create_file_body.set_auto_page_break(auto = True, margin = 15)
	create_file_body.chapter_body(self, content)
	create_file_body.output(f"{path}\\{valid_name}")

file_name = input("Enter file name: ")
path = set_path()
create_file_manager_dir(path)
content = create_content()
create_txt_read_file(file_name, "pdf", content)
