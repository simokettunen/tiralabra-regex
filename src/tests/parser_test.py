import unittest
from parser import Node, Parser

class TestParser(unittest.TestCase):
    def test_parser_recognizes_single(self):
        p = Parser()
        p.parse('a')
        self.assertEqual(p.result.__str__(), 'a')
                
    def test_parser_recognizes_kleene_star_of_one_single(self):
        p = Parser()
        p.parse('a*')
        self.assertEqual(p.result.__str__(), '(k a None)')
        
    def test_parser_recognizes_kleene_star_of_concatenation(self):
        p = Parser()
        p.parse('(ab)*')
        self.assertEqual(p.result.__str__(), '(k (c a b) None)')
        
    def test_parser_recognizes_kleene_star_of_union(self):
        p = Parser()
        p.parse('(a|b)*')
        self.assertEqual(p.result.__str__(), '(k (u a b) None)')
        
    def test_parser_recognizes_kleene_star_of_kleene_star(self):
        p = Parser()
        p.parse('a**')
        
        # TODO: Check this. The result is practically correct since a** = a* , but theoritically the result should be (k (k a None) None)
        self.assertEqual(p.result.__str__(), '(k a None)')
        
    def test_parser_recognizes_concatenation_of_two_singles(self):
        p = Parser()
        p.parse('ab')
        self.assertEqual(p.result.__str__(), '(c a b)')
        
    def test_parser_recognizes_concatenation_of_single_and_kleene_star(self):
        p = Parser()
        p.parse('ab*')
        self.assertEqual(p.result.__str__(), '(c a (k b None))')
        
    def test_parser_recognizes_concatenation_of_three_singles(self):
        # TODO: Check this. This can be interpret as concatenation of single and concatenation or
        # concatenation of concatenation and single
        p = Parser()
        p.parse('abc')
        self.assertEqual(p.result.__str__(), '(c (c a b) c)')
        
    def test_parser_recognizes_concatenation_of_single_and_union(self):
        p = Parser()
        p.parse('a(b|c)')
        self.assertEqual(p.result.__str__(), '(c a (u b c))')
        
    def test_parser_recognizes_concatenation_of_kleene_star_and_single(self):
        p = Parser()
        p.parse('a*b')
        self.assertEqual(p.result.__str__(), '(c (k a None) b)')
        
    def test_parser_recognizes_concatenation_of_two_kleene_stars(self):
        p = Parser()
        p.parse('a*b*')
        self.assertEqual(p.result.__str__(), '(c (k a None) (k b None))')
        
    def test_parser_recognizes_concatenation_of_kleene_star_and_union(self):
        p = Parser()
        p.parse('a*(b|c)')
        self.assertEqual(p.result.__str__(), '(c (k a None) (u b c))')
        
    def test_parser_recognizes_concatenation_of_concatenation_and_kleene_star(self):
        p = Parser()
        p.parse('abc*')
        self.assertEqual(p.result.__str__(), '(c (c a b) (k c None))')

    def test_parser_recognizes_concatenation_of_concatenation_and_union(self):
        p = Parser()
        p.parse('ab(c|d)')
        self.assertEqual(p.result.__str__(), '(c (c a b) (u c d))')
        
    def test_parser_recognizes_concatenation_of_union_and_single(self):
        p = Parser()
        p.parse('(a|b)c')
        self.assertEqual(p.result.__str__(), '(c (u a b) c)')
        
    def test_parser_recognizes_concatenation_of_union_and_kleene_star(self):
        p = Parser()
        p.parse('(a|b)c*')
        self.assertEqual(p.result.__str__(), '(c (u a b) (k c None))')
        
    def test_parser_recognizes_concatenation_of_union_and_concatenation(self):
        p = Parser()
        p.parse('(a|b)cd')
        
        # TODO: Check this. Actually (a|b)cd is concatenation of concatenation of union and single and single
        self.assertEqual(p.result.__str__(), '(c (c (u a b) c) d)')
        
    def test_parser_recognizes_concatenation_of_two_unions(self):
        p = Parser()
        p.parse('(a|b)(c|d)')
        self.assertEqual(p.result.__str__(), '(c (u a b) (u c d))')

    def test_parser_recognizes_union_of_two_singles(self):
        p = Parser()
        p.parse('a|b')
        self.assertEqual(p.result.__str__(), '(u a b)')
        
    def test_parser_recognizes_union_of_single_and_kleene_star(self):
        p = Parser()
        p.parse('a|b*')
        self.assertEqual(p.result.__str__(), '(u a (k b None))')
        
    def test_parser_recognizes_union_of_single_and_concatenation(self):
        p = Parser()
        p.parse('a|bc')
        self.assertEqual(p.result.__str__(), '(u a (c b c))')

    def test_parser_recognizes_union_of_single_and_union(self):
        p = Parser()
        p.parse('a|(b|c)')
        self.assertEqual(p.result.__str__(), '(u a (u b c))')
    
    def test_parser_recognizes_union_of_kleene_star_and_single(self):
        p = Parser()
        p.parse('a*|b')
        self.assertEqual(p.result.__str__(), '(u (k a None) b)')
        
    def test_parser_recognizes_union_of_two_kleene_stars(self):
        p = Parser()
        p.parse('a*|b*')
        self.assertEqual(p.result.__str__(), '(u (k a None) (k b None))')
        
    def test_parser_recognizes_union_of_kleene_star_and_concatenation(self):
        p = Parser()
        p.parse('a*|bc')
        self.assertEqual(p.result.__str__(), '(u (k a None) (c b c))')
    
    def test_parser_recognizes_union_of_kleene_star_and_union(self):
        p = Parser()
        p.parse('a*|(b|c)')
        self.assertEqual(p.result.__str__(), '(u (k a None) (u b c))')
    
    def test_parser_recognizes_union_of_concatenation_and_single(self):
        p = Parser()
        p.parse('ab|c')
        self.assertEqual(p.result.__str__(), '(u (c a b) c)')
        
    def test_parser_recognizes_union_of_concatenation_and_kleene_star(self):
        p = Parser()
        p.parse('ab|c*')
        self.assertEqual(p.result.__str__(), '(u (c a b) (k c None))')
        
    def test_parser_recognizes_union_of_concatenation_and_concatenation(self):
        p = Parser()
        p.parse('ab|cd')
        self.assertEqual(p.result.__str__(), '(u (c a b) (c c d))')
        
    def test_parser_recognizes_union_of_concatenation_and_union(self):
        p = Parser()
        p.parse('ab|(c|d))')
        self.assertEqual(p.result.__str__(), '(u (c a b) (u c d))')
        
    def test_parser_recognizes_union_of_union_and_single(self):
        p = Parser()
        p.parse('(a|b)|c')
        self.assertEqual(p.result.__str__(), '(u (u a b) c)')
        
    def test_parser_recognizes_union_of_union_and_kleene_star(self):
        p = Parser()
        p.parse('(a|b)|c*')
        self.assertEqual(p.result.__str__(), '(u (u a b) (k c None))')
        
    def test_parser_recognizes_union_of_union_and_concatenation(self):
        p = Parser()
        p.parse('(a|b)|cd')
        self.assertEqual(p.result.__str__(), '(u (u a b) (c c d))')
        
    def test_parser_recognizes_union_of_union_and_union(self):
        p = Parser()
        p.parse('(a|b)|(c|d)')
        self.assertEqual(p.result.__str__(), '(u (u a b) (u c d))')