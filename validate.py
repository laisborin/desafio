#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

class Validate:

	def get_str_number(data_in):
		return re.search(r'\d+', data_in).group()

	def is_number(data_in):
		return True