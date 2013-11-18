# -----------------------------------------------------------------------------
# test.py
# Created by Ingrid Avendano 11/17/13.
#
# Tests digital logic expression compiler.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"..")

from grammar import *
import unittest

# -----------------------------------------------------------------------------

class TestGrammarTokens(unittest.TestCase):
	""" """

	def test_binary_token(self):
		""" Check literal nodes take binary. """
		self.assertEqual( Literal('0b11'),  '0b11')
		self.assertEqual( Literal(0b10110), 0b10110)

	def test_integer_token(self):
		""" Check literal nodes take integers. """
		self.assertEqual( Literal('4'), '4')
		self.assertEqual( Literal(6), 6)

	def test_boolean_tokens(self):
		""" Check literal nodes take booleans. """
		self.assertEqual( Literal('TRUE'), 'TRUE')
		self.assertEqual( Literal(False), False)

	def test_id_token(self):
		""" Check id nodes represent their expression. """
		pass

	def test_delimiter_tokens(self):
		""" """
		pass

	def test_operator_tokens(self):
		""" """
		pass


	def test_root_node(self):
		""" """
		pass

	def test_terminal_nodes(self):
		""" """
		pass

	def test_nonterminal_nodes(self):
		""" """
		pass

	def test_depth_of_node_tree(self):
		""" """
		pass

	def test_node_locations(self):
		""" """
		pass

	def test_node_children_relationships(self):
		""" """
		pass

	def test_node_parent_relationships(self):
		""" """
		pass


if __name__ == '__main__':
	unittest.main()
