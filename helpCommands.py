from modules import *

layout = Layout()
console = Console(height = 22)

def app_layout(title, subtitle, message, commands, actions) -> None:
	layout.split_column(
		Layout(Panel(message, title="File Manager", subtitle="V1.1.3")),
		Layout(name = "bottom"),
	)

	layout["bottom"].split_row(
	    Layout(Panel(commands, title="Commands")),
	    Layout(Panel(actions, title="Action")),
	)
	layout["bottom"].size = 17
	console.print(layout)

def file_actions() -> str:
	return ""\
	"\nView program information\n\n"\
	"Create a new empty file or add text to a new file\n\n"\
	"Look for a file\n\n"\
	"Send file through browser\n\n"\
	"Remove a file\n\n"\
	"View a file\n\n"\
	"Organize files in a folder\n\n"


def valid_commands() -> str:
	return ""\
	"\nfilemanager\n\n"\
	"filemanager write filename\n\n"\
	"filemanager search filename\n\n"\
	"filemanager share filename\n\n"\
	"filemanager remove filename\n\n"\
	"filemanager view filename\n\n"\
	"filemanager tidy folder\n\n"\


def entry():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	message = "\nWelcome to file manager, the all you need file management tool for easy file operations\n"
	title = "File Manager"
	subtitle = "Thank you for choosing File Manager"
	commands = valid_commands()
	actions = file_actions()
	app_layout(title, subtitle, message, commands, actions)