import unittest
from entities.nfa import empty, single, union, concatenation, kleene_star
from algorithms.rabin_scott import rabin_scott
from props import alphabet

class TestRabinScott(unittest.TestCase):
    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_consisting_of_empty_transition(self):
        nfa = empty()
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = {}
        for symbol in alphabet:
            transitionsShouldBe[symbol] = [2, 2]
        
        self.assertSetEqual(dfa.states, {1, 2})
        self.assertDictEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [1])

    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_consisting_of_single_transition(self):
        nfa = single('a')
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = {}
        for symbol in alphabet:
            transitionsShouldBe[symbol] = [3, 3, 3]
        
        # Transition 1 -> 2 with a
        transitionsShouldBe['a'][0] = 2
        
        self.assertSetEqual(dfa.states, {1, 2, 3})
        self.assertDictEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [2])

    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_having_multiple_parallel_transitions(self):
        nfa1 = single('a')
        nfa2 = single('b')
        nfa = union(nfa1, nfa2)
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = {}
        for symbol in alphabet:
            transitionsShouldBe[symbol] = [4, 4, 4, 4]
        
        # Transitions 1 -> 2 with a and 1 -> 3 with b
        transitionsShouldBe['a'][0] = 2
        transitionsShouldBe['b'][0] = 3
        
        self.assertSetEqual(dfa.states, {1, 2, 3, 4})
        self.assertDictEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [2, 3])

    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_having_multiple_sequential_transitions(self):
        nfa1 = single('a')
        nfa2 = single('b')
        nfa = concatenation(nfa1, nfa2)
        dfa = rabin_scott(nfa)
        
        transitionsShouldBe = {}
        for symbol in alphabet:
            transitionsShouldBe[symbol] = [3, 3, 3, 3]
        
        # Transitions 1 -> 2 with a and 2 -> 4 with b
        transitionsShouldBe['a'][0] = 2
        transitionsShouldBe['b'][1] = 4
        
        self.assertSetEqual(dfa.states, {1, 2, 3, 4})
        self.assertDictEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [4])
        
    def test_rabin_scott_algorithm_creates_correct_dfa_from_nfa_having_looping_transitions(self):
        nfa1 = single('a')
        nfa2 = kleene_star(nfa1)
        dfa = rabin_scott(nfa2)
        
        transitionsShouldBe = {}
        for symbol in alphabet:
            transitionsShouldBe[symbol] = [3, 3, 3]
        
        # Transitions 1 -> 2 with a and 2 -> 2 with a
        transitionsShouldBe['a'][0] = 2       
        transitionsShouldBe['a'][1] = 2       
        
        self.assertSetEqual(dfa.states, {1, 2, 3})
        self.assertDictEqual(dfa.transitions, transitionsShouldBe)
        self.assertEqual(dfa.start_state, 1)
        self.assertListEqual(dfa.accept_state, [1, 2])