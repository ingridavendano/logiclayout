# -----------------------------------------------------------------------------
# parser.py
# Created by Ingrid Avendano 11/11/13.
#
# List of grammar specifications of digital logic expressions. 
# -----------------------------------------------------------------------------

import lexer 
# from token import Node
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
id_nodes = { }
terminals = { }
nonterminals = { }

literal_nodes = {}
nodes = []
root = []


# -----------------------------------------------------------------------------

def p_statement_assign(t):
	'statement : ID EQUALS expression'
	id_node = Id(t[1])
	# expr_node = 
	equals_node = Equals()

	# print 11

	# variable = Node(t[1], "ID")
	# equals = Node(t[2], "EQUALS")

	# # checks if ID is the lowest value
	# if isinstance(t[3], int):
	# 	expr = literal_nodes[t[3]]
	# else:
	# 	expr = t[3]


	# variable.value = expr.value

	# equals.right(expr)
	# equals.left(expr)

	# id_nodes[t[1]] = variable

	# nodes.append(variable)
	# nodes.append(equals)

	# ids[t[1]] = t[3]

def p_statement_expr(t):
	'statement : expression'
	print 2
	# print t[1], t[1].value
	# return t[1]
	print "--->", t[1]


def p_expression_not(t):
	'expression : NOT expression'
	print 3
	
	t[0] = ~t[2]


def p_expression_or(t):
	'expression : expression OR expression'
	print 4
	print "expr1", t[1]
	print "expr2", t[3]

	# checks if the expressions are the same and does not apply OR operator 
	if t[1] == t[3]:
		t[0] = t[1]
	else:
		or_node = Node(t[2],"OR")
		or_node.left(t[1])
		or_node.right(t[3])

		value = t[1].value | t[3].value
		or_node.eval(value)

		nodes.append(or_node)

		t[0] = or_node
	# t[0] = t[1] | t[3]

def p_expression_and(t):
	'expression : expression AND expression'
	print 5
	print "expr1", t[1]
	print "expr2", t[3]

	if t[1] == t[3]:
		t[0] = t[1]
	else: 
		and_node = Node(t[2],"AND")
		and_node.left(t[1])
		and_node.right(t[3])

		value = t[1].value & t[3].value
		and_node.eval(value)

		nodes.append(and_node)

		t[0] = and_node

def p_expression_xor(t):
	'expression : expression XOR expression'
	if t[1] == t[3]:
		t[0] = t[1]
	else: 
		xor_node = Node(t[2],"XOR")
		xor_node.left(t[1])
		xor_node.right(t[3])

		value = t[1].value ^ t[3].value
		xor_node.eval(value)

		nodes.append(and_node)

		t[0] = and_node
	# t[0] = t[1] ^ t[3]

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

	t[0] = Literal(t[1])

	# t[0] = nodes[t[]]
	# print 8
	# base = Node(t[1], "LITERAL", base=True)
	# literal_nodes[t[1]] = base
	# nodes.append(base)
	# t[0] = t[1] 

def p_expression_id(t):
	'expression : ID'
	print 9
	try:
		t[0] = id_nodes[t[1]]
		print "id", t[1], id_nodes[t[1]]
	except LookupError:
		print "Undefined name '%s'!" % t[1]
		node_without_value = Node(t[1],'UNDEFINED_VAR',base=True)
		t[0] = node_without_value

def p_error(t):
	print "Syntax error at '%s'." % t.value

# -----------------------------------------------------------------------------

import ply.yacc as yacc
yacc_parser = yacc.yacc()
