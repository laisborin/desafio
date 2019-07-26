#!/usr/bin/env python3

class Translate:

	# sorted to access by index
	number_names = (
                     ('',"um","dois","três","quatro","cinco","seis","sete","oito","nove"),
                     ("dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove"),
                     ('', '', "vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"),
                     ('',"cento","duzentos","trezentos","quatrocentos","quinhentos","seiscentos","setecentos","oitocentos", "novecentos")
                     )

	def get_decimals(self, decimal):
		return self.number_names[0][int(decimal)]

	def get_hundreds(self, hundred):
		return self.number_names[3][int(hundred)]

	def get_dozens(self, dozen):
		if dozen[0] == '1':
			return self.number_names[1][int(dozen[1])] # special case dozens < 20
	
		out = []
		out.append(self.number_names[2][int(dozen[0])])
		if dozen[1] != '0':
			out.append(self.get_decimals(dozen[1]))

		# suppress zero occurrences
		try:
			out.remove('')
		except:
			pass			

		return ' e '.join(out)

	def translate(self, part):
		"""
			Translates a number by its length
		"""
		len_p = len(part)

		out = []

		if len_p == 1:
			out.append(self.get_decimals(part))

		elif len_p == 2:
			out.append(self.get_dozens(part))
		else:
			# special case of hundreds
			if part == '100':
				return 'cem'

			out.append(self.get_hundreds(part[0]))
			out.append(self.get_dozens(part[1:3]))

			# suppress zero occurrences
			try:
				out.remove('')
			except:
				pass			

		return ' e '.join(out)

	def split_string(self, str_number):
		"""
			Splits str_number into parts of at least 3 numbers from the end of str_number
			Return a part or two parts in reverse order
		"""
		split = []

		len_n = len(str_number)

		if len_n <= 3:
			split.append(str_number)
		else:
			split.append(str_number[len_n-3:len_n]) # take the last part
			split.append(str_number[0:len_n-3]) # and the first part

		return split

	def get_extenso(self, str_number):

		sinal = ''
		f_part = ''
		l_part = ''

		# negative number
		if str_number[0] == '-':
			sinal += 'menos '
			str_number = str_number.lstrip('-')

		# remove left zeros
		str_number = str_number.lstrip('0')
		if len(str_number) == 0:
			return "zero"

		# split string to identify the right way to translate it
		str_split = self.split_string(str_number)

		# inverse number parts
		for part in range(0, len(str_split)):

			# translates each part
			out = self.translate(str_split[part])

			# last part
			if part == 0:
				l_part = out
				# if there are two parts and last part is > 0, insert 'e'
				if len(str_split) > 1 and str_split[0] != '000':
					l_part = 'e '+ l_part
			
			# there are two parts, so insert 'mil'
			else:
				# don't use 'um' followed by 'mil'
				if out != 'um':
					f_part = out + ' '
				f_part += 'mil '


		return sinal + f_part + l_part
