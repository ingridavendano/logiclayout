# -----------------------------------------------------------------------------
# model.py
# Created by Ingrid Avendano 11/17/13.
#
# Runs the compiler on a logic expression. 
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0,"./compiler") 

import run
import json

# -----------------------------------------------------------------------------


def compile_expr(expr):
	run.clear_parser()
	parse_tree_root = run.parse_on(expr)

	json_module = make_json(parse_tree_root)
	# print json_mess


def prep_json(root):
	
	if not root.base:
		pass
	else:
		return str(root)

def make_json(root):
	module = prep_json(root)
	print module

	# for start in module:
	# 	pass