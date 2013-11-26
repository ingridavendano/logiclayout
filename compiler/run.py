# -----------------------------------------------------------------------------
# run.py
# Created by Ingrid Avendano 11/14/13.
# -----------------------------------------------------------------------------
# Run compiler file by sending it a digital logic expression.
# -----------------------------------------------------------------------------

import parser
import serializer
from optimizer2 import Tree

# -----------------------------------------------------------------------------
# Run PLY yacc in the parser module.
# -----------------------------------------------------------------------------

yacc = parser.run_yacc

# -----------------------------------------------------------------------------

def clear_parser():
	""" Empties root of pre-exisiting root tokens. """
	parser.root = []

def compiler(data, debug=0, print_tree=1):
	""" Run compiler on a logic expression. """
	clear_parser()
	yacc.error = 0
	yacc.parse(data)

	if yacc.error:
		return None

	tree = Tree(parser.root[0], data)
	tree.print_tree()
	tree.print_nodes()
	# tree.print_levels()
	json_data = serializer.to_json(tree, debug=debug)

	return json_data
