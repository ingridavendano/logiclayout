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

		def gate(self, node):
			return {
				'type': node.expr,
				'weight': node.weight,
				'size': len(node.children),
				'inputs': [
					unknown_node(child) for child in node.children
				]
			}

		def pin(self, node):
			return {
				'type': "pin",
				'name': node.expr
			}


		if isinstance(tree, Tree):
			return {
				'expr': tree.expr,
				'tree': {
					'output': unknown_node(tree.root),
				},

				'output': {
					'type': "pin",
					'name': tree.root.expr
				},
				'children': [
					self.default(child) for child in node.children
				]
			}	
		else:
			return json.JSONEncoder.default(self, node)

# -----------------------------------------------------------------------------

def to_json(tree):
	""" Converts a Node Tree to JSON. """

	json_module = json.dumps(tree.root, cls=NodeEncoder)

	print json_module