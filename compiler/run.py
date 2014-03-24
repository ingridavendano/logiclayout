# -----------------------------------------------------------------------------
# run.py
# Created by Ingrid Avendano 11/14/13.
# -----------------------------------------------------------------------------
# Run compiler file by sending it a digital logic expression.
# -----------------------------------------------------------------------------

import parser
import serializer
from optimizer import Tree

# -----------------------------------------------------------------------------
# Run PLY yacc in the parser module.
# -----------------------------------------------------------------------------

yacc = parser.run_yacc


def compiler(data, debug=0):
    # empties root of pre-exisiting tokens
    parser.root = []

    # run parser
    yacc.parse(data)
    tree = None

    # catches errors of bad data expressions
    try:
        parser.root[0]
        tree = Tree(parser.root[0], data)

        # print working tree in debug mode
        if debug:
            tree.print_tree()
            tree.print_nodes()

        # second catch for bad data of a list of literals
        if len(tree.nodes) == 1:
            tree = None

    # return an empty tree if the parser is empty
    except IndexError:
        print "Error: expression is bad"

    return serializer.to_json(tree, debug=debug)
