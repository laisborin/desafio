#!/usr/bin/env python3

import requests as req
import json

while True:
	url = input()

	try:
		resp = req.get('http://localhost:3000/'+url)
		print(resp.json())
	except:
		print('ERROR : enter http://localhost:3000/ following by a number; \nCheck if server is on!')