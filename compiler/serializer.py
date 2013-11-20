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
				'inputs': [
					unknown_node(child) for child in node.children
				]
			}

		def pin(node):
			return {
				'type': 'pin',
				'name': node.expr
			}

		if isinstance(tree, Tree):
			return {
				'type': 'function',
				'output': unknown_node(tree.root),
				'inputs': unknown_node(tree.root.children[0])
			}	
		else:
			return json.JSONEncoder.default(self, tree)

# -----------------------------------------------------------------------------

def to_json(tree):
	""" Converts a Node Tree to JSON. """

	json_string = json.dumps(
		tree, 
		cls=NodeEncoder, 
		sort_keys=True, 
		indent=4, 
		separators=(',', ': ')
		)

	return json_string
