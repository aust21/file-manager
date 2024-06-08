import sys, os
from fpdf import FPDF
sys.path.append(os.getcwd())
from modules import *
import text_operations.search_file as sf
import text_operations.pdf_handler as pdf


def welcome_console(title, message, commands, actions) -> None:
	layout = Layout()
	console = Console(height=7)
	layout.split_column(
		Layout(Panel(message, title=title, subtitle="")),
		Layout(name = "bottom")
	)

	layout["bottom"].split_row(
		Layout(Panel(commands, title="Commands")),
		Layout(Panel(actions, title="Actions"))
	)

	console.print(layout)


def writing_layout(message, empty_file, not_empty_file) -> None:

	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

	layout = Layout()
	console = Console(height=10)
	new_message = "The file will be saved in the FileManager folder in documents"
	layout.split_column(
		
		Layout(Panel(new_message, title="File Location", subtitle="")),
		Layout(name = "bottom")
	)

	layout["bottom"].split_row(
		Layout(Panel(empty_file, title="Creating an empty file")),
		Layout(Panel(not_empty_file, title="Creating and adding text to a new file"))
	)
	layout["bottom"].size = 7
	console.print(layout)


def set_path() -> str:

	if platform.system() == "Linux":
		return f"/home/{os.getenv('USERNAME')}/Documents/FileManager/"
	return f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager\\"


def create_file_manager_dir(path) -> None:

	if not os.path.exists(path):
		os.mkdir(path)


def take_file_name() -> str:

	name = input("Enter file name: ").lower()
	if name.endswith(".txt") or name.endswith(".pdf"):
		return name
	print("Name must end with .pdf or .txt")
	return ""


def extract_file_type(file_name) -> str:

	return file_name.split(".")[1]


def type_of_operation_you_want_to_perform() -> str:

	operation = input("What would you like to do? Enter c to "\
				   "create a new file, or cw to create and add text to the file: ")
	return operation


def take_file_kind() -> str:

	kind_of_file = input("Enter the kind of file you are creating: i.e invoice, notes: ")
	return kind_of_file


def take_purpose_of_file() -> str:

	purpose = input("What is the file intended for? i.e school, work or personal? ")
	return purpose


def combine_paths(purpose_path, path) -> str:

	if not os.path.exists(f"{path}{purpose_path}"):
		os.mkdir(f"{path}{purpose_path}")
	sys_path = path+purpose_path
	slash = "/" if platform.system() == "Linux" else "\\"
	comb_path = sys_path+slash
	# print(comb_path)

	return comb_path

def set_path_of_file(path, file_kind) -> None:

	if not os.path.exists(f"{path}{file_kind}"):
		os.mkdir(f"{path}{file_kind}")
	sys_path = path+file_kind
	slash = "/" if platform.system() == "Linux" else "\\"
	file_path = sys_path+slash
	return file_path


def write_to_txt(file, path) -> None:

	with open(f"{path}{file}", 'w') as fl:
		print("Enter the file contents (Press enter on an empty line when you are done)")
		while True:
			content = input()
			if not content:
				break
			fl.write(content + "\n\n")


def write_to_pdf(file, path) -> None:

	with open(f"{path}{file.split('.')[0]}.txt", 'w') as fl:
		print("Enter the file contents (Press enter on an empty line when you are done)")
		while True:
			content = input()
			if not content:
				break
			fl.write(content + "\n\n")

	if platform.system() == "Linux":
		output = f"{path}{file}"
		chaper_body = f"{path}/{file[:-4]}.txt"
	else:
		output = f"{path}\\{file}"
		chaper_body = f"{path}\\{file[:-4]}.txt"

	create_file_body = pdf.PDF("P", "mm", "Letter")
	create_file_body.set_auto_page_break(auto = True, margin = 15)
	create_file_body.add_page()
	create_file_body.chapter_body(chaper_body)
	create_file_body.output(output)
	os.remove(chaper_body)
	print(f"File created at location: {output}")


def create_pdf(path, name):

	if platform.system() == "Linux":
		output = f"{path}{name}"
	else:
		output = f"{path}\\{name}"

	create_file_body = pdf.PDF("P", "mm", "Letter")
	create_file_body.add_page()
	create_file_body.output(output)


def what_to_perform(operation, file_name, file_type, path):

	if operation == "c" and file_type == "txt":
		file = open(f"{path}{file_name}", 'w')
		file.close()
	elif operation == "c" and file_type == "pdf":
		create_pdf(path, file_name)
	elif operation == "cw" and file_type == "txt":
		write_to_txt(file_name, path)
	elif operation == "cw" and file_type == "pdf":
		write_to_pdf(file_name, path)


def empty_file_creation_instructions() -> str:
	return "1. To create an empty file just enter 'c' press enter.\n"\
		"2. Wait for the window to pop up to reveal your file\n"\
		"3. Edit the file...."


def not_empty_file_instructions() -> str:
	return "1. To create and add text to the file, enter 'cw' and you will"\
				"be prompted to enter the contents of the file\n"\
		"2. To enter a new paragraph, press the enter key only one and continue typing.\n"\
		"3. To exit and save the file press the enter key twice."


def get_commands() -> str:
	return "1. c \n"\
		"2. cw "


def get_actions() -> str:
	return "1. create a new file\n"\
		"2. create and add text to the file"


def main() -> None:
	message = "You can create a new empty file or create and add text to the file"
	commands = get_commands()
	actions = get_actions()
	welcome_console("Create and Write files", message, commands, actions)

	# setting path
	system_path = set_path()
	root_path = create_file_manager_dir(system_path)

	purpose = take_purpose_of_file()
	file_path = combine_paths(purpose, system_path)
	# print(f"file path {file_path}")

	#
	file_name = take_file_name()
	file_kind = take_file_kind()
	writing_layout(message, empty_file_creation_instructions(), not_empty_file_instructions())
	final_path = set_path_of_file(file_path, file_kind)

	operation = type_of_operation_you_want_to_perform()
	file_type = extract_file_type(file_name)
	# print(file_name)
	what_to_perform(operation, file_name, file_type, final_path)



if __name__ == "__main__":
	main()
