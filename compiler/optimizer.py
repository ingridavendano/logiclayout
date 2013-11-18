# -----------------------------------------------------------------------------
# optimizer.py
# Created by Ingrid Avendano 11/17/13.
#
# Optimizer the parser.py output which is a parser trees. 
# -----------------------------------------------------------------------------

from tree import *

def print_parse_tree(root_node, indent=0):
	print '\t'*indent, ' ', root_node
	indent += 1

	if root_node.left: 
		print "\t"*indent, "LEFT:"
		print_parse_tree(root_node.left, indent)
	if root_node.right:
		print "\t"*indent, "RIGHT:"
		print_parse_tree(root_node.right, indent)


def next_node(node):
	if node.right and node.left:
		return True


def reorganize_ast(root):
	""" Reoganizing abstract syntax tree. """
	

