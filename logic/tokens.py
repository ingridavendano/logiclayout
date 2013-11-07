# -----------------------------------------------------------------------------
# tokens.py
# Created by Ingrid Avendano 11/7/13.
#
# Lexer file that reads in digital logic expressions and parses it. 
# -----------------------------------------------------------------------------


tokens = (
	'NAME', 'BINARY',
	'AND', 'OR', 'NOT', 'XOR', 
	'EQUALS', 'LPAREN', 'RLAREN'
	)


# tokens 
t_NAME = r'[a-zA-z_][a-zA-Z0-9_]*'
t_AND = r'\*'
t_OR = r'\+'
t_NOT = r'!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
# tokens to ignore
t_ignore = " \t"


# just in case a '1' or '0' is used
def t_BINARY(t):
	r'[01]+'
	try:
		t.value = bin(t.value)
	except ValueError:
		print "Binary value %d is too large." % t.value
		t.value = bin(0)
	return t


def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")


def t_error(t):
	print "Illegal character '%s'!" % t.value[0]
	t.lexer.skip(1)
