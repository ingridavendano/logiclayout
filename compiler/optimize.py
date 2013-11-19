# -----------------------------------------------------------------------------
# optimizer.py
# Created by Ingrid Avendano 11/17/13.
#
# Optimizer the parser.py output which is a parser trees. 
# -----------------------------------------------------------------------------

from tree import *

def print_parse_tree(root_node, indent=0):
	""" Print node tree where each node has left and right child. """
	print '\t'*indent, ' ', root_node
	indent += 1

	if root_node.left: 
		print "\t"*indent, "LEFT:"
		print_parse_tree(root_node.left, indent)
	if root_node.right:
		print "\t"*indent, "RIGHT:"
		print_parse_tree(root_node.right, indent)


def print_tree(node, indent=0):
	""" Print a node tree that has children. """
	print '\t'*indent, node
	indent += 1

	for child in node.children:
		print_tree(child, indent)
	

def reorganize(root):
	""" Reoganizing abstract syntax tree. """

	if root.kind == 'EQUALS':
		# left node will always be what the tree is assigned as
		new_node = Node(root.left)
		new_child = reorganize(root.right)
		new_node.add(new_child)
	else:
		new_node = Node(root)

		if root.kind != 'ID':
			if root.right:
				new_child = reorganize(root.right)
				new_node.add(new_child)
		
			if root.left:
				new_child = reorganize(root.left)

				# left child might be the same as root
				if root.left.kind == root.kind:
					new_node.children += new_child.children
				else: 
					new_node.add(new_child)
		elif root.kind == 'ID':
			new_node.base = True

	return new_node


