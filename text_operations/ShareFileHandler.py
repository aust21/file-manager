import http.server
import socketserver

PORT = 8000
DIRECTORY = "C:\\Users\\Austin\\Desktop"
LOCAL_IP = "192.168.14.130"  # Replace this with your actual local network IP address

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def runServer():
    with socketserver.TCPServer((LOCAL_IP, PORT), MyRequestHandler) as httpd:
        print(f"Serving files from {DIRECTORY} at http://{LOCAL_IP}:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    runServer()
