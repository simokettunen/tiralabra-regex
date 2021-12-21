from props import alphabet

class DFA:
    """Class representing deterministic finite automaton.

    Attributes:
        states: set of integers presenting set of states
        transitions: dictionary where keys are symbols in alphabet. Every key has as its value a
            list having as many items as states. Now transition[x][y] = z represents transition
            (y-1) -> z with symbol x. Minus one because of list indices start with zero.
        start state: integer representing start state of DFA
        accept state: list of integers representing accept state of DFA
        i: largest index of state indices

    """

    def __init__(self):
        self.states = set()
        self.transitions = {}
        self.start_state = None
        self.accept_state = None
        self.i = 0
        
        for symbol in alphabet:
            self.transitions[symbol] = []

    def __str__(self):
        return f'\n{self.states}\n{self.transitions}\n{self.start_state}\n{self.accept_state}'

    def add_state(self):
        """Adds a new state to DFA.

        The new state is indexed as i + 1, which simultaneously becomes as the new largest index.
        In addition, new row and column are added to transition array.

        Returns:
            Index of the new state.

        """

        self.i += 1
        self.states.add(self.i)
        
        for symbol in alphabet:
            self.transitions[symbol].append(None)

        return self.i

    def add_transition(self, state1, state2, symbol):
        """Adds a new transition to DFA.

        Args:
            state1: start state of transition
            state2: end state of transition
            label: symbol for which transition is performed

        Raises:
            Exception, if either of the given states does not belong to set of DFA's states.
            Exception, if the given symbol does not belong to alphabet

        """

        if not state1 in self.states or not state2 in self.states:
            raise Exception('Both states must belong to set of NFA\'s states')
        
        if not symbol in alphabet:
            raise Exception('The given symbol must belong to alphabet')
            
        self.transitions[symbol][state1-1] = state2

    def match(self, string):
        """Tests if given string belongs to language formed by DFA.

        Initially, start state is set as current state. Then, for each character the next state
        is looked from transition table. Finally, if current state is accept state, then accept,
        else reject.

        Args:
            string (str): string to be matched

        Returns:
            True if string belongs to language formed by DFA
            False if string does not belong to language formed by DFA

        """
        
        current_state = self.start_state

        for char in string:
        
            # Skip empty char
            if char == '.':
                continue
        
            # If DFA is not constructed with Rabin-Scott algorithm, reject on character not
            # belonging to alphabet of the language
            if self.transitions[char][current_state-1] is None:
                return False
                
            current_state = self.transitions[char][current_state-1]

        if current_state in self.accept_state:
            return True

        return False
