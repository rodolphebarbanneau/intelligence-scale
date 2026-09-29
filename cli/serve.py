"""Serve the static report so a browser can fetch the output JSON locally."""

from __future__ import annotations

import functools
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

from cli.paths import ROOT


def serve(host: str, port: int, open_browser: bool) -> None:
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer((host, port), handler)
    url = f"http://{host}:{port}/"
    print(f"serving {ROOT} at {url}")
    if open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
    finally:
        server.server_close()
