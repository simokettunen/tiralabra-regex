import unittest
from entities.node import Node

class TestThompson(unittest.TestCase):
    def test_constructing_node_having_type_of_empty_works(self):
        node = Node('empty')
        
        self.assertEqual(node.type, 'empty')
        self.assertEqual(node.label, '.')
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        
    def test_constructing_node_having_type_of_single_works(self):
        node = Node('single', label='a')
        
        self.assertEqual(node.type, 'single')
        self.assertEqual(node.label, 'a')
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        
    def test_constructing_node_having_type_of_kleene_works(self):
        left = Node('single', 'a')
        node = Node('kleene', left=left)
        
        self.assertEqual(node.type, 'kleene')
        self.assertIsNone(node.label)
        self.assertEqual(node.left, left)
        self.assertIsNone(node.right)

    def test_constructing_node_having_type_of_concatenation_works(self):
        left = Node('single', 'a')
        right = Node('single', 'b')
        node = Node('concatenation', left=left, right=right)
        
        self.assertEqual(node.type, 'concatenation')
        self.assertIsNone(node.label)
        self.assertEqual(node.left, left)
        self.assertEqual(node.right, right)
        
    def test_constructing_node_having_type_of_concatenation_works(self):
        left = Node('single', 'a')
        right = Node('single', 'b')
        node = Node('union', left=left, right=right)
        
        self.assertEqual(node.type, 'union')
        self.assertIsNone(node.label)
        self.assertEqual(node.left, left)
        self.assertEqual(node.right, right)