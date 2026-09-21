"""Serve only the Odyssey app on localhost so Google accepts browser imports."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

# Support both "Odyssey new version.html" and "Odyssey new version (1).html"
for _name in ("Odyssey new version.html", "Odyssey new version (1).html"):
    _p = Path(__file__).with_name(_name)
    if _p.exists():
        APP = _p
        break
else:
    APP = Path(__file__).with_name("Odyssey new version.html")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?", 1)[0] not in ("/", "/index.html"):
            self.send_error(404)
            return
        body = APP.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
        url = f"http://127.0.0.1:{server.server_port}/"
        print(f"Odyssey is running at {url}", flush=True)
        webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
