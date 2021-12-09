from entities.nfa import empty, single, union, kleene_star, concatenation

def thompson(t):
    """Create a nondeterministic finite automaton from the given abstract syntax tree."""

    if t.type == 'e':
        return empty()

    if t.type == 's':
        return single(t.label)
        
    if t.type == 'u':
        nfa1 = thompson(t.left)
        nfa2 = thompson(t.right)
        
        return union(nfa1, nfa2)
        
    if t.type == 'k':
        nfa1 = thompson(t.left)
        
        return kleene_star(nfa1)
        
    if t.type == 'c':
        nfa1 = thompson(t.left)
        nfa2 = thompson(t.right)
        
        return concatenation(nfa1, nfa2)