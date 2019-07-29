#!/usr/bin/env python3

"""
	This class implements data validation.
"""
class Validate:

	def is_number(self, data_in):
		"""
			Checks if data_in is a valid integer number, 
			positive or negative.
			Returns True if is valid.
		"""

		# check if is empty
		if data_in == '':
			return False

		# check if is a negative number and remove '-'
		if data_in[0] == '-':
			data_in = data_in[1:]

		# check if a integer
		if data_in.isdigit():
			if int(data_in) >= -99999 and int(data_in) <= 99999:
				return True

		return False

