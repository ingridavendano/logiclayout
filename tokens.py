# -----------------------------------------------------------------------------
# tokens.py
# Created by Ingrid Avendano 11/11/13.
#
# List of tokens for boolean alegbra expressions. 
# -----------------------------------------------------------------------------

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
	'BIN', 'INT',
	] 

# -----------------------------------------------------------------------------

# identifier
t_ID			= r'^(0b)[a-zA-Z_][a-zA-Z0-9_]*'

# logic operators 
t_NOT 	 = r'(([Nn][Oo][Tt])|~|!)'
t_AND 	 = r'(([An][Nn][Dd])|(\&{1,2})|\*)'
t_OR 	 = r'(([Oo][Rr])|\|{1,2}|\+)'
t_XOR 	 = r'\^'

# assignments
t_EQUALS = r'='

# delimiters
t_LPAREN		= r'\('
t_RPAREN		= r'\)'
t_LBRACKET		= r'\['
t_RBRACKET		= r'\]'
t_LBRACE		= r'\{'
t_RBRACE		= r'\}'

# tokens to ignore
t_ignore = " \t"

# binary numbers
t_BIN 			= r'(0b)[01^(2-9)]+'

# integers
def t_INT(t):
	r'[1-9][0-9]*'
	try:
		t.value = bin(int(t.value))
	except ValueError:
		print "Binary value %d is too large." % t.value
		t.value = bin(int(0))
	return t

# new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# tokens that have no type
def t_error(t):
	print "Illegal character '%s'!" % t.value[0]
	t.lexer.skip(1)
