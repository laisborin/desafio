#!/usr/bin/env python3

import re

class Validate:

	def get_str_number(self, data_in):
		return re.search(r'-?\d+', data_in).group()

	def is_number(self, data_in):
		return True