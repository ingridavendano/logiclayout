# -----------------------------------------------------------------------------
# token.py
# Created by Ingrid Avendano 11/17/13.
#
# Node classes for boolean algebra tokens with left and right children.
# -----------------------------------------------------------------------------

# token class template
class Node(object):
	""" Basic node class for tokens. """ 

	def __init__(self, left=None, right=None, expr=None):
		""" Lets a node set its children immediately when made. """
		self.left = left
		self.right = right
		self.expr = expr

	def __repr__(self):
		""" What is displayed when a node is represented. """
		return "%s('%r')" % (self.kind, self.expr)

	def __contains__(self, other):
		""" Checks if other Node is a child 'in' this Node object. """
		return True if other in [self.left, self.right] else False

	def set_left(self, child):
		""" Set left child of node. """	
		self.left(child)

	def set_right(self, child):
		""" Set right child of node. """
		self.right(child)


class Root(Node):
	""" Root nodes represent the top of a tree of a tree of nodes. """
	kind = 'EXPR'

class Equals(Node):
	""" Equals node.  """ 
	kind = 'EQUALS'
	expr = '='

class Not(Node):
	""" Not node. """ 
	kind = 'NOT'

class And(Node):
	""" And node. """ 
	kind = 'AND'

class Or(Node):
	""" Or node. """ 
	kind = 'OR'

class Xor(Node):
	""" Xor node. """ 
	kind = 'XOR'

class Id(Node):
	""" Id node. """ 
	kind = 'ID'
	def __init__(self, expr, child=None):
		self.expr = expr
		self.child = child

class Literal(Node):
	""" Literal node composed of integers, binary and boolean values. """ 
	kind = 'LITERAL'

	def __init__(self, expr):
		self.expr = expr

	def __repr__(self):
		""" Displayed when a node is represented. """
		return "Node(%s)" % self.expr

	def __iter__(self):
		""" iter(self): returns the value/expression of the literal node. """
		return iter(self.expr)


if __name__ == "__main__":

	a = Literal('1')
	b = Literal('b')
	c = Literal('8')

	d = Not(a,b,c)
	g = Not(a)
	# d.add_child(c)
	print '8' in c
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


