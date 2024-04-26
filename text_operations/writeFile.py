import sys, os
from fpdf import FPDF
sys.path.append(os.getcwd())
import text_operations.search_file as sf
import text_operations.pdf_handler as pdf

def set_path() -> str:
	return f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager"


def create_file_manager_dir(path) -> None:
	if not os.path.exists(path):
		os.mkdir(path)


def create_sub_directory(file_name, path):
	if not os.path.exists(f"{path}\\{file_name[:3]}"):
		os.mkdir(f"{path}\\{file_name[:3]}")
	return file_name[3:], f"{path}\\{file_name[:3]}"


def create_txt_read_file(file_name, file_type, sub_dir) -> None:
	with open(f"{sub_dir}\\{file_name.split('.')[0]}.txt", 'w') as fl:
		print("Enter the file contents (Press enter on an empty line when you are done)")
		while True:
			content = input()
			if not content:
				break
			fl.write(content + "\n\n")


def extract_extension(file_name) -> str:
	return file_name.split(".")[1]


def write_to_file(file_name, content, sub_dir) -> None:
	print(file_name)
	if not file_name:
		return "Invalid file name."

	create_file_body = pdf.PDF("P", "mm", "Letter")
	create_file_body.set_auto_page_break(auto = True, margin = 15)
	create_file_body.add_page()
	create_file_body.chapter_body(f"{sub_dir}\\{file_name[:-4]}.txt")
	create_file_body.output(f"{sub_dir}\\{file_name}")
	return "File created."


def main(valid_name) -> None:
	path = set_path()
	file_name, sub_dir = create_sub_directory(valid_name, path)
	create_file_manager_dir(path)
	file_type = extract_extension(file_name)
	text_format = create_txt_read_file(file_name, file_type, sub_dir)
	if file_type == "pdf":
		write_to_file(file_name, f"{sub_dir}\\{file_name.split('.')[0]}.txt", sub_dir)


if __name__ == "__main__":
	file_name = sf.take_filename()
	canContinue = sf.validate_filename(file_name)
	if canContinue:
		main(file_name)
