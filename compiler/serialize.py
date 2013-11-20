# -----------------------------------------------------------------------------
# serialize.py
# Created by Ingrid Avendano 11/14/13.
# -----------------------------------------------------------------------------
# Converts AST (abstract syntax tere) to JSON. 
# -----------------------------------------------------------------------------

import json

# -----------------------------------------------------------------------------

class NodeEncoder(json.JSONEncoder):
	""" Encode Node class objects to JSON. """

	def default(self, node):
		if isinstance(node, Node):
			return {
				'base': node.base,
				'expr': node.expr,
				'children': [
					self.default(child) for child in node.children
				]
			}	
		else:
			return json.JSONEncoder.default(self, node)
