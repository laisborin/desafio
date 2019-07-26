#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import json



while True:
	url = input()

	try:
		resp = req.get('http://localhost:3000/'+url)
		print(resp.text)
	except:
		print('ERROR : enter http://localhost:3000/ following by a number')