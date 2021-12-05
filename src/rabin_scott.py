from dfa import DFA
from nfa import NFA

def set_to_bit_string(s, i):
    """TODO"""
    
    x = ''
    
    for j in range(1,i+1):
        if j in s:
            x += '1'
        else:
            x += '0'
    
    return x

def rabin_scott(nfa):
    """Create a deterministic finite automaton from the given nondeterministic finite automaton."""

    states_handled = []
    states_unhandled = []
    states_with_bit_string = {}
    initial_eps_closure = nfa.eps_closure([nfa.start_state])
    states_handled.append(initial_eps_closure)
    
    i = 0
    i += 1
    states_with_bit_string[set_to_bit_string(initial_eps_closure, nfa.i)] = i
    
    transitions = []
    accept_states = []
    
    if nfa.accept_state in initial_eps_closure:
        accept_states.append(i)
        
    while states_handled:
        state = states_handled.pop()
        states_unhandled.append(state)
        
        for x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            eps_closure = nfa.eps_closure(list(nfa.move(list(state), x)))
            
            if not (eps_closure in states_unhandled or eps_closure in states_handled):
                states_handled.append(eps_closure)
                i += 1
                states_with_bit_string[set_to_bit_string(eps_closure, nfa.i)] = i
                
                if nfa.accept_state in eps_closure:
                    accept_states.append(i)
                    
            s1 = states_with_bit_string[set_to_bit_string(state, nfa.i)]            
            s2 = states_with_bit_string[set_to_bit_string(eps_closure, nfa.i)]    
            transitions.append([s1, s2, x])
            
    states = list(states_with_bit_string.values())
    dfa = DFA()
    
    for i in states:
        dfa.add_state()
        
    for i in transitions:
        dfa.add_transition(i[0], i[1], i[2])
    
    dfa.start_state = states_with_bit_string[set_to_bit_string(initial_eps_closure, nfa.i)]
    dfa.accept_state = accept_states

    return dfa