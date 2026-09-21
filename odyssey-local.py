"""Serve only the Odyssey app on localhost so Google accepts browser imports."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

# Support both "Odyssey new version.html" and "Odyssey new version (1).html" and Hope V2
for _name in ("Odyssey new version.html", "Odyssey new version (1).html"):
    _p = Path(__file__).with_name(_name)
    if _p.exists():
        APP = _p
        break
else:
    APP = Path(__file__).with_name("Odyssey new version.html")

HOPE_V2 = Path(__file__).with_name("Hope Voucher v2.html")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        # Decode URL
        import urllib.parse, os
        path = urllib.parse.unquote(path)
        # On Render (PORT set), serve Hope V2 as default
        is_render = "PORT" in os.environ
        if path in ("/v2", "/v2/", "/hope", "/hope-v2", "/Hope Voucher v2.html", "/Hope%20Voucher%20v2.html"):
            if HOPE_V2.exists():
                body = HOPE_V2.read_bytes()
            else:
                self.send_error(404)
                return
        elif path in ("/", "/index.html"):
            if is_render and HOPE_V2.exists():
                body = HOPE_V2.read_bytes()
            else:
                body = APP.read_bytes()
        elif path in ("/Odyssey new version.html", "/Odyssey new version (1).html"):
            body = APP.read_bytes()
        else:
            # Try to serve any html file in folder safely
            safe = Path(__file__).with_name(path.lstrip("/"))
            try:
                # prevent directory traversal
                safe.resolve().relative_to(Path(__file__).parent.resolve())
                if safe.exists() and safe.suffix.lower() == ".html":
                    body = safe.read_bytes()
                else:
                    self.send_error(404)
                    return
            except Exception:
                self.send_error(404)
                return
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
