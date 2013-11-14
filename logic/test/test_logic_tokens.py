# -----------------------------------------------------------------------------
# test_logic_tokens.py
# Created by Ingrid Avendano 11/13/13.
#
# Test that boolean algebra tokens are tokenized properly.
# -----------------------------------------------------------------------------

import unittest
import sys

sys.path.insert(0,"..")
from logic_tokens import Token

a = Token("a")
b = Token("b")
c = Token("c")
d = Token("d")
e = Token("e")
f = Token("f")
list_tokens = [a, b, c, d, e, f]

class TestTokens(unittest.TestCase):

	def test_children(self):
		"""> check the relationship of children tokens using '<=' """

		a <= b
		a <= c
		a <= d
		f <= e

		# for tok in list_tokens:
		# 	print tok, "and parents", tok.parents, "has children", tok.children
		# # f <= d
		# f <= a
		self.assertIn(b, a)
		self.assertIn(c, a)

		# # print d.parents
		# print "b in a"
		# print b in a
		# self.assertIn(b, a)
		# b <= [c, d]
		# self.assertIn(c, b)
		# self.assertIn(d, b)



if __name__ == '__main__':
	unittest.main()
