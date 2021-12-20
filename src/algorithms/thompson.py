from entities.nfa import empty, single, union, kleene_star, concatenation

def thompson(tree):
    """Construct a nondeterministic finite automaton from the given parse tree.

    Algorithm works recursively. Union and concatenation are binary operators, so NFAs are
    constructed based on their left and right child node. Kleene star is unary operator, so it has
    only left child node. Empty and single are constructed directly, since they do not have
    child nodes.

    Args:
        tree (Node): Root of the parse tree used to form NFA.
  
    Returns:
        Nondeterministic finite automaton (instance of class NFA) corresponding the given parse
        tree.

    Raises:
        Exception if node type is not empty, single, union, kleene or concatenation.

    """

    if tree.type == 'empty':
        return empty()

    if tree.type == 'single':
        return single(tree.label)

    if tree.type == 'union':
        nfa1 = thompson(tree.left)
        nfa2 = thompson(tree.right)
        return union(nfa1, nfa2)

    if tree.type == 'kleene':
        nfa = thompson(tree.left)
        return kleene_star(nfa)

    if tree.type == 'concatenation':
        nfa1 = thompson(tree.left)
        nfa2 = thompson(tree.right)
        return concatenation(nfa1, nfa2)

    raise Exception(f'Incorrect node type: {tree.type}')
