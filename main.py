from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout

layout = Layout()
console = Console(height = 17)

def app_layout(title, subtitle, message, commands, actions) -> None:
	layout.split_column(
		Layout(Panel(message, title="File Manager", subtitle="Thank you for choosing File Manager")),
		Layout(name = "bottom"),
	)

	layout["bottom"].split_row(
	    Layout(Panel(commands, title="Commands")),
	    Layout(Panel(actions, title="Action")),
	)
	layout["bottom"].size = 11
	console.print(layout)

def file_actions() -> str:
	return ""\
	"\nEdit an existing file\n\n"\
	"Create a new file\n\n"\
	"Look for a file and return the path to the file\n\n"\
	"Send file to email\n\n"


def valid_commands() -> str:
	return ""\
	"\nedt filename\n\n"\
	"crt filename\n\n"\
	"luk filename\n\n"\
	"shr filename email\n\n"\


if __name__ == "__main__":
	message = "\nWelcome to file manager, the all you need file management tool for easy file operations\n"
	title = "File Manager"
	subtitle = "Thank you for choosing File Manager"
	commands = valid_commands()
	actions = file_actions()
	app_layout(title, subtitle, message, commands, actions)
