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
		return "%s('%r')" % (self.kind, self.expr)

	def __contains__(self, other):
		""" Checks if other Node is a child 'in' this Node object. """
		return True if other in self.children else False
		
	def __iter__(self):
		""" Returns list of children when iter(self). """
		return iter(self.children)

	def add_child(self, child):
		""" Adds a new child to node. """
		if child not in self.children:
			self.children += [child]

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

class Literal(object):
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
