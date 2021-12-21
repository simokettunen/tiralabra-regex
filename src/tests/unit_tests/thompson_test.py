import unittest
from entities.node import Node
from algorithms.thompson import thompson

class TestThompson(unittest.TestCase):
    def test_thompson_algorithm_handles_empty_string_correctly(self):
        tree = Node('empty')
        nfa = thompson(tree)
        
        self.assertSetEqual(nfa.states, {1, 2})
        self.assertListEqual(nfa.transitions, [[1, 2, '.']])
        self.assertEqual(nfa.start_state, 1)
        self.assertEqual(nfa.accept_state, 2)
        
    def test_thompson_algorithm_handles_single_symbol_correctly(self):
        tree = Node('single', 'a')
        nfa = thompson(tree)
        
        self.assertSetEqual(nfa.states, {1, 2})
        self.assertListEqual(nfa.transitions, [[1, 2, 'a']])
        self.assertEqual(nfa.start_state, 1)
        self.assertEqual(nfa.accept_state, 2)
        
    def test_thompson_algorithm_handles_union_correctly(self):
        tree = Node('union')
        tree.left = Node('single', 'a')
        tree.right = Node('single', 'b')
        nfa = thompson(tree)
        
        self.assertSetEqual(nfa.states, {1, 2, 3, 4, 5, 6})
        self.assertListEqual(nfa.transitions, [
            [1, 2, 'a'],
            [3, 4, 'b'],
            [5, 1, '.'],
            [5, 3, '.'],
            [2, 6, '.'],
            [4, 6, '.'],
        ])
        self.assertEqual(nfa.start_state, 5)
        self.assertEqual(nfa.accept_state, 6)
        
    def test_thompson_algorithm_handles_kleene_star_correctly(self):
        tree = Node('kleene')
        tree.left = Node('single', 'a')
        nfa = thompson(tree)
        
        self.assertSetEqual(nfa.states, {1, 2, 3, 4})
        self.assertListEqual(nfa.transitions, [
            [1, 2, 'a'],
            [3, 1, '.'],
            [2, 4, '.'],
            [3, 4, '.'],
            [2, 1, '.'],
        ])
        self.assertEqual(nfa.start_state, 3)
        self.assertEqual(nfa.accept_state, 4)
        
    def test_thompson_algorithm_handles_concatenation_correctly(self):
        tree = Node('concatenation')
        tree.left = Node('single', 'a')
        tree.right = Node('single', 'b')
        nfa = thompson(tree)
        
        self.assertSetEqual(nfa.states, {1, 2, 3, 4})
        self.assertListEqual(nfa.transitions, [
            [1, 2, 'a'],
            [3, 4, 'b'],
            [2, 3, '.'],
        ])
        self.assertEqual(nfa.start_state, 1)
        self.assertEqual(nfa.accept_state, 4)