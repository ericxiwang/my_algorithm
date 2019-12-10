""" Write a Python script (or using another script language) that
reads a text string as input,
counts the number of spaces (blank characters) in the input string, and
prints out the count.
"""
import os
class raw_input:
	def __init__(self):
		self.input_string=""
	def getRawInput(self):

		self.input_string = raw_input()

	def select_spaces(self):
		count_space = 0
		for i in self.input_string:
			if i.isspace():
				count_space+=1
		return count_space


if __name__ == '__main__':
	a= "a a a bb  a a a a"
	b = a.count(" ")
	c = set(a)
	c = "".join(c)
	print c


