#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from word_param import HangmanGame
import json

class GameControl(object):
    def __init__(self):
        self.status = None
        self.word = None
        self.myobj = HangmanGame()

    def newGame(self):
        self.word = self.myobj.get_word()
        self.status = 'Playing'

    def continueGame(self, key=None):
        if self.myobj.word == self.myobj.display:
            print 'Game Won'
        else:
            self.myobj.hand(key)
            print 'Made a Guess'

gc = GameControl()

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.path == '/newGame':
            gc.status = None
        self._set_headers()
        if gc.status == None:
            gc.newGame()
        f = open('buffer.html')
        self.send_response(200)
        self.send_header('Content-type',    'text/html')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        if self.path == '/guessAlpha':
            content_len = int(self.headers.getheader('content-length'))
            post_body = self.rfile.read(content_len)
            gc.continueGame(post_body[-1])
            f = open('buffer.html')
            self.send_response(200)
            self.send_header('Content-type',    'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=4242)
