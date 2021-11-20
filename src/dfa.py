class DFA:
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
        self.i += 1
        self.states.add(self.i)
        return self.i
        
    def add_transition(self, state1, state2, s):
        self.transitions.append([state1, state2, s])
        
    def check_string(self, string):
        current_state = self.start_state
    
        for x in string:
            for transition in self.transitions:
                if transition[0] == current_state and transition[2] == x:
                    current_state = transition[1]
                    break
        
        if current_state in self.accept_state:
            return True
            
        return False