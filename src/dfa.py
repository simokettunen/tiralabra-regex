# TODO: classes DFA and NFA could be inherited from the same super class FA (finite automaton)

class DFA:
    """TODO"""
    
    def __init__(self):
        self.states = set()
        self.transitions = []
        self.start_state = None
        self.accept_state = None
        
        # largest index of any DFA's node
        self.i = 0
        
    def __str__(self):
        return f'\n{self.states}\n{self.transitions}\n{self.start_state}\n{self.accept_state}'
        
    def add_state(self):
        """TODO"""
        
        self.i += 1
        self.states.add(self.i)
        
        for terminal_list in self.transitions:
            terminal_list.append(None)
            
        self.transitions.append([None]*self.i)
        
        return self.i
        
    def add_transition(self, state1, state2, s):
        """TODO"""
        
        if self.transitions[state1-1][state2-1] is None:
            self.transitions[state1-1][state2-1] = s
        else:
            self.transitions[state1-1][state2-1] += s
        
    def match(self, string):
        """TODO"""
        current_state = self.start_state
    
        for char in string:
            new_state = 0
            
            for terminals in self.transitions[current_state-1]:
                new_state += 1
                
                if terminals is None:
                    continue
                
                if char in terminals:
                    current_state = new_state
                    
        if current_state in self.accept_state:
            return True
            
        return False