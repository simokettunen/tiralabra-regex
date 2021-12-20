from props import alphabet

def empty():
    """Constructs a nondeterministic finite automaton that has only epsilon move.

    Returns:
        NFA with following properties:
        - states: 1, 2
        - transitions: 1 -> 2 with epsilon
        - start state: 1
        - accept state: 2

    """

    nfa = NFA()
    state1 = nfa.add_state()
    state2 = nfa.add_state()
    nfa.add_transition(state1, state2, '.')
    nfa.start_state = state1
    nfa.accept_state = state2

    return nfa

def single(symbol):
    """Constructs a nondeterministic finite automatons from the given symbol.

    Args:
        symbol (str): single symbol character belonging to alphabet

    Returns:
        NFA with following properties:
        - states: 1, 2
        - transitions: 1 -> 2 with the given input symbol
        - start state: 1
        - accept state: 2

    Raises:
        Exception if symbol is not a single character.
        Exception if symbol does not belong to alphabet.

    """

    if not len(symbol) == 1:
        raise Exception('Argument must be a single symbol.')

    if not symbol in alphabet:
        raise Exception(f'Symbol {symbol} does not belong to alphabet.')

    nfa = NFA()
    state1 = nfa.add_state()
    state2 = nfa.add_state()
    nfa.add_transition(state1, state2, symbol)
    nfa.start_state = state1
    nfa.accept_state = state2

    return nfa

def union(nfa1, nfa2):
    """Combines two given nondeterministic finite automaton with union operator.

    Args:
        nfa1 (NFA): any nondeterministic finite automaton
        nfa2 (NFA): any nondeterministic finite automaton

    Returns:
        NFA with following properties:
        - states: union of states from nfa1, nfa2 and two new states (let us denote new states as A
          and B)
        - transitions: union of transitions from nfa1, nfa2 and four new transitions:
            - A -> start state of nfa1 with epsilon
            - A -> start state of nfa2 with epsilon
            - accept state of nfa1 -> B with epsilon
            - accept state of nfa2 -> B with epsilon
        - start state: A
        - accept state: B

    Raises:
        Exception if both arguments are not instances of class NFA.

    """

    if not isinstance(nfa1, NFA) or not isinstance(nfa2, NFA):
        raise Exception('Both arguments must be instances of class NFA.')

    nfa = NFA()
    nfa.i = nfa1.i + nfa2.i
    nfa2.increase_by_i(nfa1.i)

    nfa.states = nfa.states.union(nfa1.states)
    nfa.states = nfa.states.union(nfa2.states)

    nfa.transitions.extend(nfa1.transitions)
    nfa.transitions.extend(nfa2.transitions)

    state1 = nfa.add_state()
    state2 = nfa.add_state()

    nfa.add_transition(state1, nfa1.start_state, '.')
    nfa.add_transition(state1, nfa2.start_state, '.')
    nfa.add_transition(nfa1.accept_state, state2, '.')
    nfa.add_transition(nfa2.accept_state, state2, '.')

    nfa.start_state = state1
    nfa.accept_state = state2

    return nfa

def kleene_star(nfa1):
    """Applies Kleene star operator on the given nondeterministic finite automaton.

    Args:
        nfa1: any nondeterministic finite automaton

    Returns:
        NFA with following properties:
        - states: union of states from nfa1 and two new states (let us denote new states as A and
          B)
        - transitions: union of transitions from nfa and for new transitions:
            - A -> start state of nfa1 with epsilon
            - accept state of nfa1 -> B with epsilon
            - A -> B with epsilon
            - accept state of nfa1 -> start state of nfa1 with epsilon
        - start state: A
        - accept state: B

    Raises:
        Exception if the argument is not instance of class NFA.

    """

    if not isinstance(nfa1, NFA):
        raise Exception('The argument must be instance of class NFA.')

    nfa = NFA()
    nfa.i = nfa1.i

    state1 = nfa.add_state()
    state2 = nfa.add_state()

    nfa.states = nfa.states.union(nfa1.states)
    nfa.transitions.extend(nfa1.transitions)

    nfa.add_transition(state1, nfa1.start_state, '.')
    nfa.add_transition(nfa1.accept_state, state2, '.')
    nfa.add_transition(state1, state2, '.')
    nfa.add_transition(nfa1.accept_state, nfa1.start_state, '.')

    nfa.start_state = state1
    nfa.accept_state = state2

    return nfa

def concatenation(nfa1, nfa2):
    """Combines two given nondeterministic finite automatons with concatenation operator.

    Args:
        nfa1: any nondeterministic finite automaton
        nfa2: any nondeterministic finite automaton

    Returns:
        NFA with following properties:
        - states: union of states from nfa1 and nfa2
        - transitions: union of transitions from nfa1 and nfa2 and a new transition:
            - accept state of nfa1 -> start state of nfa2 with epsilon
        - start state: start state of nfa1
        - accept state: accept state of nfa2

    Raises:
        Exception if both arguments are not instances of class NFA.

    """

    if not isinstance(nfa1, NFA) or not isinstance(nfa2, NFA):
        raise Exception('Both arguments must be instances of class NFA.')

    nfa = NFA()
    nfa.i = nfa1.i + nfa2.i
    nfa2.increase_by_i(nfa1.i)

    nfa.states = nfa.states.union(nfa1.states)
    nfa.states = nfa.states.union(nfa2.states)

    nfa.transitions.extend(nfa1.transitions)
    nfa.transitions.extend(nfa2.transitions)

    nfa.add_transition(nfa1.accept_state, nfa2.start_state, '.')

    nfa.start_state = nfa1.start_state
    nfa.accept_state = nfa2.accept_state

    return nfa

class NFA:
    """Class representing nondeterministic finite automaton.

    Attributes:
        states: set of integers presenting set of states
        transitions: list of 3-lists, representing set of transitions. For example, 3-list
            [1, 2, 'a'] represents transition 1 -> 2 with symbol a
        start state: integer representing start state of NFA
        accept state: integer representing accept state of NFA
        i: largest index of state indices

    """

    def __init__(self):
        self.states = set()
        self.transitions = []
        self.start_state = None
        self.accept_state = None
        self.i = 0

    def __str__(self):
        return f'\n{self.states}\n{self.transitions}\n{self.start_state}\n{self.accept_state}'

    def add_state(self):
        """Adds a new state to NFA.

        The new state is indexed as i + 1, which simultaneously becomes as the new largest index.

        Returns:
            Index of the new state.

        """

        self.i += 1
        self.states.add(self.i)
        return self.i

    def add_transition(self, state1, state2, symbol):
        """Adds a new transition to NFA.

        Args:
            state1: any NFA's state
            state2: any NFA's state
            label: any symbol in the alphabet

        Raises:
            Exception, if either of the given states does not belong to set of NFA's states.
            Exception, if the given symbol does not belong to alphabet or it not a dot
                denoting epsilon move).

        """

        if not state1 in self.states or not state2 in self.states:
            raise Exception('Both states must belong to set of NFA\'s states')

        if not (symbol in alphabet or symbol == '.'):
            raise Exception('The given symbol must belong to alphabet or be a dot .')

        self.transitions.append([state1, state2, symbol])

    def increase_by_i(self, i):
        """Increases all the state indices by the given integer.

        Args:
            i (int): integer to be added to all state indices.

        """

        self.states = {i+j for j in self.states}

        transitions = []

        for transition in self.transitions:
            transitions.append([transition[0]+i, transition[1]+i, transition[2]])

        self.transitions = transitions

        if self.start_state is not None:
            self.start_state += i
  
        if self.accept_state is not None:
            self.accept_state += i

        self.i += i

    def eps_closure(self, states):
        """Compute all reachable states on only epsilon transitions from the given set states.

        Args:
            states (set): subset of NFA's states

        Returns:
            Set of states reachable from the given set of states on epsilon transitions only.

        Raises:
            Exception if any of the given states does not belong to the set of states of NFA.

        """

        for state in states:
            if not state in self.states:
                raise Exception(f'State {state} does not belong to the set of states of NFA.')

        stack = states
        closure = set(states)

        while stack:
            state = stack.pop()

            for transition in self.transitions:
                if transition[0] == state and transition[2] == '.' and not transition[1] in closure:
                    closure.add(transition[1])
                    stack.append(transition[1])

        return closure

    def move(self, states, symbol):
        """Compute all states, for which there exists transition from the given set of states with given symbol.

        Args:
            state (set): set of ints, representing set of states from which transitions are computed
            symbol: symbol which performs transition

        Returns:
            Set of states for which there exists transition from the given state with given symbol.

        Raises:
            Exception if any of the given states does not belong to set of states of NFA,
            Exception if the given symbol does not belong to alphabet.

        """

        for state in states:
            if not state in self.states:
                raise Exception('The given state must belong to set of states of NFA.')

        if not symbol in alphabet:
            raise Exception('The given symbol must belong to alphabet')

        states_having_transition = set()

        for transition in self.transitions:
            if transition[0] in states and transition[2] == symbol:
                states_having_transition.add(transition[1])

        return states_having_transition
