import sys, os
sys.path.append(os.getcwd())
from modules import *
import operations.search_file as sf


layout = Layout()
console = Console()


def display_content(text, file_name):
	layout.split_column(
		Layout(Panel(text, title=file_name))
	)

def show_file_contents(file_exists, file_path, file_name) -> None:
	if file_exists:
		sf.pop_up("File found.", "File Manager | View File")
		with open(file_path, "r") as fl:
			content = fl.readlines()
			text = "".join(content)
			display_content(text, file_name)
			required_height = text.count('\n')+2
			console.height = required_height
			console.print(layout)
	else:
		sf.pop_up("File not found.", "File Manager | View File")
		print("Cannot open the file, make sure it exists.")


def sys_path() -> None:
	username = os.getenv("USERNAME")
	if platform.system() == "Linux":
		return f"/home/{username}/"
	return f"C:\\Users\\{username}\\"


def main(file_name):
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	path = sys_path()
	file_exists, file_path = sf.find_file(file_name, path)
	show_file_contents(file_exists, file_path, file_name)