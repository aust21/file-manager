import sys, os
from halo import Halo
from rich.console import Console
from rich.table import Table

console = Console()

def take_filename() -> str:

	table = Table(show_header = True, header_style="bold magenta")
	table.add_column("Welcome to file manager", justify="center")
	table.add_row("Enter file name below. The file name must end with .pdf or .txt")
	console.print(table)
	# print("Enter file name below. The file name must end with .pdf or .txt"\
	#  " and it must be prefixed with the kind of file it is.\nIf its an invoice,"\
	#  " you can enter something like: invmyinvoice.pdf\nThe first bit `inv` indicates"\
	#  " that the file is an invoice and should be stored in the invoice(inv) folder\n"\
	#  "The second bit `myinvoice` is the name of the file\nThe last bit `.pdf` is the file type.")
	file_name = input()
	if file_name.endswith(".pdf") or file_name.endswith(".txt"):
		return file_name
	print("File name should end with `.pdf` or `.txt`")


@Halo(text="This may take a while...Super highly advanced virtual bots are searching for your file :)")
def find_file(file_name, search_path) -> tuple[bool, str]:
	for root, dirs, files in os.walk(search_path):
		if file_name in files:
			return True, os.path.join(root, file_name)
	return False, ""

	

if __name__ == "__main__":
	file_name = take_filename
	file_path = find_file(file_name, "C:\\")
	if find_path[0]:
		print(f"file found in {find_file[1]}")
