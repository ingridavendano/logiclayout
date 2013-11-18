# -----------------------------------------------------------------------------
# test.py
# Created by Ingrid Avendano 11/12/13.
#
# Tests digital logic expression compiler.
# -----------------------------------------------------------------------------

import run
import unittest

# -----------------------------------------------------------------------------

class TestExpressions(unittest.TestCase):
	""" """

	def test_single_assigned_expressions(self):
		""" """
		pass

	def test_multiple_assigned_expressions(self):
		"""  """

		# data = ["a = 0", 
		# 		"b = 1", 
		# 		"c = 1", 
		# 		"d = 0", 
		# 		"f = [(a*b)+(c*d)]", 
		# 		"f", 
		# 		"g = b * c",
		# 		"g"]

		# node_tokens = []
		# found_tokens = []

		# for d in data:
		# 	print "*"*10, d
		# 	run.parse(d, node_tokens)
		# 	# found_tokens += logic_lex.run_input(d)
		
		# # print found_tokens

	def test_literal_expressions(self):
		""" Testing expressions that are only literals. """ 

		for expr in ['1', 'false', '24', 'TRUE', '0b11']:
			print "test:", expr
			run.parse_on(expr)


	def test_unassigned_single_variable_expressions(self):
		""" Testing unassgined single variable expressions. """ 
		pass
		for expr in ['a', 'bb', 'C']:
			print "test:", expr
			run.parse_on(expr)

	def test_single_unassigned_expressions(self):
		""" """
		pass

	def test_multiple_unassigned_expressions(self):
		""" """
		# data = ["f = [(a*b)+(c*d)]"]
		pass


class TestTokens(unittest.TestCase):
	""" """

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


class TestParser(unittest.TestCase):
	""" """

	def test_equals(self):
		""" """
		pass

	def test_not(self):
		""" """
		pass

	def test_and(self):
		""" """
		pass

	def test_or(self):
		""" """
		pass

	def test_literals(self):
		""" """
		pass


class TestLexer(unittest.TestCase):
	""" """

	def test_id_token(self):
		""" """
		pass

	def test_binary_token(self):
		""" """
		pass

	def test_integer_token(self):
		""" """
		pass

	def test_boolean_tokens(self):
		""" """
		pass

	def test_delimiter_tokens(self):
		""" """
		pass

	def test_operator_tokens(self):
		""" """
		pass


if __name__ == '__main__':
	unittest.main()
