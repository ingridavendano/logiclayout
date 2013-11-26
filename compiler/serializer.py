# -----------------------------------------------------------------------------
# serializer.py
# Created by Ingrid Avendano 11/14/13.
# -----------------------------------------------------------------------------
# Converts AST (abstract syntax tere) to JSON. 
# -----------------------------------------------------------------------------

import json
from optimizer2 import *

# -----------------------------------------------------------------------------

class NodeEncoder(json.JSONEncoder):
	""" Encode Node class objects to JSON. """
	
	def default(self, tree):
		# def unknown_node(node):
		# 	return {
		# 		'kind': node.kind,
		# 		'name': node.expr,
		# 		'weight': node.weight, 
		# 		'depth': node.level,
		# 		'inputs': len(node.children),
		# 		'x': node.x,
		# 		'y': node.y
		# 	}

		# if isinstance(tree, Tree):
		# 	return {
		# 		'depth': tree.depth,
		# 		'weight': tree.root.weight,
		# 		'nodes': [
		# 			unknown_node(node) for node in tree.nodes
		# 		]
				
		# 	}	
		# else:
		# 	return json.JSONEncoder.default(self, tree)


		def unknown_node(node):
			return {
				'kind': node.kind,
				'name': node.expr,
				'weight': node.weight, 
				'depth': node.level,
				'inputs': len(node.children),
				'x': node.x,
				'y': node.y, 
				'nodes': [
					unknown_node(child) for child in node.children
				]
			}

		if isinstance(tree, Tree):
			return {
				'depth': tree.depth,
				'weight': tree.root.weight,
				'nodes': [
					unknown_node(tree.root)
				]
				
			}	
		else:
			return json.JSONEncoder.default(self, tree)

# -----------------------------------------------------------------------------

def to_json(tree, debug=False):
	""" Converts a Node Tree to JSON. """

	json_string = json.dumps(
		tree, 
		cls=NodeEncoder, 
		# sort_keys=True, 
		# indent=4,
		# separators=(',', ': ')
		)


	if debug:
		print json_string

	return json_string
