from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout

layout = Layout()
console = Console(height = 25)

def app_layout(title, subtitle, message, commands, actions) -> None:
	layout.split_column(
		Layout(Panel(message, title="File Manager", subtitle="Thank you for choosing File Manager")),
		Layout(name = "bottom"),
	)

	layout["bottom"].split_row(
	    Layout(Panel(commands, title="Commands")),
	    Layout(Panel(actions, title="Action")),
	)
	layout["bottom"].size = 20
	console.print(layout)

def file_actions() -> str:
	return "actions"


def valid_commands():
	return ""\
	"\nedt filename       | edit an existing file\n"\
	"crt filename       | create a new file\n"\
	"luk filename       | look for a file\n"\
	"shr filename email | send file to email\n\n"\


if __name__ == "__main__":
	message = "\nWelcome to file manager, the all you need file management tool for easy file operations\n"
	title = "File Manager"
	subtitle = "Thank you for choosing File Manager"
	commands = valid_commands()
	actions = file_actions()
	app_layout(title, subtitle, message, commands, actions)
	# commands()
