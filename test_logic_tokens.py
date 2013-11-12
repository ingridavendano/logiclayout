# -----------------------------------------------------------------------------
# test_logic_tokens.py
# Created by Ingrid Avendano 11/11/13.
#
# Test that boolean algebra tokens are tokenized properly.
# -----------------------------------------------------------------------------


from logic_tokens import *
import ply.yacc as yacc
import unittest

class TestLogicTokens(unittest.TestCase):

	def test_binary(self):
		""" Test if binary expressions work. """

		variables = {
			"0": "0b0",
			"1": "0b1",
			"42": "0b101010", 
			"0b1101": "0b1101",
			"FALSE": "0b0", 
			"true": "0b1",
		}

		for variable, result in variables.iteritems():
			print variable, "->", result
			yacc.parse(variable)

			print "found_result",type(OUTPUT), OUTPUT
			print "result",type(result), result
			self.assertEqual(OUTPUT, result)

if __name__ == '__main__':
	yacc.yacc()
	unittest.main()
