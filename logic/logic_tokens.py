# -----------------------------------------------------------------------------
# logic_tokens.py
# Created by Ingrid Avendano 11/12/13.
#
# Descript the classes for boolean algebra tokens.
# -----------------------------------------------------------------------------


TYPES = [
	"STATEMENT",
	"EXPRESSION",
	"OPERATOR"
]

# token class template
class Token:
	def __init__(self, expression):
		self.expr = expression
		self.parents = []
		self.children = []

	def __str__(self):
		return self.expr

	def __repr__(self):
		return "'%s'" % self.expr

	def __le__(self, other):
		""" A <= B: sets A the parent of B and B child of A """
		self.children.append(other)
		other.parents.append(self)

	def __contains__(self, other):
		""" A in B: checks if A is a child of B """
		return True if other in self.children else False


# def main():
# 	pass

# if __name__ == "__main__":
# 	main()
