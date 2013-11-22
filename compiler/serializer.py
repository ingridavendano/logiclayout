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

		# def unknown_node(node):
		# 	if isinstance(node, Node):
		# 		return {
		# 			'name': node.expr,
		# 			'weight': node.weight,
		# 			'size': len(node.children),
		# 			'type': pin(node) if node.pin else gate(node)
		# 		}

		# def gate(node):
		# 	return {
		# 		node.expr.lower()
		# 		}

		# def pin(node):
		# 	return 'pin'

		def unknown_node(node):
			if isinstance(node, Node):
				if node.pin:
					return pin(node)
				elif node.gate:
					return gate(node)

		def gate(node):
			return {
				'kind': node.expr.lower(),
				'weight': node.weight,
				'size': len(node.children),
				'level': node.level,
				'inputs': [
					unknown_node(child) for child in node.children
				]
			}

		def pin(node):
			return {
				'kind': 'input',
				'weight': node.weight,
				'name': node.expr, 
				'level': node.level
			}

		if isinstance(tree, Tree):
			return {
				'kind': 'output',
				'name': root.expr, 
				'level': root.level,
				'inputs': [
					unknown_node(child) for child in root.children
				]
				
			}	
		else:
			return json.JSONEncoder.default(self, tree)

		# def unknown_node(node):
		# 	if isinstance(node, Node):
		# 		# if node.pin:
		# 		# 	return pin(node)
		# 		# elif node.gate:
		# 		# 	return gate(node)

		# 		return {
		# 			'name': node.expr,
		# 			'weight': node.weight,
		# 			'size': len(node.children),
		# 			'type': pin(node) if node.pin else gate(node)
		# 		}	

		# def gate(node):
		# 	return node.expr.lower()

		# def pin(node):
		# 	return 'pin'

		# def nodes_in_cluster(nodes):
		# 	return [unknown_node(node) for node in nodes] 

		# def clusters_in_levels(cluster):
		# 	# print nodes, len(nodes)
		# 	return [nodes_in_cluster(nodes) for nodes in cluster] 
			

		# if isinstance(tree, Tree):
		# 	print tree.levels
		# 	return {
		# 		'depth': tree.depth,
		# 		'weight': tree.weight,
		# 		'levels': [
		# 			clusters_in_levels(level) for level in tree.levels
		# 		]
		# 	}	
		# else:
		# 	return json.JSONEncoder.default(self, tree)

# -----------------------------------------------------------------------------

def to_json(tree):
	""" Converts a Node Tree to JSON. """

	print "*"*80
	json_string = json.dumps(
		tree, 
		cls=NodeEncoder, 
		# sort_keys=True, 
		# indent=4,
		# separators=(',', ': ')
		)
	print json_string

	return json_string
