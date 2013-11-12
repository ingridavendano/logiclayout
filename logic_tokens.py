# -----------------------------------------------------------------------------
# logic_tokens.py
# Created by Ingrid Avendano 11/11/13.
#
# List of tokens that are special for boolean alegbra expressions. 
# -----------------------------------------------------------------------------

# # class that embodies expressions that are tokenized
# class Tokenizer():
# 	expression = ""
# 	tokens = []

# 	def __init__(self, expression):






tokens = [
	'ID', 
	'BINARY',
	'NUMBER',
	'OR', 
	'AND', 
	'NOT', 
	'XOR', 
	'EQUALS', 
	'LPAREN', 
	'RPAREN',
	] 
	# + list(reserved.values())


# tokens
# regex for ignore case sensitive does not work :-(
t_BINARY = r'(0b)[01^(2-9)]+'
t_NOT 	 = r'(([Nn][Oo][Tt])|~|!)'
t_AND 	 = r'(([An][Nn][Dd])|(\&{1,2})|\*)'
t_OR 	 = r'(([Oo][Rr])|\|{1,2}|\+)'
t_XOR 	 = r'\^'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'


# tokens to ignore
t_ignore = " \t"

# def t_NOT(t):
# 	r'(([Nn][Oo][Tt])|~|!)'
# 	return t

# def t_AND(t):
# 	r'(([An][Nn][Dd])|\&{1,2}|*)'
# 	return t

# def t_OR(t):
# 	r'(([Oo][Rr])|\|{1,2}|\+)'
# 	return t

# # just in case a '1' or '0' is used for binary then it will be converted
# def t_BINARY(t):
# 	r'(0b)[01^(2-9)]+'
# 	try:
# 		print "FUCK"
# 		t.value = t.value
# 	except ValueError:
# 		print "Binary value %d is too large." % t.value
# 		t.value = bin(int(0))
# 	return t

def t_NUMBER(t):
	r'[1-9][0-9]*'
	try:
		t.value = bin(int(t.value))
	except ValueError:
		print "Binary value %d is too large." % t.value
		t.value = bin(int(0))
	return t


def t_ID(t):
	r'^(0b)[a-zA-Z_][a-zA-Z0-9_]*'
	# # catches binary or anything weird 
	# t.type = reserved.get(t.value, 'ID') 
	return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
	print "Illegal character '%s'!" % t.value[0]
	t.lexer.skip(1)



# parsing rules
precedence = (
	('left','OR', 'AND', 'XOR'),
	('right', 'NOT'),
	)

# dictionary of names
names = { }

def p_statement_assign(t):
	'statement : ID EQUALS expression'
	names[t[1]] = t[3]

def p_statement_expr(t):
	'statement : expression'
	global OUTPUT 
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
	'expression : LPAREN expression RPAREN'
	t[0] = t[2]

def p_expression_binary(t):
	'expression : BINARY'
	t[0] = t[1] 

def p_expression_number(t):
	'expression : NUMBER'
	t[0] = t[1] 

def p_expression_id(t):
	'expression : ID'
	try:
		t[0] = names[t[1]]
	except LookupError:
		print "Undefined name '%s'!" % t[1]
		t[0] = bool(int(0))

def p_error(t):
	print "Syntax error at '%s'." % t.value


if __name__ == '__main__':
	# build the lexer
	import ply.lex as lex
	check = lex.lex()
	tok = check.token()
	

	import ply.yacc as yacc
	yacc.yacc()


	while 1:
		try:
			expression = input('>> ')
		except EOFError:
			break
		yacc.parse(expression)


		

	
