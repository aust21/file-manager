from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

def welcome(title, subtitle, message):
	print(Panel(message, title=title, subtitle=subtitle))

def commands():
	return """Command                       Action
-------------------------------------------------------------------
-> open <filename>                  opens file
-> create <filename>                creates and write to a new file
-> read <filename>                  reads out file contents
-------------------------------------------------------------------
-------------------------------------------------------------------"""


if __name__ == "__main__":
	message = "\nWelcome to file manager, the all you need file management tool for easy file operations\n"
	title = "File Manager"
	subtitle = "Thank you for choosing File Manager"
	welcome(title, subtitle, message)
	# print(commands())
