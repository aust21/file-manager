import sys, os
from fpdf import FPDF
sys.path.append(os.getcwd())
import text_operations.search_file as sf
import text_operations.pdf_handler as pdf

def set_path() -> str:
	return f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\.FileManager"


def create_file_manager_dir(path) -> None:
	if not os.path.exists(path):
		os.mkdir(path)


def create_txt_read_file(file_name, file_type, path) -> None:
	with open(f"{path}\\{file_name.split('.')[0]}.txt", 'w') as fl:
		print("Enter the file contents (Press enter on an empty line when you are done)")
		while True:
			content = input()
			if not content:
				break
			fl.write(content + "\n\n")


def extract_extension(file_name) -> str:
	return file_name.split(".")[1]


def write_to_file(valid_name, content, path) -> None:
	print(valid_name)
	if not valid_name:
		print("Invalid file name.")
	else:
		create_file_body = pdf.PDF("P", "mm", "Letter")
		create_file_body.set_auto_page_break(auto = True, margin = 15)
		create_file_body.add_page()
		create_file_body.chapter_body(f"{path}\\{valid_name[:-4]}.txt")
		create_file_body.output(f"{path}\\{valid_name}")
		print("File created")


def main(valid_name) -> None:
	path = set_path()
	create_file_manager_dir(path)
	file_type = extract_extension(file_name)
	text_format = create_txt_read_file(file_name, file_type, path)
	if file_type == "pdf":
		write_to_file(valid_name, f"{path}\\{valid_name.split('.')[0]}.txt", path)


if __name__ == "__main__":
	file_name = sf.take_filename()
	if file_name:
		main(file_name)
