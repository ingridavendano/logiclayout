# -----------------------------------------------------------------------------
# logic_parser.py
# Created by Ingrid Avendano 11/11/13.
#
# List of grammar specifications for tokens of boolean alegbra expressions. 
# -----------------------------------------------------------------------------

import sys
import logic_lex
import ply.yacc as yacc

# -----------------------------------------------------------------------------

# grabs token map
tokens = logic_lex.tokens

# parsing rules
precedence = (
				('left',  'OR', 'AND', 'XOR'),
				('right', 'NOT'),
)

# dictionary of names
ids = { }

# -----------------------------------------------------------------------------

def p_statement_assign(t):
	'statement : ID EQUALS expression'
	ids[t[1]] = t[3]

def p_statement_expr(t):
	'statement : expression'
	OUTPUT = t[1]
	print OUTPUT
	return OUTPUT

def p_expression_not(t):
	'expression : NOT expression'
	t[0] = ~t[2]

def p_expression_or(t):
	'expression : expression OR expression'
	t[0] = t[1] | t[3]

def p_expression_and(t):
	'expression : expression AND expression'
	t[0] = t[1] & t[3]

def p_expression_xor(t):
	'expression : expression XOR expression'
	t[0] = t[1] ^ t[3]

def p_expression_group(t):
	'''expression : LPAREN   expression RPAREN
				  | LBRACE   expression RBRACE
				  | LBRACKET expression RBRACKET'''
	t[0] = t[2]

def p_expression_value(t):
	'''expression : BIN
				  | INT
				  | TRUE
				  | FALSE'''
	t[0] = t[1] 

def p_expression_id(t):
	'expression : ID'
	try:
		t[0] = ids[t[1]]
	except LookupError:
		print "Undefined name '%s'!" % t[1]
		t[0] = bool(int(0))

def p_error(t):
	print "Syntax error at '%s'." % t.value

# -----------------------------------------------------------------------------

parser = yacc.yacc()

def parse(data,debug=0,llex=None):
	parser.error = 0

	parsed_data = parser.parse(data, debug=debug, lexer=llex)



	# print "type", instance(parser)
	# print "data", type(parsed_data)
	# print "pinfo", type(parser.)

	if parser.error:
		return None

	print parser.goto
