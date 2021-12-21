import unittest
from entities.dfa import DFA

class TestDFA(unittest.TestCase):
    def test_adding_one_state_to_dfa_works(self):
        dfa = DFA()
        dfa.add_state()
        
        self.assertSetEqual(dfa.states, {1})
        self.assertListEqual(dfa.transitions, [[None]])
        self.assertIsNone(dfa.start_state)
        self.assertIsNone(dfa.accept_state)
        
    def test_adding_two_states_to_dfa_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        
        self.assertSetEqual(dfa.states, {1, 2})
        self.assertListEqual(dfa.transitions, [[None, None], [None, None]])
        self.assertIsNone(dfa.start_state)
        self.assertIsNone(dfa.accept_state)
        
    def test_adding_one_transition_to_dfa_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        
        self.assertSetEqual(dfa.states, {1, 2})
        self.assertListEqual(dfa.transitions, [[None, 'a'], [None, None]])
        self.assertIsNone(dfa.start_state)
        self.assertIsNone(dfa.accept_state)
        
    def test_adding_two_transitions_to_dfa_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(2, 3, 'b')
        
        self.assertSetEqual(dfa.states, {1, 2, 3})
        self.assertListEqual(dfa.transitions, [[None, 'a', None], [None, None, 'b'], [None, None, None]])
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
        
        self.assertSetEqual(dfa.states, {1, 2, 3})
        self.assertListEqual(dfa.transitions, [[None, 'a', 'c'], [None, None, 'b'], [None, None, None]])
        self.assertIsNone(dfa.start_state)
        self.assertIsNone(dfa.accept_state)

    def test_dfa_consisting_of_single_transition_works(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.start_state = 1
        dfa.accept_state = [2]
        
        self.assertTrue(dfa.match('a'))

    def test_dfa_having_branch_works(self):
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
        
    def test_dfa_having_loop_works(self):
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
        
    def test_dfa_having_two_sequential_transitions_and_accept_state_in_the_end_works(self):
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
        
    def test_dfa_having_two_sequential_transitions_and_accept_state_in_the_middle_works(self):
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