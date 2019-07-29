
# Set path to import "qppserver" modules
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "appserver"



from appserver.validate import Validate
import unittest

class TestValidade(unittest.TestCase):

	def test_is_number(self):
		val = Validate()
		self.assertEqual(val.is_number("10"), True)
		self.assertEqual(val.is_number("-250"), True)
		self.assertEqual(val.is_number("2501"), True)
		self.assertEqual(val.is_number("25001"), True)
		self.assertEqual(val.is_number("99999"), True)
		self.assertEqual(val.is_number("-99999"), True)

		self.assertEqual(val.is_number("25as"), False)
		self.assertEqual(val.is_number("-25as"), False)
		self.assertEqual(val.is_number("/25as"), False)
		self.assertEqual(val.is_number("25.as"), False)
		self.assertEqual(val.is_number("100000"), False)
		self.assertEqual(val.is_number("-100000"), False)


if __name__ == '__main__':
    unittest.main()