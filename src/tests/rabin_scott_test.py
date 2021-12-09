import unittest
from entities.nfa import empty, single, union, concatenation, kleene_star
from algorithms.rabin_scott import rabin_scott

class TestRabinScott(unittest.TestCase):
    def setUp(self):
        self.terminals = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        
    def filtered_terminals(self, terminals):
        """Filter the given terminals from self.terminals"""
        return ''.join(list(filter(lambda c : not c in terminals, self.terminals)))
        
    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_consisting_of_empty_transition(self):
        nfa = empty()
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = [
            [None, self.terminals],
            [None, self.terminals],
        ]
        
        self.assertSetEqual(dfa.states, {1, 2})
        self.assertListEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [1])

    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_consisting_of_single_transition(self):
        nfa = single('a')
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = [
            [None, 'a', self.filtered_terminals('a')],
            [None, None, self.terminals],
            [None, None, self.terminals],
        ]
        
        self.assertSetEqual(dfa.states, {1, 2, 3})
        self.assertListEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [2])

    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_having_multiple_parallel_transitions(self):
        nfa1 = single('a')
        nfa2 = single('b')
        nfa = union(nfa1, nfa2)
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = [
            [None, 'a', 'b', self.filtered_terminals('ab')],
            [None, None, None, self.terminals],
            [None, None, None, self.terminals],
            [None, None, None, self.terminals],
        ]
        
        self.assertSetEqual(dfa.states, {1, 2, 3, 4})
        self.assertListEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [2, 3])

    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_having_multiple_sequential_transitions(self):
        nfa1 = single('a')
        nfa2 = single('b')
        nfa = concatenation(nfa1, nfa2)
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = [
            [None, 'a', self.filtered_terminals('a'), None],
            [None, None, self.filtered_terminals('b'), 'b'],
            [None, None, self.terminals, None],
            [None, None, self.terminals, None],
        ]
        
        self.assertSetEqual(dfa.states, {1, 2, 3, 4})
        self.assertListEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [4])
        
    def rabin_scott_algorithm_creates_correct_dfa_from_nfa_having_looping_transitions(self):
        nfa1 = single('a')
        nfa2 = kleene_star(nfa1)
        dfa = rabin_scott(nfa2)
        
        transitionsShouldBe = [
            [None, 'a', self.filtered_terminals('a')],
            [None, 'a', self.filtered_terminals('a')],
            [None, None, self.terminals],
        ]
        
        self.assertSetEqual(dfa.states, {1, 2, 3})
        self.assertListEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [2])