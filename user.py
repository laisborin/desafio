#!/usr/bin/env python3

import requests as req
import json

"""
	Implements user example of GET request
	to server started by start_server.py file.
"""
while True:

	# wait a url to server
	url = input()

	try:
		# GET request
		resp = req.get(url)
		# print return
		print(resp.json())
	except:
		print('ERROR : enter http://localhost:3000/ following by a number; \nCheck if server is on!')