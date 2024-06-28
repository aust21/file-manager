
import sys, os
sys.path.append(os.getcwd())
from modules import *
import text_operations.search_file as sf

PORT = 8000


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


def get_address():
    hostname = socket.gethostname()
    LOCAL_IP = socket.gethostbyname(hostname)
    return LOCAL_IP


def runServer(ip, directory):
    print("Running local share..... in insecure mode, lol")
    with socketserver.TCPServer((ip, PORT), MyRequestHandler) as httpd:
        print(f"Serving files from {directory} at http://{ip}:{PORT}")
        httpd.serve_forever()


def main(name):
    global DIRECTORY
    ip = get_address()
    path = sf.find_file(name, sf.sys_path())
    if path[0]:
        file_path = path[1]
        DIRECTORY = os.path.dirname(file_path)
        print("File found....The file explorer will open for you to confirm the file")
        time.sleep(3)
        sf.open_files(path[1])
        confirm = input("Please confirm this is the file you want to share: [y or n]: ")
        if confirm == "y":
            print("Okay")
            time.sleep(2)
            print()
            runServer(ip, path[1])
        else:
            print("Please make sure you enter the correct file name")
    else:
        print("File not found.")