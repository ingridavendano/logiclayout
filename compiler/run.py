# -----------------------------------------------------------------------------
# run.py
# Created by Ingrid Avendano 11/14/13.
#
# Run compiler file by sending it a digital logic expression.
# -----------------------------------------------------------------------------

import parser_binary

# -----------------------------------------------------------------------------

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

yacc_parser = parser_binary.yacc_parser

def parse_on(data, node_tokens=[], debug=0):
	yacc_parser.error = 0

	list_node_tokens = node_tokens
	yacc_parser.parse(data)

	if yacc_parser.error:
		return None

	print parser_binary.root

