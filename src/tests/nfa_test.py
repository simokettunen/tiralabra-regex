import unittest
from nfa import *

class TestNFA(unittest.TestCase):
    def test_nfa_corresponding_to_empty_string_is_created_correctly(self):
        nfa = empty()
        
        self.assertSetEqual(nfa.states, {1, 2})
        self.assertListEqual(nfa.transitions, [[1, 2, '.']])
        self.assertEqual(nfa.start_state, 1)
        self.assertEqual(nfa.accept_state, 2)

    def test_nfa_corresponding_to_single_symbol_is_created_correctly(self):
        nfa = single('a')
        
        self.assertSetEqual(nfa.states, {1, 2})
        self.assertListEqual(nfa.transitions, [[1, 2, 'a']])
        self.assertEqual(nfa.start_state, 1)
        self.assertEqual(nfa.accept_state, 2)

    def test_two_nfas_are_handled_correctly_by_union_operator(self):
        nfa1 = single('a')
        nfa2 = single('b')
        nfa = union(nfa1, nfa2)
        
        self.assertSetEqual(nfa.states, {1, 2, 3, 4, 5, 6})
        self.assertListEqual(nfa.transitions, [[1, 2, 'a'], [3, 4, 'b'], [5, 1, '.'], [5, 3, '.'], [2, 6, '.'], [4, 6, '.']])
        self.assertEqual(nfa.start_state, 5)
        self.assertEqual(nfa.accept_state, 6)

    def test_one_nfa_is_handled_correctly_by_kleene_star_operator(self):
        nfa1 = single('a')
        nfa = kleene_star(nfa1)
        
        self.assertSetEqual(nfa.states, {1, 2, 3, 4})
        self.assertListEqual(nfa.transitions, [[1, 2, 'a'], [3, 1, '.'], [2, 4, '.'], [3, 4, '.'], [2, 1, '.']])
        self.assertEqual(nfa.start_state, 3)
        self.assertEqual(nfa.accept_state, 4)

    def test_two_nfas_are_handled_correctly_by_concatenation_operator(self):
        nfa1 = single('a')
        nfa2 = single('b')
        nfa = concatenation(nfa1, nfa2)
        
        self.assertSetEqual(nfa.states, {1, 2, 3, 4})
        self.assertListEqual(nfa.transitions, [[1, 2, 'a'], [3, 4, 'b'], [2, 3, '.']])
        self.assertEqual(nfa.start_state, 1)
        self.assertEqual(nfa.accept_state, 4)

    def test_eps_closure_accepts_eps_transition(self):
        nfa = NFA()
        nfa.add_state()
        nfa.add_state()
        nfa.add_transition(1, 2, '.')
        
        self.assertSetEqual(nfa.eps_closure([1]), {1, 2})

    def test_eps_closure_rejects_non_eps_transition(self):
        nfa = NFA()
        nfa.add_state()
        nfa.add_state()
        nfa.add_transition(1, 2, 'a')
        
        self.assertSetEqual(nfa.eps_closure([1]), {1})

    def test_eps_closure_handles_eps_and_non_eps_transition_from_same_node_correctly(self):
        nfa = NFA()
        nfa.add_state()
        nfa.add_state()
        nfa.add_state()
        nfa.add_transition(1, 2, '.')
        nfa.add_transition(1, 3, 'a')
        
        self.assertSetEqual(nfa.eps_closure([1]), {1, 2})

    def test_eps_closure_accepts_two_sequential_eps_transitions(self):
        nfa = NFA()
        nfa.add_state()
        nfa.add_state()
        nfa.add_state()
        nfa.add_transition(1, 2, '.')
        nfa.add_transition(2, 3, '.')
        
        self.assertSetEqual(nfa.eps_closure([1]), {1, 2, 3})

    def test_eps_closure_rejects_non_eps_transition_after_eps_transition(self):
        nfa = NFA()
        nfa.add_state()
        nfa.add_state()
        nfa.add_state()
        nfa.add_transition(1, 2, '.')
        nfa.add_transition(2, 3, 'a')
        
        self.assertSetEqual(nfa.eps_closure([1]), {1, 2})

    def test_eps_clousure_rejects_eps_transition_after_non_eps_transition(self):
        nfa = NFA()
        nfa.add_state()
        nfa.add_state()
        nfa.add_state()
        nfa.add_transition(1, 2, 'a')
        nfa.add_transition(2, 3, '.')
        
        self.assertSetEqual(nfa.eps_closure([1]), {1})

    def test_move_accepts_next_state_on_correct_symbol(self):
        nfa = NFA()
        nfa.add_state()
        nfa.add_state()
        nfa.add_transition(1, 2, 'a')
        
        self.assertSetEqual(nfa.move([1], 'a'), {2})

    def test_move_rejects_next_state_on_incorrect_symbol(self):
        nfa = NFA()
        nfa.add_state()
        nfa.add_state()
        nfa.add_transition(1, 2, 'b')
        
        self.assertSetEqual(nfa.move([1], 'a'), set())

    def test_move_handles_only_one_transition(self):
        nfa = NFA()
        nfa.add_state()
        nfa.add_state()
        nfa.add_state()
        nfa.add_state()
        nfa.add_state()
        nfa.add_state()
        nfa.add_transition(1, 2, 'a')
        nfa.add_transition(2, 3, 'a')
        
        self.assertSetEqual(nfa.move([1], 'a'), {2})