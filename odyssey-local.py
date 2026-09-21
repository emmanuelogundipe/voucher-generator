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
    import os

    # Render sets PORT env var; locally use random free port
    port = int(os.environ.get("PORT", "0"))
    host = "0.0.0.0" if "PORT" in os.environ else "127.0.0.1"
    bind_port = port if port != 0 else 0

    with ThreadingHTTPServer((host, bind_port), Handler) as server:
        actual_port = server.server_port
        if "PORT" in os.environ:
            print(f"Odyssey is running on port {actual_port}", flush=True)
        else:
            url = f"http://127.0.0.1:{actual_port}/"
            print(f"Odyssey is running at {url}", flush=True)
            try:
                webbrowser.open(url)
            except Exception:
                pass
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
