# -----------------------------------------------------------------------------
# run.py
# Created by Ingrid Avendano 11/14/13.
#
# Run compiler file by sending it a digital logic expression.
# -----------------------------------------------------------------------------

import ply.lex as lex
import lexer
import parser

# -----------------------------------------------------------------------------

yacc_parser = parser.yacc_parser

# -----------------------------------------------------------------------------

def run_input(expression):
	lexer.lexer.input(expression)
	lextokens = []

	dummy_tokens = []

	while True:
		token = lexer.lexer.token()
		if not token:
			break
		lextokens.append(token)
		print token

	for lextoks in lextokens:

		if lextoks.type == "ID":
			dummy_tokens.append(lextoks)
		
	return dummy_tokens

# -----------------------------------------------------------------------------

def left_child(node, indent):
	print "\t"*indent, "LEFT:"
	print_parse_tree(node.left, indent)


def right_child(node, indent):
	print "\t"*indent, "RIGHT:"
	print_parse_tree(node.right, indent)


def print_parse_tree(root_node, indent):
	print '\t'*indent, root_node
	indent += 1

	if root_node.left: 
		left_child(root_node, indent)
	if root_node.right:
		right_child(root_node, indent)
# -----------------------------------------------------------------------------

def parse_on(data, node_tokens=[], debug=0, print_tree=1):
	yacc_parser.error = 0

 	print run_input(data)

	list_node_tokens = node_tokens
	yacc_parser.parse(data)

	if yacc_parser.error:
		return None

	# print parser.root

	if print_tree:
		for root_node in parser.root:
			print "*"*80
			print "TREE:"
			print_parse_tree(root_node, 0)


def clear_parser():
	parser.root = []

