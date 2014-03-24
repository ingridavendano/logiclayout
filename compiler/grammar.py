# -----------------------------------------------------------------------------
# grammar.py
# Created by Ingrid Avendano 11/17/13.
# -----------------------------------------------------------------------------
# General token class for boolean algebra tokens with left and right children.
# -----------------------------------------------------------------------------


class Token(object):
    """Basic node class for tokens."""
    terminal = True

    def __init__(self, left=None, right=None):
        """Lets a node set its children immediately when made."""
        self.left = left
        self.right = right

    def __repr__(self):
        """What is displayed when a token is represented."""
        return "%s(%r)" % (self.kind, self.expr)

    def __str__(self):
        """String of how token is represented."""
        return str(self.expr)

    def __contains__(self, other):
        """Checks if other Node is a child 'in' this Node object."""
        return True if other in [self.left, self.right] else False

    def set_left(self, child):
        """Set left child of node."""
        self.left(child)

    def set_right(self, child):
        """Set right child of node."""
        self.right(child)

# -----------------------------------------------------------------------------
# List of specified tokens classes below based on grammar for each token.
# -----------------------------------------------------------------------------


class Equals(Token):
    """Equals node."""
    kind = 'EQUALS'
    expr = '='


class Not(Token):
    """Not node takes in only one child."""
    kind = 'NOT'
    expr = '~'
    right = None

    def __init__(self, child=None):
        self.left = child


class And(Token):
    """And node."""
    kind = 'AND'
    expr = '*'


class Nand(Token):
    """Nand node."""
    kind = 'NAND'
    expr = '!*'


class Or(Token):
    """Or node."""
    kind = 'OR'
    expr = '+'


class Nor(Token):
    """Nor node."""
    kind = 'NOR'
    expr = '!+'


class Xor(Token):
    """Xor node."""
    kind = 'XOR'
    expr = '^'


class Nxor(Token):
    """Nxor node."""
    kind = 'NXOR'
    expr = '!^'


class Id(Token):
    """Id node."""
    kind = 'ID'
    terminal = False
    right = None

    def __init__(self, expr, child=None):
        self.expr = expr
        self.left = child


class Literal(Token):
    """Literal node composed of integers, binary and boolean values."""
    kind = 'LITERAL'
    left = None
    right = None
    terminal = False
    base = True

    def __init__(self, expr=None):
        self.expr = expr

    def __iter__(self):
        """iter(self): returns the value/expression of the literal node."""
        return iter(self.expr)


class Break(Token):
    """Meant to catch bad errors."""
    kind = 'BREAK'
    expr = "error"
