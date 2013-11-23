# -----------------------------------------------------------------------------
# optimizer.py
# Created by Ingrid Avendano 11/17/13.
# -----------------------------------------------------------------------------
# Node class and Tree made from Tokens defined in grammar module.
# -----------------------------------------------------------------------------

class Node(object):
	def __init__(self, token, pin=False, gate=False, root=False):
		self.parents = []
		self.children = []
		self.gate = gate
		self.pin = pin
		self.root = root
		self.level = 0
		self.weight = 0
		self.x = 0
		self.y = 0

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

		for child in children:
			if self not in child.parents:
				child.parents.append(self)

# -----------------------------------------------------------------------------
# Cluster and Level hold Nodes that are at the same level in AST.
# -----------------------------------------------------------------------------

class Level(object):
	""" Level to hold Nodes. """

	def __init__(self, depth, *clusters):
		self.depth = depth
		self.clusters = clusters


# -----------------------------------------------------------------------------
# Tree that holds all Nodes and has extra attributes listed about the tree.
# -----------------------------------------------------------------------------

class Tree(object):
	""" Tree of Nodes. """

	def __init__(self, root_token, expression=""):
		""" Takes a root Token from parser and converts it to Node tree. """

		# ---------------------------------------------------------------------
		# Go through Tokens and convert them to Nodes, find depth of tree.
		# ---------------------------------------------------------------------

		def reorganize(token): 
			""" Organize tree of Nodes out of tokens and gives depth. """

			# checks if the token is the top of a tree
			if token.kind == 'EQUALS':

				# asssign left Token as the new_node which is now top of tree
				new_node = Node(token.left, pin=True, root=True)

				# recursively go through new_node to find children
				new_child_node = reorganize(token.right)
				new_node.add(new_child_node)

			# if token if not at the top of tree just look for children
			else:
				# checks if new_node is a nonterminal and returns new_node
				if token.kind == 'ID' or token.kind == 'LITERAL':
					return Node(token, pin=True)

				new_node = Node(token, gate=True)
				
				# recursively checks for right Tokens
				if token.right:
					new_child_node = reorganize(token.right)
					new_node.add(new_child_node)
				
				# recursively checks for left Tokens
				if token.left:
					new_child_node = reorganize(token.left)

					# OPTIMIZE PART
					# left child Token might be the same kind as root Token
					# if so, don't add the child Token, just add its children
					if token.left.kind == token.kind:
						new_node.children += new_child_node.children
					else: 
						new_node.add(new_child_node)

			return new_node


		def find_depth(node, depth=0):
			""" Determines the depth of a tree based on its nodes. """
			deepest_depth = depth 

			for child in node.children:
				new_depth = find_depth(child, depth + 1)

				if new_depth > deepest_depth:
					deepest_depth = new_depth

			# this function also sets the depth level of a node
			node.level = depth

			return deepest_depth

		def find_nodes(node, list_of_nodes=[]):
			""" Determines the depth of a tree and weight of nodes. """
			list_of_nodes.append(node)

			# adds weight of 1 if this is a pin Node
			weight = 1 if (node.pin and not node.root) else 0

			for child in node.children:
				list_of_nodes = find_nodes(child, list_of_nodes)
				weight += child.weight

			# sets the weight for node based on children
			node.weight = weight

			return list_of_nodes

		def find_base_nodes(nodes, base):
			base_nodes = []

			for node in nodes:
				if node.pin == base:
					base_nodes.append(node)

			return base_nodes

		def find_levels(nodes, depth):
			""" Determines how many nodes go into each level. """
			levels = [[] for i in range(depth)]

			for node in nodes:
				levels[node.level].append(node)

			return levels

		def find_clusters_by_level(node, levels):
			""" Determines the depth of a tree based on its nodes. """
			
			for child in node.children:
				levels = find_clusters_by_level(child, levels)

			# this should not be an okay way to do this
			if node.level == 0:
				levels[0] = [[node],]
				levels[1].append(node.children)
			else:
				if not node.pin:
					levels[node.level+1].append(node.children)
			return levels

		# ---------------------------------------------------------------------

		self.expr 			= expression
		self.root 			= reorganize(root_token)
		self.depth 			= find_depth(self.root) + 1
		self.nodes 			= find_nodes(self.root)
		self.nonterminals 	= find_base_nodes(self.nodes, True)
		self.terminals 		= find_base_nodes(self.nodes, False)
		self.levels 		= find_levels(self.nodes, self.depth)
		layers				= [[] for i in range(self.depth)]
		self.clusters 		= find_clusters_by_level(self.root, layers)
		self.weight 		= self.root.weight

		self.find_node_positions()
	# -------------------------------------------------------------------------

	def find_node_positions(self):

		for level in self.levels:
			print len(level)
			for cell in level:
		
		# def x_y_positions(node):

		# 	for child in node.children:



	def print_tree(self):
		""" Prints each Node in tree in tree like structure to console. """ 

		def print_node(node, indent=0):
			""" Print a node that has children. """
			print '\t'*indent, node
			indent += 1
			for child in node.children:
				print_node(child, indent)

		print_node(self.root)

	def print_nodes(self):
		""" Prints a life of each Node to console. """ 
		for node in self.nodes:
			print node, node.gate

	def print_levels(self):
		for i in range(self.depth):
			print i, self.levels[i]
