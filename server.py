#!/usr/bin/env python3

import json
from validate import Validate
from translate import Translate
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		
		# check if is a valid number
		if Validate().is_number(self.path):
			str_number = Validate().get_str_number(self.path)

			# if true, translate it
			message = Translate().get_extenso(str_number)
			out = json.dumps({'extenso': message})
		
		else:
			# if false, report an error
			out = json.dumps({'ERROR': 'enter a number in [-99999, 99999] range'})
		
		# return json
		self.wfile.write(out.encode())
		return


def main():

	try:
	    print('starting server on port 3000...')
	    server_address = ('', 3000)
	    server = HTTPServer(server_address, MyHandler)
	    server.serve_forever()
	except KeyboardInterrupt:
		print(' shutting down the web server')
		server.socket.close()

main()