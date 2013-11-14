# -----------------------------------------------------------------------------
# logic_lex.py
# Created by Ingrid Avendano 11/11/13.
#
# List of tokens for boolean alegbra expressions. 
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"..")

import ply.lex as lex

# -----------------------------------------------------------------------------

# list of tokens
tokens = [
	# identifier
	'ID',

	# logic operatiors 
	'NOT', 'AND', 'OR', 'XOR',
	
	# assigments
	'EQUALS',

	# delimiters 
	'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE',

	# binary numbers and integers
	'BIN', 'INT', 'TRUE', 'FALSE'
	]

# -----------------------------------------------------------------------------

# identifier
t_ID			= r'[a-zA-Z_][a-zA-Z0-9_]*'

# logic operators 
t_NOT			= r'(([Nn][Oo][Tt])|~|!)'
t_AND			= r'(([An][Nn][Dd])|(\&{1,2})|\*)'
t_OR			= r'(([Oo][Rr])|\|{1,2}|\+)'
t_XOR			= r'\^'

# assignments
t_EQUALS		= r'='

# delimiters
t_LPAREN		= r'\('
t_RPAREN		= r'\)'
t_LBRACKET		= r'\['
t_RBRACKET		= r'\]'
t_LBRACE		= r'\{'
t_RBRACE		= r'\}'

# tokens to ignore
t_ignore		= " \t"

# binary
def t_BIN(t):
	r'(0b)[01^(2-9)]+'
	try:
		t.value = int(t.value,2)
	except ValueError:
		print "Binary value %d is too large." % t.value
		t.value = int(0)
	return t

# integers
def t_INT(t):
	r'[0-9][0-9]*'
	try:
		t.value = int(t.value)
	except ValueError:
		print "Integer value %d is too large." % t.value
		t.value = int(0)
	return t

# true value considered on
def t_TRUE(t):
	r'([tT][rR][uU][eE])' 
	t.value = int(1)
	return t

# false value considered off
def t_FALSE(t):
	r'([fF][aA][lL][sS][eE])'
	t.value = int(0)
	return t

# new lines
def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

# tokens that have no type
def t_error(t):
	print "Illegal character '%s'!" % t.value[0]
	t.lexer.skip(1)

# -----------------------------------------------------------------------------

lexer = lex.lex()

# def run_input(expression):
# 	lexer.input(expression)
# 	lextokens = []

# 	while True:
# 		token = lexer.token()
# 		if not token:
# 			break
# 		lextokens.append(token)

# 	return lextokens

# if __name__ == "__main__":
# 	lex.runmain(lexer)
