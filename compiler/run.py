# -----------------------------------------------------------------------------
# run.py
# Created by Ingrid Avendano 11/14/13.
# -----------------------------------------------------------------------------
# Run compiler file by sending it a digital logic expression.
# -----------------------------------------------------------------------------

import ply.lex as lex
import lexer
import parser
import optimize
from optimize import *

# -----------------------------------------------------------------------------
# Run PLY yacc in the parser module.
# -----------------------------------------------------------------------------

yacc = parser.run_yacc

# -----------------------------------------------------------------------------

def clear_parser():
	""" Empties root of pre-exisiting root tokens. """
	parser.root = []

def parse_expression(expr, debug=0):
	""" Run parser on one expression and return a tree of that expression. """
	clear_parser()
	yacc.error = 0
	yacc.parse(expr)

	if yacc.error:
		return None

	return Tree(parser.root[0])

# def compiler_multiple(data, debug=0, print_tree=1):
# 	""" Run compiler on a logic expression. """

# 	parser_trees = []

# 	for expr in data:
# 		new_tree = parse_expression(expr)
# 		parser_trees.append(new_tree)

# 		print "*"*80
# 		new_tree.print_tree()
# 		print "*"*80
# 		new_tree.print_levels()	
# 		print "*"*80

# 	return None

def compiler(data, debug=0, print_tree=1):
	""" Run compiler on a logic expression. """
	clear_parser()
	yacc.error = 0
	yacc.parse(data)

	if yacc.error:
		return None

	return Tree(parser.root[0])

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

