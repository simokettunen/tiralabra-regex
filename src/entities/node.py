class Node:
    """Class representing node in parse tree.

    Parse tree can be constructed by inserting another nodes as left and right childs.

    Attributes:
        type (string): type of node, can be any of the following:
            empty
            single
            concatenation
            union
            kleene
        label (string): label of node. Label is set automatically . for nodes having type of empty.
            For nodes type of single, label must be provided
        left (Node): Nodes left child. Only nodes having type of concatenation, union and kleene
            have left child.
        right (Node): Right child of node. Only nodes having type of concatenation and union have
            right child.

    """

    def __init__(self, type, label=None, left=None, right=None):
        self.type = type
        self.label = None
        self.left = None
        self.right = None

        if type == 'empty':
            self.label = '.'

        elif type == 'single':

            if label is None:
                raise Exception('Node type of single must have label')

            self.label = label

        elif type == 'kleene':

            if left is None:
                raise Exception('Node type of kleene must have left node')

            self.left = left

        elif type in ['concatenation', 'union']:

            if left is None or right is None:
                raise Exception(f'Node type of {type} must have left and right node')

            self.left = left
            self.right = right

        else:
            raise Exception(f'Incorrect node type: {type}')

    def __str__(self):
        if self.type in ['concatenation', 'kleene', 'union']:
            return f'({self.type[0]} {self.left.__str__()} {self.right.__str__()})'

        if self.label is None:
            return ''

        return self.label
