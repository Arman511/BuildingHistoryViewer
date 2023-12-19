import http.server
import socketserver
import signal
import sys
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PORT = 8000
HTML_FILE = "index.html"

class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(HTML_FILE):
            print("HTML file modified. Reloading server...")
            restart_server()

def restart_server():
    # Terminate the current server process
    os.kill(os.getpid(), signal.SIGINT)

Handler = http.server.SimpleHTTPRequestHandler

def signal_handler(sig, frame):
    print('Ctrl+C pressed. Shutting down the server...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

event_handler = ReloadHandler()
observer = Observer()
observer.schedule(event_handler, path=".", recursive=False)
observer.start()

while True:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            break

observer.stop()
observer.join()

httpd.server_close()
