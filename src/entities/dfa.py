from props import alphabet

class DFA:
    """Class representing deterministic finite automaton.

    Attributes:
        states: set of integers presenting set of states
        transitions: two dimensional array of strings, representing set of transitions. String at
            row i and column j represents transition i -> j with any symbol character in the string
            (i, j).
        start state: integer representing start state of DFA
        accept state: list of integers representing accept state of DFA
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
        """Adds a new state to DFA.

        The new state is indexed as i + 1, which simultaneously becomes as the new largest index.
        In addition, new row and column are added to transition array.

        Returns:
            Index of the new state.

        """

        self.i += 1
        self.states.add(self.i)

        for terminal_list in self.transitions:
            terminal_list.append(None)

        self.transitions.append([None]*self.i)

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

        if self.transitions[state1-1][state2-1] is None:
            self.transitions[state1-1][state2-1] = symbol
        else:
            self.transitions[state1-1][state2-1] += symbol

    def match(self, string):
        """Tests if given string belongs to language formed by DFA.

        Initially, start state is set as current state. Then, for each character in the given
        string, a new currect state is searched from transition array. After scanning the whole
        string, if current state is in the set of accept states, string is accepet, else rejected.

        Args:
            string (str): string to be matched

        Returns:
            True if string belongs to language formed by DFA
            False if string does not belong to language formed by DFA

        """

        current_state = self.start_state

        for char in string:
            new_state = 0

            for symbols in self.transitions[current_state-1]:
                new_state += 1

                if symbols is None:
                    continue

                if char in symbols:
                    current_state = new_state

        if current_state in self.accept_state:
            return True

        return False
