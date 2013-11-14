# -----------------------------------------------------------------------------
# logic_parser.py
# Created by Ingrid Avendano 11/11/13.
#
# List of grammar specifications for tokens of boolean alegbra expressions. 
# -----------------------------------------------------------------------------

import lexer 
from token import Node
import ply.yacc as yacc

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

global nodes
global id_nodes
# nodes = []
literal_nodes = {}
nodes = []
id_nodes = {}



# -----------------------------------------------------------------------------

def p_statement_assign(t):
	'statement : ID EQUALS expression'
	print 11

	variable = Node(t[1], "ID")
	equals = Node(t[2], "EQUALS")

	if isinstance(t[3], int):
		expr = literal_nodes[t[3]]
	else:
		expr = t[3]

	variable.value = expr.value

	equals.right(expr)
	equals.left(expr)

	id_nodes[t[1]] = variable

	nodes.append(variable)
	nodes.append(equals)

	ids[t[1]] = t[3]

def p_statement_expr(t):
	'statement : expression'
	print 2
	# print t[1], t[1].value
	# return t[1]
	print "--->", t[1], t[1].value

def p_expression_not(t):
	'expression : NOT expression'
	print 3
	t[0] = ~t[2]

def p_expression_or(t):
	'expression : expression OR expression'
	print 4
	print "expr1", t[1]
	print "expr2", t[3]

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

	# t[0] = t[1] & t[3]

def p_expression_xor(t):
	'expression : expression XOR expression'
	print 6
	t[0] = t[1] ^ t[3]

def p_expression_group(t):
	'''expression : LPAREN   expression RPAREN
				  | LBRACE   expression RBRACE
				  | LBRACKET expression RBRACKET'''
	print 7
	t[0] = t[2]

def p_expression_value(t):
	'''expression : BIN
				  | INT
				  | TRUE
				  | FALSE'''
	# t[0] = nodes[t[]]
	print 8
	base = Node(t[1], "LITERAL", base=True)
	literal_nodes[t[1]] = base
	nodes.append(base)
	t[0] = t[1] 


def p_expression_id(t):
	'expression : ID'
	print 9
	try:
		# t[0] = ids[t[1]]
		t[0] = id_nodes[t[1]]
		print "id", t[1], id_nodes[t[1]]
	except LookupError:
		print "Undefined name '%s'!" % t[1]
		t[0] = bool(int(0))

def p_error(t):
	print "Syntax error at '%s'." % t.value

# -----------------------------------------------------------------------------

yacc_parser = yacc.yacc()

# -----------------------------------------------------------------------------

def parse(data, node_tokens=[], debug=0):
	yacc_parser.error = 0

	list_node_tokens = node_tokens
	yacc_parser.parse(data)



	# print "type", instance(parser)
	# print "data", type(parsed_data)
	# print "pinfo", type(parser.)

	if yacc_parser.error:
		return None

	print nodes

