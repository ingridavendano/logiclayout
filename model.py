# -----------------------------------------------------------------------------
# model.py
# Created by Ingrid Avendano 11/17/13.
# -----------------------------------------------------------------------------
# Runs the compiler on a logic expression. 
# -----------------------------------------------------------------------------

from compiler import run

# -----------------------------------------------------------------------------


def compile_expr(expr):
	run.clear_parser()
	return run.compiler(expr)

def make_json(root):
	pass 
