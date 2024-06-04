import sys, os
sys.path.append(os.getcwd())
from modules import *

layout = Layout()
console = Console(height = 12)

def display_messages(instructions) -> None:
	layout.split_column(
		Layout(Panel("\nSearch and Locate files on your pc....\n", title="Search & Locate")),
		Layout(name = "Stuff")
	)

	layout["Stuff"].split_row(
		Layout(Panel("\nEnter a valid file name, the file must be a pdf or txt format", title="File Format")),
		Layout(Panel(instructions, title = "input Instructions"))
	)

	layout["Stuff"].size = 8
	console.print(layout)


def take_filename() -> str:
	file_name = input("Enter file name: ")
	return file_name


def validate_filename(file_name) -> bool:
	if file_name.endswith(".pdf") or file_name.endswith(".txt"):
		return True
	print("File name should end with `.pdf` or `.txt`")
	return False


def file_input_instructions() -> str:
	return "\n\nEnter file name below. The file name must end with .pdf or .txt"\
		" and it must be prefixed with the kind of file it is.\nIf its an invoice,"\
		" you can enter something like: invmyinvoice.pdf\nThe first bit `inv` indicates"\
		" that the file is an invoice and should be stored in the invoice(inv) folder\n"\
		"The second bit `myinvoice` is the name of the file\nThe last bit `.pdf` is the file type."


def search_instructions() -> str:
	return "\nEnter file name below. If the file is found a path to the file will be "\
		"displayed and the file explorer will be automatically opened."\
		"For your safety, this feature on windows only searches beyond Users directory"


def find_file(file_name, search_path) -> tuple[bool, str]:
	print("This process may take a while....")
	for root, dirs, files in tqdm(os.walk(search_path), desc="Searching"):
		if file_name in files:
			return True, os.path.join(root, file_name)
	return False, ""


def sys_path() -> None:
	username = os.getenv("USERNAME")
	if platform.system() == "Linux":
		return f"/home/{username}/"
	return f"C:\\Users\\{username}\\"


def open_files(file_path) -> None:
	if platform.system() == "Windows":
		subprocess.Popen(fr'explorer /select,"{file_path}"')
	elif platform.system() == "Linux":
		try:
			subprocess.Popen(["nautilus", "--select", file_path])
		except FileNotFoundError:
			try:
				subprocess.Popen(["thunar", "--select", file_path])
			except FileNotFoundError:
				try:
					subprocess.Popen(["dolphin", "--select", file_path])
				except FileNotFoundError:
					print("No supported file manager found. Please install nautilus, thunar, or dolphin.")


def main() -> None:
	instructions = search_instructions()
	display_messages(instructions)
	file_name = take_filename()
	path = sys_path()
	find_path = find_file(file_name, path)
	if find_path[0]:
		print("Opening explorer")
		time.sleep(3)
		open_files(find_path[1])
	else:
		print("File not found, please make sure it exists")


if __name__ == "__main__":
	main()