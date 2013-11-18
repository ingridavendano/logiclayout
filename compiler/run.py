# -----------------------------------------------------------------------------
# run.py
# Created by Ingrid Avendano 11/14/13.
#
# Run compiler file by sending it a digital logic expression.
# -----------------------------------------------------------------------------

import ply.lex as lex
import lexer
import parser
import optimize

# -----------------------------------------------------------------------------

yacc_parser = parser.yacc_parser

# -----------------------------------------------------------------------------

# def run_input(expression):
# 	lexer.lexer.input(expression)
# 	lextokens = []

# 	dummy_tokens = []

# 	while True:
# 		token = lexer.lexer.token()
# 		if not token:
# 			break
# 		lextokens.append(token)
# 		print token

# 	for lextoks in lextokens:

# 		if lextoks.type == "ID":
# 			dummy_tokens.append(lextoks)
		
# 	return dummy_tokens

# -----------------------------------------------------------------------------

def parse_on(data, node_tokens=[], debug=0, print_tree=1):
	yacc_parser.error = 0

 	# print run_input(data)

	list_node_tokens = node_tokens
	yacc_parser.parse(data)

	if yacc_parser.error:
		return None

	# print parser.root
	parse_tree_root = None
	if print_tree:
		for root_node in parser.root:
			# print "*"*80
			# print "TREE:"
			# optimizer.print_parse_tree(root_node)

			print "#"*80

			parse_tree_root = optimize.reorganize(root_node)

			optimize.print_tree(parse_tree_root)
		print "#"*80

	return parse_tree_root

def clear_parser():
	parser.root = []

