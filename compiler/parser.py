# -----------------------------------------------------------------------------
# parser.py
# Created by Ingrid Avendano 11/11/13.
# -----------------------------------------------------------------------------
# Grammar functions highlighted for how digital logic tokens are stacked. 
# -----------------------------------------------------------------------------

import lexer 
from grammar import *

# -----------------------------------------------------------------------------

# grabs token map from lexer
tokens = lexer.tokens

# parsing rules
precedence = (
    ('left', 'AND', 'NAND', 'OR', 'NOR', 'XOR', 'NXOR'),
    ('right', 'NOT'),
)

# dictionary of id names and root list to hold the root tokens 
ids  = {}
root = []

# -----------------------------------------------------------------------------

def p_statement_assign(t):
    'statement : ID EQUALS expression'
    if t[3].expr == 'error':
        equals_node = Break()
    else:
        if type(t[1]) == str:
            id_node = Id(t[1])
            equals_node = Equals(id_node, t[3])
        else:
            equals_node = Equals(t[1], t[3])
        root.append(equals_node)
    ids[t[1]] = t[3]
    t[0] = equals_node

def p_statement_expr(t):
    'statement : expression'
    root.append(t[1])

def p_expression_not(t):
    'expression : NOT expression'
    t[0] = Not(t[2])

def p_expression_nand(t):
    'expression : expression NAND expression'
    t[0] = Nand(t[1], t[3])

def p_expression_and(t):
    'expression : expression AND expression'
    t[0] = And(t[1], t[3])

def p_expression_nor(t):
    'expression : expression NOR expression'
    t[0] = Nor(t[1], t[3])

def p_expression_or(t):
    'expression : expression OR expression'
    t[0] = Or(t[1], t[3])

def p_expression_nxor(t):
    'expression : expression NXOR expression'
    t[0] = Nxor(t[1], t[3])

def p_expression_xor(t):
    'expression : expression XOR expression'
    t[0] = Xor(t[1], t[3])

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

def p_expression_id(t):
    'expression : ID'
    try:
        variable = ids[t[1]]
    except LookupError:
        variable = Literal()
    id_node = Id(t[1], variable)
    t[0] = id_node

def p_expression_broken(t):
    '''expression : expression AND
                  | expression OR
                  | expression XOR
                  | expression NAND
                  | expression NOR
                  | expression NXOR'''
    print "This expression is not valid."
    t[0] = Break()

def p_error(t):
    print "Syntax error at '%s'." % t.value

# -----------------------------------------------------------------------------
# Run PLY yacc module that uses grammar functions to address tokens on stack.
# -----------------------------------------------------------------------------

import ply.yacc as yacc
run_yacc = yacc.yacc()
