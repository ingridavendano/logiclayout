# -----------------------------------------------------------------------------
# test.py
# Created by Ingrid Avendano 11/12/13.
# -----------------------------------------------------------------------------
# Tests digital logic expression compiler.
# -----------------------------------------------------------------------------

# import run

# -----------------------------------------------------------------------------

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
		# self.assertEqual( Id('A'), 'A')
		# self.assertEqual( Id('z'), 'z')
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

class TestExpressions(unittest.TestCase):
	""" """

	def test_single_assigned_expressions(self):
		""" """
		pass

	def test_multiple_assigned_expressions(self):
		"""  """
		# run.clear_parser()
		# # expressions = [
		# # 	'a = 1',
		# # 	'b = 0',
		# # 	'f = a * b',
		# # 	'f'
		# # ]
		# expressions = [
		# 	'f = a | b | c'
		# ]
		# for expr in expressions:
		# 	print expr
		# 	run.parse_on(expr)
		pass

	# def test_literal_expressions(self):
	# 	""" Testing expressions that are only literals. """ 
	# 	run.clear_parser()
	# 	for expr in ['1', 'false', '24', 'TRUE', '0b11']:
	# 		print "test:", expr
	# 		run.parse_on(expr)


	# def test_unassigned_single_variable_expressions(self):
	# 	""" Testing unassgined single variable expressions. """ 
	# 	run.clear_parser()
	# 	for expr in ['a', 'bb', 'C']:
	# 		print "test:", expr
	# 		run.parse_on(expr)

	# def test_single_unassigned_expressions(self):
	# 	""" Testing multiple expressions with unassigned variables. """
	# 	run.clear_parser()
	# 	# for expr in ['f = False and b', 'g = c ^ d', 'h = e | True']:
	# 	for expr in ['f = a and b\n']:
	# 		print "test:", expr
	# 		run.parse_on(expr, print_tree=1)

	# def test_multiple_unassigned_expressions(self):
	# 	""" """
	# 	# data = ["f = [(a*b)+(c*d)]"]
	# 	pass


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

	# def test_layout(self):
		
	# 	def print_parse_tree(root_node, indent=0):
	# 		""" Print node tree where each node has left and right child. """
	# 		print '\t'*indent, ' ', root_node
	# 		indent += 1

	# 		if root_node.left: 
	# 			print "\t"*indent, "LEFT:"
	# 			print_parse_tree(root_node.left, indent)
	# 		if root_node.right:
	# 			print "\t"*indent, "RIGHT:"
	# 			print_parse_tree(root_node.right, indent)



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
