# -----------------------------------------------------------------------------
# parser.py
# Created by Ingrid Avendano 11/11/13.
#
# List of grammar specifications of digital logic expressions. 
# -----------------------------------------------------------------------------

import lexer 
from token import *

# -----------------------------------------------------------------------------

# grabs token map from lexer
tokens = lexer.tokens

# parsing rules
precedence = (
				('left',  'OR', 'AND', 'XOR'),
				('right', 'NOT'),
)

# dictionary of names
ids = { }
root = []


# -----------------------------------------------------------------------------

def p_statement_assign(t):
	'statement : ID EQUALS expression'
	print 'EQUALS'
	

	if type(t[1]) == str:
		id_node = Id(t[1])
		equals_node = Equals(id_node, t[3])
	else:
		equals_node = Equals(t[1], t[3])
	ids[t[1]] = t[3]

	t[0] = equals_node

	root.append(equals_node)

def p_statement_expr(t):
	'statement : expression'
	print 'EXPR'
	root.append(t[1])

def p_expression_not(t):
	'expression : NOT expression'
	print 'NOT'
	not_node = Not(t[2])
	t[0] = not_node

def p_expression_or(t):
	'''expression : expression OR expression
			  	  | ID OR expression'''
	# 'expression : expression OR expression'
	print 'OR'
	or_node = Or(t[1], t[3])
	t[0] = or_node

def p_expression_and(t):
	'expression : expression AND expression'
	print 'AND'
	and_node = And(t[1], t[3])
	t[0] = and_node

def p_expression_xor(t):
	'expression : expression XOR expression'
	print 'XOR'
	xor_node = Xor(t[1], t[3])
	t[0] = xor_node

def p_expression_group(t):
	'''expression : LPAREN   expression RPAREN
				  | LBRACE   expression RBRACE
				  | LBRACKET expression RBRACKET'''
	t[0] = t[2]

def p_expression_literal(t):
	'''expression : BIN
				  | INT
				  | TRUE
				  | FALSE'''
	print 'LITERAL'
	t[0] = Literal(t[1])

def p_expression_id(t):
	'expression : ID'
	# print 'ID'
	try:
		variable = ids[t[1]]
		id_node = Id(t[1], variable)
	except LookupError:
		print "Undefined name '%s'!" % t[1]
		dummy_variable = Literal()
		id_node = Id(t[1], dummy_variable)
	t[0] = id_node

def p_error(t):
	print "Syntax error at '%s'." % t.value

# -----------------------------------------------------------------------------

import ply.yacc as yacc
yacc_parser = yacc.yacc()
