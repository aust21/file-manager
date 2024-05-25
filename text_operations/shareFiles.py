import sys, os
sys.path.append(os.getcwd())
from modules import *
import ShareFileHandler as sh

layout = Layout()
console = Console(height = 17)

def app_layout(message, warning, instuctions) -> None:
	layout.split_column(
		Layout(Panel(message, title="Share files locally")),
		Layout(name = "bottom"),
	)

	layout["bottom"].split_row(
	    Layout(Panel(warning, title="WARNING")),
	    Layout(Panel(instuctions, title="Instuction")),
	)
	layout["bottom"].size = 11
	console.print(layout)


def warning_message():
    return "Use this feature with people you trust. Make sure that they"\
     "access the files they need. Please read the instructions carefully!"\
     " Hold down 'Crtl' key and press 'c' on your keybord when you are done."


def instuctions_text():
    return ""


def share():
    print("Running local share..... in insecure mode, lol")
    try:
        sh.runServer()
    except KeyboardInterrupt:
        print("lol bye....")


if __name__ == "__main__":
    warning = warning_message()
    instuctions = instuctions_text()
    app_layout("The unsecure way to share files", warning, instuctions)
    share()
