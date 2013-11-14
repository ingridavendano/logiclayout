# -----------------------------------------------------------------------------
# test_logic_tokens.py
# Created by Ingrid Avendano 11/13/13.
#
# Test that boolean algebra tokens are tokenized properly.
# -----------------------------------------------------------------------------

import unittest
import sys

sys.path.insert(0,"..")
from logic_tokens import NodeToken

a = NodeToken("a", "LITERAL")
b = NodeToken("b", "AND")
c = NodeToken("c", "OR")
d = NodeToken("d", "EQUALS")
e = NodeToken("e", "FOO")
f = NodeToken("f", "BAR")
list_tokens = [a, b, c, d, e, f]

class TestTokens(unittest.TestCase):
	a <= b
	a <= c
	a <= d
	def test_children(self):
		"""> check the relationship of children in a token """
		self.assertIn(b, a)
		self.assertIn(c, a)
		self.assertIn(d, a)

	def test_parents(self):
		""" check the relationship of parents of a token """
		self.assertIn(a, d.parents)




if __name__ == '__main__':
	unittest.main()
