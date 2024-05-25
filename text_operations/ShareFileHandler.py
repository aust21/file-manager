import http.server
import socketserver
import socket
import search_file as sf
import time
import subprocess

PORT = 8000
DIRECTORY = "C:\\Users\\Austin\\"


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

def get_filename():
    name = input("Enter the file name: ")
    return name

def get_file_path():
    path = input("Do you know where the file is located? ")
    if path == "yes":
        true_path = input(f"Enter the path: {DIRECTORY}")
        return DIRECTORY+true_path
    print("No worries...")
    time.sleep(2)
    print(f"Preparing to search for your file...")
    time.sleep(2)
    return False


def main():
    ip = get_address()
    name = get_filename()
    path = get_file_path()
    if not path:
        real_path = sf.find_file(name, "C:\\")
    if real_path[0]:
        print("File found....The file explorer will open for you to confirm the file")
        time.sleep(3)
        subprocess.Popen(fr'explorer /select,"{real_path[1]}"')
        confirm = input("Please confirm this is the file you want to share: [y or n]: ")
        if confirm == "y":
            print("Okay")
            time.sleep(2)
            print()
            runServer(ip, real_path[1])
    else:
        print("File not found.")

if __name__ == "__main__":
    main()
