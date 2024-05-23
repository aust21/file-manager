import sys, os
sys.path.append(os.getcwd())
from modules import *
import text_operations.search_file as sf


layout = Layout()
# console = Console(height = 12)


def display_content(text, file_name):
	layout.split_column(
		Layout(Panel(text, title=file_name))
	)

def show_file_contents(file_exists, file_path) -> None:
	if file_exists:
		with open(file_path, "r") as fl:
			content = fl.readlines()
			display_content("".join(content), file_name)
			console.print(layout)
	else:
		print("Cannot open the file, make sure it exists.")


if __name__ == "__main__":
	file_name = sf.take_filename()
	file_exists, file_path = sf.find_file(file_name, "C:\\")
	show_file_contents(file_exists, file_path)
