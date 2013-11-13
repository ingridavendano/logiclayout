# -----------------------------------------------------------------------------
# expressions.py
# Created by Ingrid Avendano 11/12/13.
#
# Main file to run lex-yacc on boolean algebra expressions. 
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"..")

import logic_lex
import logicgrammar

# -----------------------------------------------------------------------------

if __name__ == '__main__':

	while True:
		try:
			line = input(' expr: ')
		except EOFError:
			break
		# logictokens.run_input(line)
		logicgrammar.parse(line)

