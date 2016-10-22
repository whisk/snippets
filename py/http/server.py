#!/usr/bin/env python3

"""
Very simple HTTP server in python.

Usage::
    ./server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
import http.server
import socketserver

class S(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(b"<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(b'{"str": "a string", "int": 123, "float": 123.567}')

def run(server_class=socketserver.TCPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Shutting down')
        httpd.shutdown()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()