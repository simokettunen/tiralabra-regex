import unittest
from entities.nfa import empty, single, union, concatenation, kleene_star
from algorithms.rabin_scott import rabin_scott
from props import alphabet

class TestRabinScott(unittest.TestCase):
    def setUp(self):
        self.symbols = alphabet
        
    def filtered_symbols(self, symbols):
        """Filter the given symbols from self.symbols"""
        return ''.join(list(filter(lambda c : not c in symbols, self.symbols)))
        
    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_consisting_of_empty_transition(self):
        nfa = empty()
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = [
            [None, self.symbols],
            [None, self.symbols],
        ]
        
        self.assertSetEqual(dfa.states, {1, 2})
        self.assertListEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [1])

    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_consisting_of_single_transition(self):
        nfa = single('a')
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = [
            [None, 'a', self.filtered_symbols('a')],
            [None, None, self.symbols],
            [None, None, self.symbols],
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
            [None, 'a', 'b', self.filtered_symbols('ab')],
            [None, None, None, self.symbols],
            [None, None, None, self.symbols],
            [None, None, None, self.symbols],
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
            [None, 'a', self.filtered_symbols('a'), None],
            [None, None, self.filtered_symbols('b'), 'b'],
            [None, None, self.symbols, None],
            [None, None, self.symbols, None],
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
            [None, 'a', self.filtered_symbols('a')],
            [None, 'a', self.filtered_symbols('a')],
            [None, None, self.symbols],
        ]
        
        self.assertSetEqual(dfa.states, {1, 2, 3})
        self.assertListEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [2])