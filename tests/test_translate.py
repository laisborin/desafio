#!/usr/bin/env python3

# Set path to import "qppserver" modules
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "appserver"



from appserver.translate import Translate
import unittest

class TestTranslate(unittest.TestCase):

	tran = Translate()

	def test_get_decimals(self):
		self.assertEqual(self.tran._get_decimals("1"), "um")
		self.assertEqual(self.tran._get_decimals("5"), "cinco")
		self.assertEqual(self.tran._get_decimals("9"), "nove")
		self.assertEqual(self.tran._get_decimals('0'), '')

	def test_get_hundreds(self):
		self.assertEqual(self.tran._get_hundreds("0"), "")
		self.assertEqual(self.tran._get_hundreds("1"), "cento")
		self.assertEqual(self.tran._get_hundreds("2"), "duzentos")
		self.assertEqual(self.tran._get_hundreds("9"), "novecentos")

	def test_get_tens(self):
		self.assertEqual(self.tran._get_tens("10"), "dez")
		self.assertEqual(self.tran._get_tens("15"), "quinze")
		self.assertEqual(self.tran._get_tens("20"), "vinte")
		self.assertEqual(self.tran._get_tens("22"), "vinte e dois")
		self.assertEqual(self.tran._get_tens("99"), "noventa e nove")
	
	def test_translate(self):
		self.assertEqual(self.tran._translate("10"), "dez")
		self.assertEqual(self.tran._translate("1"), "um")
		self.assertEqual(self.tran._translate("20"), "vinte")
		self.assertEqual(self.tran._translate("201"), "duzentos e um")
		self.assertEqual(self.tran._translate("999"), "novecentos e noventa e nove")

	# Main method
	def test_get_extenso(self):
		self.assertEqual(self.tran.get_extenso("0"), "zero")
		self.assertEqual(self.tran.get_extenso("10"), "dez")
		self.assertEqual(self.tran.get_extenso("100"), "cem")
		self.assertEqual(self.tran.get_extenso("-1"), "menos um")
		self.assertEqual(self.tran.get_extenso("20"), "vinte")
		self.assertEqual(self.tran.get_extenso("-201"), "menos duzentos e um")
		self.assertEqual(self.tran.get_extenso("1000"), "mil")
		self.assertEqual(self.tran.get_extenso("29000"), "vinte e nove mil")
		self.assertEqual(self.tran.get_extenso("29505"), "vinte e nove mil e quinhentos e cinco")


	def test_split_string(self):
		self.assertEqual(self.tran._split_string("10"), ['10'])
		self.assertEqual(self.tran._split_string("1"), ['1'])
		self.assertEqual(self.tran._split_string("1000"), ['000', '1'])
		self.assertEqual(self.tran._split_string("20001"), ['001', '20'])
		self.assertEqual(self.tran._split_string("98012"), ['012', '98'])


if __name__ == '__main__':
    unittest.main()