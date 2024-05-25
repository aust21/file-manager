import sys, os
sys.path.append(os.getcwd())
from modules import *
from center_text import *
import ShareFileHandler as sh

layout = Layout()
console = Console(height = 20)

def app_layout(message, warning, instuctions) -> None:
	layout.split_column(
		Layout(Panel(message, title="Share files locally")),
		Layout(name = "bottom"),
	)

	layout["bottom"].split_row(
	    Layout(Panel(warning, title="WARNING")),
	    Layout(Panel(instuctions, title="Instuction")),
	)
	layout["bottom"].size = 15
	console.print(layout)


def warning_message():
    return "Use this feature with people you trust. Make sure that they "\
     "access the files they need. Please read the instructions carefully!"\
     " Hold down 'Crtl' key and press 'c' on your keybord when you are done."


def instuctions_text():
    return "What you must do:\n1. Make sure that this computer and the device you want to share the "\
        "file with are connected to the same network.\n"\
        f"2. Share the this address `{sh.get_address()}` with the person you want to share with.\n"\
        "3. Hold 'Crtl' key and press letter 'c' on your keybord to close the sharing when you are done\n\n"\
        "What the reciever must do:\n1. Open the browser\n"\
        f"2. Enter `{sh.get_address()}:8000` in the search bar.\n"\
        "3. Download the files they need.\n"\
        "Simple... isn't?"


def share():
    try:
        sh.main()
    except KeyboardInterrupt:
        print("lol bye....")


if __name__ == "__main__":
    warning = warning_message()
    instuctions = instuctions_text()
    app_layout("\n"+center("The insecure way to share files"), warning, instuctions)
    share()
