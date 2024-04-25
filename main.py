from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout

layout = Layout()
console = Console(height = 25)

def app_layout(title, subtitle, message, commands, actions):
	layout.split_column(
		Layout(Panel(message, title="File Manager", subtitle="By Austin")),
		Layout(name = "bottom"),
	)

	layout["bottom"].split_row(
	    Layout(Panel(commands, title="Commands")),
	    Layout(Panel(actions, title="Action")),
	)
	# layout["top"].size = 5
	layout["bottom"].size = 20
	console.print(layout)

def file_actions():
	return "actions"


def valid_commands():
	return "commands"
# 	return """Command                       Action
# -------------------------------------------------------------------
# -> open <filename>                  opens file
# -> create <filename>                creates and write to a new file
# -> read <filename>                  reads out file contents
# -------------------------------------------------------------------
# -------------------------------------------------------------------"""


if __name__ == "__main__":
	message = "\nWelcome to file manager, the all you need file management tool for easy file operations\n"
	title = "File Manager"
	subtitle = "Thank you for choosing File Manager"
	commands = valid_commands()
	actions = file_actions()
	app_layout(title, subtitle, message, commands, actions)
	# commands()
