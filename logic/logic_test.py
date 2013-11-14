# -----------------------------------------------------------------------------
# logic_test.py
# Created by Ingrid Avendano 11/12/13.
#
# Test that boolean algebra tokens are tokenized properly.
# -----------------------------------------------------------------------------

import lexer
import parser

import unittest

class TestLogicTokens(unittest.TestCase):

	def test_binary(self):
		""" Test if binary expressions work. """


		data = ["a = 0", 
				"b = 1", 
				"c = 1", 
				"d = 0", 
				"f = [(a*b)+(c*d)]", 
				"f", 
				"g = b * c",
				"g"]
		# data = ["f = [(a*b)+(c*d)]"]
# 		data = ["""a = 1
# b = 0"""]

		# data = ["a = 1", "b = 0", "c = a + b", "c"]
		# data = ["a = 1", "b = 0"]
		# data = ["a = 1", "a"]
		node_tokens = []
		found_tokens = []
		for d in data:
			print "*"*10, d
			parser.parse(d, node_tokens)
			# found_tokens += logic_lex.run_input(d)
		
		# print found_tokens



if __name__ == '__main__':
	unittest.main()
