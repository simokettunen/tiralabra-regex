from entities.dfa import DFA
from entities.nfa import NFA
from props import alphabet

def bit_string(integers, n):
    """Calculates a bit string of the given set of integers.

    Args:
        integers (set): set of integers
        n: maximum length of bit string

    Returns:
        Bit string, where bit at position i has value 0 if i is not in the given set of integers,
        and value 1 if i is in the given set opf integers.

    """

    string = ''

    for i in range(1, n+1):
        if i in integers:
            string += '1'
        else:
            string += '0'

    return string

def rabin_scott(nfa):
    """Creates a deterministic finite automaton from the given nondeterministic finite automaton.

    Initially, eps-closure of NFA's start state is calculated and this becomes the only DFA's state
    so far. Then, for every symbol in alphabet, eps-closure of set of all states reachable from any
    state in initial eps-closure by transition with that symbol is computed. If the computation
    yields any new eps-closure, then it is added as a new DFA's state and stored for upcoming
    computations. The process is continued until all eps-closures are handled. Finally, DFA is
    constructed by using data computed in the process.

    Args:
        nfa (NFA): Nondeterministic finite automaton

    Returns:
        Deterministic finite automaton accepting the same language as the given nondeterministic
        finite automaton.

    Raises:
        Exception if argument is not instance of class NFA.

    """

    if not isinstance(nfa, NFA):
        raise Exception('Argument must be instance of class NFA.')

    dfa_states_unhandled = []
    dfa_states_handled = []
    dfa_states = {}
    dfa_accept_states = []
    dfa_transitions = []

    # Computation of data for construction of DFA

    # Compute initial eps-closure from NFA's start state
    initial_eps_closure = nfa.eps_closure([nfa.start_state])

    # Store computed initial eps-closure and mark it as unhandled
    i = 1
    dfa_states[bit_string(initial_eps_closure, nfa.i)] = i
    dfa_states_unhandled.append(initial_eps_closure)

    # If NFA's accept state is in the eps-closure, the eps-closure must be in one of DFA's accept
    # states
    if nfa.accept_state in initial_eps_closure:
        dfa_accept_states.append(i)
        
    while dfa_states_unhandled:
    
        # Mark popped eps-closure as handled
        state = dfa_states_unhandled.pop()
        dfa_states_handled.append(state)

        for symbol in alphabet:
            
            # First, compute all states, for which there exists transition from any state in
            # eps-closure. Then compute eps-closure of the set of states.
            eps_closure = nfa.eps_closure(list(nfa.move(list(state), symbol)))

            # Check if computation yielded new eps-closure
            if not (eps_closure in dfa_states_unhandled or eps_closure in dfa_states_handled):
            
                # New eps-closure found so store it and mark as unhandled
                i += 1
                dfa_states[bit_string(eps_closure, nfa.i)] = i
                dfa_states_unhandled.append(eps_closure)

                # If NFA's accept state is in the eps-closure, the eps-closure must be in one of
                # DFA's accept states
                if nfa.accept_state in eps_closure:
                    dfa_accept_states.append(i)

            # DFA must have a transition from eps-closure under investigation to computed eps-closure by
            # transition with symbol
            state1 = dfa_states[bit_string(state, nfa.i)]            
            state2 = dfa_states[bit_string(eps_closure, nfa.i)]    
            dfa_transitions.append([state1, state2, symbol])

    # Construction of the DFA

    dfa = DFA()

    for _ in list(dfa_states.values()):
        dfa.add_state()

    for t in dfa_transitions:
        dfa.add_transition(t[0], t[1], t[2])

    dfa.start_state = dfa_states[bit_string(initial_eps_closure, nfa.i)]
    dfa.accept_state = dfa_accept_states

    return dfa
