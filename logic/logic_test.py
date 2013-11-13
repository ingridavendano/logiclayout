# -----------------------------------------------------------------------------
# logic_test.py
# Created by Ingrid Avendano 11/12/13.
#
# Test that boolean algebra tokens are tokenized properly.
# -----------------------------------------------------------------------------


import logicgrammar
import logic_lex
# from logictokens import lexer
import unittest

class TestLogicTokens(unittest.TestCase):

	def test_binary(self):
		""" Test if binary expressions work. """

		# variables = {
		# 	"0": "0",
		# 	"1": "1",
		# 	"42": "42", 
		# 	"0b1101": "13",
		# 	"FALSE": "0", 
		# 	"true": "1",
		# }

		# for variable, result in variables.iteritems():
		# 	print variable, "->", result
		# 	logicgrammar.parse(variable)

		# 	self.assertEqual(OUTPUT, result)

		data = ["a=1", "b=0", "c=1", "d=1", "f=[(a*b)+(c*d)]", "f"]
		for d in data:
			print d
			# logicgrammar.parse(d, llex=lexer)
			found_tokens = logic_lex.run_input(d)
			print found_tokens


if __name__ == '__main__':
	unittest.main()
