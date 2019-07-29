#!/usr/bin/env python3

# Set path to import "qppserver" modules
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "appserver"


from appserver.server import Server
import requests as req
import unittest
import json

class TestServer(unittest.TestCase):

	"""
		First start server, run $ python3 start_server.py
		So, run this test case 
	"""
		
	def test_GET(self):
		resp = req.get("http://localhost:3000/1")
		self.assertEqual(resp.json(), {'extenso': 'um'})

		resp = req.get("http://localhost:3000/abc")
		self.assertEqual(resp.json(), {'ERROR': 'enter a number in [-99999, 99999] range'})

		resp = req.get("http://localhost:3000/-10")
		self.assertEqual(resp.json(), {'extenso': 'menos dez'})

		resp = req.get("http://localhost:3000/-1000")
		self.assertEqual(resp.json(), {'extenso': 'menos mil'})


if __name__ == '__main__':
    unittest.main()