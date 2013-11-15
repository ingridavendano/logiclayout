# -----------------------------------------------------------------------------
# token.py
# Created by Ingrid Avendano 11/12/13.
#
# Description the Node classes for boolean algebra tokens.
# -----------------------------------------------------------------------------

# token class template
class Node(object):
	def __init__(self, expr, kind, is_terminal=False, base=False, root=False):
		self.expr = expr
		self.kind = kind
		self.is_terminal = is_terminal
		self.base = base
		self.root = root
		self.children = []
		self.parents = []
		self.parent = None
		self.right_child = None
		self.left_child = None

		if base:
			self.value = expr
		else:
			self.value = 0



	# def __init__(self, expression, kind="", is_terminal=False, children=[], parents=[]):
	# 	self.expr = expression
	# 	self.kind = kind
	# 	self.parents = parents
	# 	self.children = children

	# 	self.is_terminal = is_terminal
	# 	self.parent = None
	# 	self.left_child = None
	# 	self.right_child = None

	# def __str__(self):
	# 	return str(self.expr)

	def __repr__(self):
		return "Node(%s,%s)" % (self.expr, self.kind)

	# def __le__(self, other):
	# 	""" A <= B: sets A the parent of B and B child of A """
	# 	if other not in self.children:
	# 		self.children.append(other)
	# 	if self not in other.parents:
	# 		other.parents.append(self)

	# def __le__(self, other):
	# 	""" A <= B: sets A the parent of B and B child of A """
	# 	if other not in self.children:
	# 		self.children.append(other)
	# 	if self not in other.parents:
	# 		other.parents.append(self)

	# def __contains__(self, other):
	# 	""" A in B: checks if A is a child of B """
	# 	return True if other in self.children else False

	# def __len__(self):
	# 	""" len(self): returns number of children """
	# 	return len(self.children)

	# def __iter__(self):
	# 	""" iter(self): returns list of children """
	# 	return iter(self.children)

	def right(self, child):
		self.right_child = child
		child.parent = self

	def left(self, child):
		self.left_child = child
		child.parent = self

	def eval(self, value):
		self.value = value

