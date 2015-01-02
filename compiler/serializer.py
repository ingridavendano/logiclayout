# -----------------------------------------------------------------------------
# Converts AST (abstract syntax tere) to JSON.
# -----------------------------------------------------------------------------
import json
from optimizer import *

# -----------------------------------------------------------------------------


class NodeEncoder(json.JSONEncoder):
    """Encode Node class objects to JSON."""

    def default(self, tree):
        def unknown_node(node):
            return {
                'kind': node.kind,
                'name': node.expr,
                'weight': node.weight,
                'depth': node.level,
                'inputs': len(node.children),
                'x': node.x,
                'y': node.y,
                'nodes': [
                    unknown_node(child) for child in node.children
                ]
            }

        if isinstance(tree, Tree):
            return {
                'depth': tree.depth,
                'weight': tree.root.weight,
                'nodes': [
                    unknown_node(tree.root)
                ]
            }
        else:
            return json.JSONEncoder.default(self, tree)

# -----------------------------------------------------------------------------


def to_json(tree, debug=False):
    """Converts a Node Tree to JSON."""

    # if tree doesn't exist return no json
    if tree is None:
        return tree

    # encodes AST to JSON
    json_string = json.dumps(tree, cls=NodeEncoder)

    # debug mode
    if debug:
        print json_string

    return json_string
