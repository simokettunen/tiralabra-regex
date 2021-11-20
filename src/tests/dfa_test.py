import unittest
from dfa import DFA

class TestDFA(unittest.TestCase):
    def test_dfa_recognizes_union_operator_correctly(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(1, 3, 'b')
        dfa.start_state = 1
        dfa.accept_state = [2, 3]
        
        self.assertTrue(dfa.check_string('a'))
        self.assertTrue(dfa.check_string('b'))
        
    def test_dfa_recognizes_kleene_star_operator_correctly(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(2, 1, 'a')
        dfa.start_state = 1
        dfa.accept_state = [1, 2]
        
        self.assertTrue(dfa.check_string('a'))
        self.assertTrue(dfa.check_string('aa'))
        
    def test_dfa_recognizes_concatenation_operator_correctly(self):
        dfa = DFA()
        dfa.add_state()
        dfa.add_state()
        dfa.add_state()
        dfa.add_transition(1, 2, 'a')
        dfa.add_transition(2, 3, 'b')
        dfa.start_state = 1
        dfa.accept_state = [3]
        
        self.assertTrue(dfa.check_string('ab'))
        self.assertFalse(dfa.check_string('a'))