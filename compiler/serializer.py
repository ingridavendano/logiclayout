# -----------------------------------------------------------------------------
# serializer.py
# Created by Ingrid Avendano 11/14/13.
# -----------------------------------------------------------------------------
# Converts AST (abstract syntax tere) to JSON. 
# -----------------------------------------------------------------------------

import json
from optimizer import *

# -----------------------------------------------------------------------------

class NodeEncoder(json.JSONEncoder):
	""" Encode Node class objects to JSON. """
	
	def default(self, tree):

		def unknown_node(node):
			if isinstance(node, Node):
				if node.pin:
					return pin(node)
				elif node.gate:
					return gate(node)

		def gate(node):
			return {
				'type': node.expr,
				'weight': node.weight,
				'size': len(node.children),
				'level': node.level,
				'inputs': [
					unknown_node(child) for child in node.children
				]
			}

		def pin(node):
			return {
				'type': 'pin',
				'name': node.expr, 
				'level': node.level
			}

		if isinstance(tree, Tree):
			return {
				'type': 'function',
				'output': unknown_node(tree.root),
				'input': unknown_node(tree.root.children[0]),
				'weight': tree.weight,
				'levels': tree.depth,
			}	
		else:
			return json.JSONEncoder.default(self, tree)

# -----------------------------------------------------------------------------

def to_json(tree):
	""" Converts a Node Tree to JSON. """

	print "*"*80
	json_string = json.dumps(
		tree, 
		cls=NodeEncoder, 
		# sort_keys=True, 
		# separators=(',', ': ')
		)
	print json_string

	return json_string
