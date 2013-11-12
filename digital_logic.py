# -----------------------------------------------------------------------------
# digital_logic.py
# Created by Ingrid Avendano 11/7/13.
#
# Reads in digital logic expressions into tokens and parses it. 
# -----------------------------------------------------------------------------

reserved = {
	'and' : 'AND',
}


tokens = [
	'NAME', 'BINARY',
	'OR', 'NOT', 'XOR', 
	'EQUALS', 'LPAREN', 'RPAREN',
	] + list(reserved.values())


# tokens 
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_AND = r'\&'
t_OR = r'\|'
t_NOT = r'~'
t_XOR = r'\^'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'



# just in case a '1' or '0' is used
def t_BINARY(t):
	r'(b0)[01]+'
	try:
		t.value = bool(int(t.value))
	except ValueError:
		print "Binary value %d is too large." % t.value
		t.value = bool(int(0))
	return t

# tokens to ignore
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
	print "Illegal character '%s'!" % t.value[0]
	t.lexer.skip(1)


# build the lexer
import ply.lex as lex
lex.lex()


# parsing rules
precedence = (
	('left','OR', 'AND', 'XOR'),
	('right', 'NOT'),
	)

# dictionary of names
names = { }

def p_statement_assign(t):
	'statement : NAME EQUALS expression'
	names[t[1]] = t[3]

def p_statement_expr(t):
	'statement : expression'
	print t[1]

def p_expression_binop(t):
	'''expression : expression OR expression
				  | expression AND expression
				  | expression XOR expression'''
	if 	 t[2] == '|': t[0] = (t[1] or  t[3])
	elif t[2] == 'and': t[0] = (t[1] and t[3])
	elif t[2] == '^': t[0] = (t[1] !=  t[3])

def p_expression_not(t):
	'expression : NOT expression'
	t[0] = not t[2]

def p_expression_group(t):
	'expression : LPAREN expression RPAREN'
	t[0] = t[2]

def p_expression_binary(t):
	'expression : BINARY'
	t[0] = t[1] 

def p_expression_name(t):
	'expression : NAME'
	try:
		t[0] = names[t[1]]
	except LookupError:
		print "Undefined name '%s'!" % t[1]
		t[0] = bool(int(0))

def p_error(t):
	print "Syntax error at '%s'." % t.value


if __name__ == '__main__':
	import ply.yacc as yacc
	yacc.yacc()


	while 1:
		try:
			expression = input('>> ')
		except EOFError:
			break
		yacc.parse(expression)
		
