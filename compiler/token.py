# -----------------------------------------------------------------------------
# token.py
# Created by Ingrid Avendano 11/12/13.
#
# Description the Node classes for boolean algebra tokens.
# -----------------------------------------------------------------------------

# token class template
class Node(object):
	""" Basic node class for tokens. """ 

	def __init__(self, *child):
		""" Lets a node set its children immediately when made. """
		self.expr = None
		self.children = []
		self.children += child

	def __repr__(self):
		""" What is displayed when a node is represented. """
		return "Node( %s )" % self.kind

	def __contains__(self, other):
		""" Checks if other Node is a child 'in' this Node object. """
		return True if other in self.children else False
		
	# def __iter__

	def add_child(self, child):
		self.children += [child]



class Root(Node):
	""" Root node that represents the top of a tree of nodes. """
	kind = "EXPR"
	pass

class Equals(Node):
	kind = "EQUALS"
	pass

class Not(Node):
	kind = 'NOT'

class And(Node):
	kind = 'AND'
	pass

class Or(Node):
	kind = 'OR'
	pass

class Xor(Node):
	kind = 'XOR'
	pass 

class Id(Node):
	kind = 'ID'
	pass

class Literal(object):
	kind = "LITERAL"

	def __init__(self, expr):
		self.expr = expr

	def __repr__(self):
		""" Displayed when a node is represented. """
		return "Node(%s)" % self.expr



if __name__ == "__main__":

	a = Literal('1')
	b = Literal('b')
	c = Literal('8')

	d = Not(a,b)
	g = Not(a)
	d.add_child(c)

	print d.children
	print g.children

	# print a in b


	# print not_node
	# print not_node.expr

	# lit_node = Literal("a")
	# print lit_node
	# print lit_node.expr



################################################################################
################################################################################
# THIS CODE WORKS WELL for Node class
	# def __init__(self, expr, kind, is_terminal=False, base=False, root=False):
	# 	self.expr = expr
	# 	self.kind = kind
	# 	self.is_terminal = is_terminal
	# 	self.base = base
	# 	self.root = root
	# 	self.parent = None
	# 	self.right_child = None
	# 	self.left_child = None

	# 	# set the value of the node to its expression
	# 	if base:
	# 		self.value = expr
	# 	else:
	# 		# self.eval()
	# 		self.value = 0

	# def __repr__(self):
	# 	return "Node(%s,%s)" % (self.expr, self.kind)

	# def right(self, child):
	# 	""" set right child of node """
	# 	self.right_child = child
	# 	child.parent = self

	# def left(self, child):
	# 	""" set left child of node """
	# 	self.left_child = child
	# 	child.parent = self

	# def eval(self, value):
	# 	# if kind == "EQUALS":
	# 	self.value = value
################################################################################
################################################################################


# # tree of tokens
# def Tree(object):
# 	def __init__(self, list_of_tokens):
# 		self.tokens = list_of_tokens


