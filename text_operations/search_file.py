import sys, os
from halo import Halo
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.layout import Layout

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
	if file_name.endswith(".pdf") or file_name.endswith(".txt"):
		return file_name
	print("File name should end with `.pdf` or `.txt`")


def file_input_instructions() -> str:
	return "\n\nEnter file name below. The file name must end with .pdf or .txt"\
		" and it must be prefixed with the kind of file it is.\nIf its an invoice,"\
		" you can enter something like: invmyinvoice.pdf\nThe first bit `inv` indicates"\
		" that the file is an invoice and should be stored in the invoice(inv) folder\n"\
		"The second bit `myinvoice` is the name of the file\nThe last bit `.pdf` is the file type."


def find_file(file_name, search_path) -> tuple[bool, str]:
	for root, dirs, files in os.walk(search_path):
		if file_name in files:
			return True, os.path.join(root, file_name)
	return False, ""



if __name__ == "__main__":
	instructions = file_input_instructions()
	display_messages(instructions)
	file_name = take_filename()
	file_path = find_file(file_name, "C:\\")
	if find_path[0]:
		print(f"file found in {find_file[1]}")
