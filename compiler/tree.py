# -----------------------------------------------------------------------------
# tree.py
# Created by Ingrid Avendano 11/17/13.
#
# Building blocks to make abstract syntax tree.
# -----------------------------------------------------------------------------
import json

class Node(object):
	def __init__(self, token):
		self.children = []
		self.base = False
		self.gate = False

		if token.kind == 'LITERAL':
			if token.expr == None:
				self.expr = '0'
			else:
				self.expr = '1'
		elif token.kind == 'ID':
			self.expr = token.expr
		else:
			self.gate = True
			self.expr = token.kind

	def __repr__(self):
		""" What is displayed when a node is represented. """
		return "%r" % self.expr

	def __str__(self):
		""" What is displayed when a node is represented. """
		return "%s" % str(self.expr)

	def add(self, *children):
		self.children += children

class NodeEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Node):
			return {
				'base': obj.base,
				'expr': obj.expr,
				'children': [
					self.default(child) for child in obj.children
				]
			}	
		else:
			return json.JSONEncoder.default(self, obj)


class Tree(object):
	def __init__(self, root_node):
		self.root = root_node

	def json(self):
		pass


