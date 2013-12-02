# -----------------------------------------------------------------------------
# optimizer.py
# Created by Ingrid Avendano 11/17/13.
# -----------------------------------------------------------------------------
# Node class and Tree made from Tokens defined in grammar module.
# -----------------------------------------------------------------------------

class Node(object):
	def __init__(self, token, pin=False, gate=False, root=False, weight=0):
		self.cell = None
		self.children = []
		self.gate = gate
		self.pin = pin
		self.root = root
		self.weight = weight
		self.level = 0
		self.x = 0
		self.y = 0 
		self.y_min = 0 
		self.y_max = 0

		if token.kind == 'LITERAL' or token.kind == 'ID':
			self.expr = token.expr
		else:
			self.expr = token.kind

		if self.root:
			self.kind = 'output'
		elif self.pin: 
			self.kind = 'input'
		else: 
			self.kind = token.kind.lower()

	def __repr__(self):
		""" What is displayed when a node is represented. """
		return "%r" % self.expr

	def __str__(self):
		""" What is displayed when a node is represented. """
		return "%s" % str(self.expr)

	def add(self, *children):
		self.children += children

	def calculate_weight(self):
		for child in self.children:
			self.weight += child.weight

	def calculate_y(self, y_min, y_max):
		self.y_min = y_min
		self.y_max = y_max
		self.y = y_min + (y_max - y_min)/2

# -----------------------------------------------------------------------------
# Cluster and Level hold Nodes that are at the same level in AST.
# -----------------------------------------------------------------------------

class Cell(object):
	""" Cluster is a group of children of a Node. """

	def __init__(self, depth, y_min, y_max, nodes):
		self.x = depth
		self.nodes = nodes

		ticks = 0
		# connects each Node to the cell it belongs to
		for node in nodes:
			ticks += node.weight 

		# this is for determining y-axis positions
		self.y_min = y_min
		self.y_max = y_max

		num_of_nodes = len(nodes)
		y_increment = (y_max - y_min)/ticks

		# print "*"*5
		y_temp_min = y_min

	def __repr__(self):
		""" What is displayed when a node is represented. """
		return "%r (%r,%r)" % (self.nodes, self.y_min, self.y_max)

	def print_nodes(self):
		print "y depth", self.depth
		print self.nodes


class Level(object):
	""" Level to hold Nodes. """

	def __init__(self, depth):
		self.depth = depth
		self.cells = []

	def add(self, cell):
		cell.depth = len(self.cells)
		self.cells.append(cell)

	def print_level(self):
		print "x depth", self.depth
		for cell in self.cells:
			cell.print_nodes()


# -----------------------------------------------------------------------------
# Tree that holds all Nodes and has extra attributes listed about the tree.
# -----------------------------------------------------------------------------

class Tree(object):
	""" Tree of Nodes. """

	def __init__(self, root_token, expression=""):
		""" Takes a root Token from parser and converts it to Node tree. """

		self.nodes = []
		self.depth = 0
		
		# ---------------------------------------------------------------------
		# Go through Tokens and converts them to Nodes, find depth of tree.
		# ---------------------------------------------------------------------

		def convert(token, depth=1): 
			""" Organize tree of Nodes out of tokens and gives depth. """
			print token.terminal
			if token.kind == 'EQUALS':

				# asssign left Token as output pin
				new_node = Node(token.left, pin=True, root=True)

				# recursively go through new_node to find children
				new_child_node = convert(token.right, depth + 1)
				new_node.add(new_child_node)

			elif token.kind == 'ID' or token.kind == 'LITERAL':

				# must be an input pin
				new_node = Node(token, pin=True, weight=1)

				# determines depth of tree
				self.depth = depth if depth > self.depth else self.depth

			else: 
				new_node = Node(token, gate=True)

				# recursively checks for right Tokens
				if token.right:
					new_child_node = convert(token.right, depth + 1)
					new_node.children += [new_child_node]
				
				# recursively checks for left Tokens
				if token.left:
					
					# OPTIMIZE PART
					# left child Token might be the same kind as root Token
					# if so, don't add the child Token, just add its children
					if token.left.kind == token.kind:
						new_child_node = convert(token.left, depth)
						new_node.children += new_child_node.children

					# checks if left child is a gate and applies not function
					elif new_node.kind == 'not' and token.left.terminal:
						if token.left.kind[0].lower() == 'n':
							new_node.kind = token.left.kind[1:].lower()
						else:
							new_node.kind = 'n' + token.left.kind.lower();
						new_child_node = convert(token.left, depth)
						new_node.children += new_child_node.children
					else: 
						new_child_node = convert(token.left, depth + 1)
						new_node.children += [new_child_node]


			new_node.calculate_weight()
			return new_node

		def find_cells(node, depth, y_min, y_max):
			""" Determine which cells each node belongs in. """
			node.calculate_y(y_min, y_max)
			node.level = depth 
			node.x = depth 
			self.nodes.append(node)


			if len(node.children) > 0:
				ticks = node.weight
				increment = (y_max - y_min)/ticks
				print node, y_min, y_max, ticks,  (y_max - y_min), increment

				temp_y_min = y_min
				for child in node.children:
					
					cell_y_min = temp_y_min
					cell_y_max = temp_y_min + (child.weight*increment)
					print "   ", child, child.weight, cell_y_min, cell_y_max

					find_cells(child, depth - 1, cell_y_min, cell_y_max)
					temp_y_min = cell_y_max

				x_depth = node.level - 1
				y_depth = len(self.levels[x_depth])

				new_cell = Cell(y_depth, y_min, y_max, node.children)
				self.levels[x_depth].append(new_cell)

		# ---------------------------------------------------------------------

		self.expr = expression
		self.root = convert(root_token)


		self.levels = [ [] for i in range(self.depth + 1)]
		first_cell = Cell(self.depth - 1, 0.0, 1.0, [self.root])

		self.levels[self.depth - 1].append(first_cell)
		find_cells(self.root, self.depth - 1, 0.0, 1.0)

	# -------------------------------------------------------------------------

	def print_tree(self):
		""" Prints each Node in tree in tree like structure to console. """ 

		def print_node(node, indent=0):
			""" Print a node that has children. """
			print '\t'*indent, node
			indent += 1
			for child in node.children:
				print_node(child, indent)

		print_node(self.root)
		print "depth:", self.depth

	def print_nodes(self):
		""" Prints a life of each Node to console. """ 
		print "Number of nodes:", len(self.nodes)
		print "node", "\tx\t\ty"
		for node in self.nodes:
			print node, '\t', node.y_min, '\t', node.y_max, '\t\t', node.y

	def print_levels(self):
		for i in range(self.depth):
			print i, self.levels[i]
