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
		return "%s(%r)" % (self.kind, self.expr)

	def __contains__(self, other):
		""" Checks if other Node is a child 'in' this Node object. """
		return True if other in [self.left, self.right] else False

	def set_left(self, child):
		""" Set left child of node. """	
		self.left(child)

	def set_right(self, child):
		""" Set right child of node. """
		self.right(child)

# -----------------------------------------------------------------------------

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
	expr = '~'
	left = None

	def __init__(self, child=None):
		self.right = child

class And(Node):
	""" And node. """ 
	kind = 'AND'
	expr = '*'

class Or(Node):
	""" Or node. """ 
	kind = 'OR'
	expr = '+'

class Xor(Node):
	""" Xor node. """ 
	kind = 'XOR'
	expr = '^'

class Id(Node):
	""" Id node. """ 
	kind = 'ID'

	def __init__(self, expr, child=None):
		self.expr = expr
		self.right = child
		self.left = None
		
# -----------------------------------------------------------------------------

class Literal(Node):
	""" Literal node composed of integers, binary and boolean values. """ 
	kind = 'LITERAL'
	left = None
	right = None

	def __init__(self, expr=None):
		print "FUCKKKKKK"
		self.expr = expr

	def __iter__(self):
		""" iter(self): returns the value/expression of the literal node. """
		return iter(self.expr)
