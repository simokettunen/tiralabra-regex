from nfa import *

def thompson(t):
    """Create a nondeterministic finite automaton from the given abstract syntax tree."""

    if t.type == 's':
        if t.label == '.':
            return empty()
            
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