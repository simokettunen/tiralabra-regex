def empty():
    nfa = NFA()
    state1 = nfa.add_state()
    state2 = nfa.add_state()
    nfa.add_transition(state1, state2, '.')
    nfa.start_state = state1
    nfa.accept_state = state2
    
    return nfa
    
def single(c):
    nfa = NFA()
    state1 = nfa.add_state()
    state2 = nfa.add_state()
    nfa.add_transition(state1, state2, c)
    nfa.start_state = state1
    nfa.accept_state = state2
    
    return nfa
                
def union(nfa1, nfa2):
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
    def __init__(self):
        self.states = set()
        self.transitions = []
        self.start_state = None
        self.accept_state = None
        
        # largest index of any NFA's node
        self.i = 0
        
    def __str__(self):
        return f'\n{self.states}\n{self.transitions}\n{self.start_state}\n{self.accept_state}'
        
    def add_state(self):
        self.i += 1
        self.states.add(self.i)
        return self.i
        
    def add_transition(self, state1, state2, s):
        self.transitions.append([state1, state2, s])
        
    def increase_by_i(self, i):
        # adds i for all state ids in the NFA
        
        self.states = {i+j for j in self.states}
        
        transitions = []
        
        for transition in self.transitions:
            transitions.append([transition[0]+i, transition[1]+i, transition[2]])
        
        self.transitions = transitions
        
        if not self.start_state is None:
            self.start_state += i
            
        if not self.accept_state is None:
            self.accept_state += i
        
        self.i += i
        
    def eps_closure(self, s):
        stack = s
        closure = set(s)
        
        while stack:
            t = stack.pop()
            
            for transition in self.transitions:
                if transition[0] == t and transition[2] == '.' and not transition[1] in closure:
                    closure.add(transition[1])
                    stack.append(transition[1])
                    
        return closure
        
    def move(self, s, x):
        states = set()
        
        for transition in self.transitions:
            if transition[0] in s and transition[2] == x:
                states.add(transition[1])
                
        return states