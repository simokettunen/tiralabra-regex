import unittest
from entities.dfa import DFA
from props import alphabet

def create_transitions(n):
    transitions = {}
    
    for symbol in alphabet:
        transitions[symbol] = [None]*n
        
    return transitions

class TestDFA(unittest.TestCase):
    def test_adding_one_state_to_dfa_works(self):
        dfa = DFA()
        dfa.add_state()
        transitions = create_transitions(1)
        
        self.assertSetEqual(dfa.states, {1})
        self.assertDictEqual(dfa.transitions, transitions)
        self.assertIsNone(dfa.start_state)
        self.assertIsNone(dfa.accept_state)
        
    def test_adding_two_states_to_dfa_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        transitions = create_transitions(2)
        
        self.assertSetEqual(dfa.states, {1, 2})
        self.assertDictEqual(dfa.transitions, transitions)
        self.assertIsNone(dfa.start_state)
        self.assertIsNone(dfa.accept_state)
        
    def test_adding_one_transition_to_dfa_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        transitions = create_transitions(2)
        transitions['a'][1-1] = 2
        
        self.assertSetEqual(dfa.states, {1, 2})
        self.assertDictEqual(dfa.transitions, transitions)
        self.assertIsNone(dfa.start_state)
        self.assertIsNone(dfa.accept_state)
        
    def test_adding_two_transitions_to_dfa_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(2, 3, 'b')
        transitions = create_transitions(3)
        transitions['a'][1-1] = 2
        transitions['b'][2-1] = 3
        
        self.assertSetEqual(dfa.states, {1, 2, 3})
        self.assertDictEqual(dfa.transitions, transitions)
        self.assertIsNone(dfa.start_state)
        self.assertIsNone(dfa.accept_state)
        
    def test_adding_three_transitions_to_dfa_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(2, 3, 'b')
        dfa.add_transition(1, 3, 'c')
        transitions = create_transitions(3)
        transitions['a'][1-1] = 2
        transitions['b'][2-1] = 3
        transitions['c'][1-1] = 3
        
        self.assertSetEqual(dfa.states, {1, 2, 3})
        self.assertDictEqual(dfa.transitions, transitions)
        self.assertIsNone(dfa.start_state)
        self.assertIsNone(dfa.accept_state)

    def test_matching_with_dfa_consisting_of_single_transition_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.start_state = 1
        dfa.accept_state = [2]
        
        self.assertTrue(dfa.match('a'))

    def test_matching_with_dfa_having_branch_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(1, 3, 'b')
        dfa.start_state = 1
        dfa.accept_state = [2]
        
        self.assertTrue(dfa.match('a'))
        self.assertFalse(dfa.match('b'))
        
    def test_matching_with_dfa_having_loop_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(2, 1, 'a')
        dfa.start_state = 1
        dfa.accept_state = [2]
        
        self.assertTrue(dfa.match('a'))
        self.assertFalse(dfa.match('aa'))
        
    def test_matching_with_dfa_having_two_sequential_transitions_and_accept_state_in_the_end_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(2, 3, 'b')
        dfa.start_state = 1
        dfa.accept_state = [3]
        
        self.assertTrue(dfa.match('ab'))
        self.assertFalse(dfa.match('a'))
        
    def test_matching_with_dfa_having_two_sequential_transitions_and_accept_state_in_the_middle_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(2, 3, 'b')
        dfa.start_state = 1
        dfa.accept_state = [2]
        
        self.assertFalse(dfa.match('ab'))
        self.assertTrue(dfa.match('a'))