#!/usr/bin/env python3

from server import Server
from http.server import BaseHTTPRequestHandler, HTTPServer

"""
	Start server implemented in server.py
"""

try:
    print('starting server on port 3000...')
    server_address = ('', 3000)
    server = HTTPServer(server_address, Server)
    print('SERVER ON!\nType Ctrl+C to shut down.')
    server.serve_forever()

except KeyboardInterrupt:
	print('\nshutting down the web server')
	server.socket.close()