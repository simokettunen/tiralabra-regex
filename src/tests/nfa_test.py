import unittest
from nfa import *

class TestNFA(unittest.TestCase):
    def test_empty(self):
        nfa = empty()
        
        self.assertSetEqual(nfa.states, {1, 2})
        self.assertListEqual(nfa.transitions, [[1, 2, '.']])
        self.assertEqual(nfa.start_state, 1)
        self.assertEqual(nfa.accept_state, 2)
        
    def test_single(self):
        nfa = single('a')
        
        self.assertSetEqual(nfa.states, {1, 2})
        self.assertListEqual(nfa.transitions, [[1, 2, 'a']])
        self.assertEqual(nfa.start_state, 1)
        self.assertEqual(nfa.accept_state, 2)
        
    def test_union(self):
        nfa1 = single('a')
        nfa2 = single('b')
        nfa = union(nfa1, nfa2)
        
        self.assertSetEqual(nfa.states, {1, 2, 3, 4, 5, 6})
        self.assertListEqual(nfa.transitions, [[1, 2, 'a'], [3, 4, 'b'], [5, 1, '.'], [5, 3, '.'], [2, 6, '.'], [4, 6, '.']])
        self.assertEqual(nfa.start_state, 5)
        self.assertEqual(nfa.accept_state, 6)
        
    def test_kleene_star(self):
        nfa1 = single('a')
        nfa = kleene_star(nfa1)
        
        self.assertSetEqual(nfa.states, {1, 2, 3, 4})
        self.assertListEqual(nfa.transitions, [[1, 2, 'a'], [3, 1, '.'], [2, 4, '.'], [3, 4, '.'], [2, 1, '.']])
        self.assertEqual(nfa.start_state, 3)
        self.assertEqual(nfa.accept_state, 4)
        
    def test_concatenation(self):
        nfa1 = single('a')
        nfa2 = single('b')
        nfa = concatenation(nfa1, nfa2)
        
        self.assertSetEqual(nfa.states, {1, 2, 3, 4})
        self.assertListEqual(nfa.transitions, [[1, 2, 'a'], [3, 4, 'b'], [2, 3, '.']])
        self.assertEqual(nfa.start_state, 1)
        self.assertEqual(nfa.accept_state, 4)