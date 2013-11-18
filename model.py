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
		root_module = []

		children = []

		for child in root.children:
			print "parent", root, "children", child
			if child.base:
				print "base!", child
				children.append(str(child))
			else:
				child_module = make_json(child)
				children.append(child_module)

		root_module.append((root, children))

		return root_module
	# return root

def make_json(root):
	module = prep_json(root)
	print module

	for start in module:
		pass