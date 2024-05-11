import sys, os, time, subprocess
from halo import Halo
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from threading import Thread
from rich.progress import Progress, BarColumn
from tqdm import tqdm

layout = Layout()
console = Console(height = 25)

def display_messages(instructions) -> None:
	layout.split_column(
		Layout(Panel("\nSearch and Locate files on your pc....", title="Search & Locate")),
		Layout(name = "Stuff")
	)

	layout["Stuff"].split_row(
		Layout(Panel("Live search update", title="Search Program")),
		Layout(Panel(instructions, title = "input Instructions"))
	)

	layout["Stuff"].size = 20
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
	return "Enter file name below. If the file is found a path to the file will be "\
		"displayed and the file explorer will be automatically opened."


def discover_file_number(dir):
	count = 0
	for file in tqdm(os.listdir(dir)):
		if os.path.isfile(os.path.join(dir, file)):
			count += 1
	return count


def find_file(file_name, search_path) -> tuple[bool, str]:
	for root, dirs, files in tqdm(os.walk(search_path), desc="Searching"):
		if file_name in files:
			return True, os.path.join(root, file_name)
	return False, ""


if __name__ == "__main__":
	instructions = search_instructions()
	display_messages(instructions)
	file_name = take_filename()
	find_path = find_file(file_name, "C:\\Users\\Austin\\Desktop\\")
	if find_path[0]:
		print("Opening explorer")
		time.sleep(3)
		subprocess.Popen(fr'explorer /select,"{find_path[1]}"')
	else:
		print("File not found, please make sure it exists")
