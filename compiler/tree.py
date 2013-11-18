# -----------------------------------------------------------------------------
# tree.py
# Created by Ingrid Avendano 11/17/13.
#
# Building blocks to make abstract syntax tree.
# -----------------------------------------------------------------------------

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



class Tree(object):
	def __init__(self, root_node):
		self.root = root_node

	def json(self):
		pass


