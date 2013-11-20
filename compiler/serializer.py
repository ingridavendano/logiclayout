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
				'type': "pin",
				'name': node.expr
			}


		if isinstance(tree, Tree):
			print "*"*80
			return {
				'expr': tree.expr,
				'output': unknown_node(tree.root),
				'tree': unknown_node(tree.root.children[0])
			}	
		else:
			return json.JSONEncoder.default(self, tree)

# -----------------------------------------------------------------------------

def to_json(tree):
	""" Converts a Node Tree to JSON. """
	print "*"*80

	json_module = json.dumps(tree, cls=NodeEncoder)

	print json_module