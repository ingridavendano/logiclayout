# -----------------------------------------------------------------------------
# model.py
# Created by Ingrid Avendano 11/17/13.
#
# Runs the compiler on a logic expression. 
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"./compiler") 

import run

def compile_expr(expr):
	print expr
	run.clear_parser()
	run.parse_on(expr)