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
		self.parent = None
		self.right_child = None
		self.left_child = None

		# set the value of the node to its expression
		if base:
			self.value = expr
		else:
			# self.eval()
			self.value = 0

	def __repr__(self):
		return "Node(%s,%s)" % (self.expr, self.kind)

	def right(self, child):
		""" set right child of node """
		self.right_child = child
		child.parent = self

	def left(self, child):
		""" set left child of node """
		self.left_child = child
		child.parent = self

	def eval(self, value):
		# if kind == "EQUALS":
		self.value = value

class TopNode(Node):
	pass

class NotNode(Node):
	pass

class AndNode(Node):
	pass

class OrNode(Node):
	pass

class XorNode(Node):
	pass 

class VariableNode(Node):
	pass


# tree of tokens
def Tree(object):
	def __init__(self, list_of_tokens):
		self.tokens = list_of_tokens


