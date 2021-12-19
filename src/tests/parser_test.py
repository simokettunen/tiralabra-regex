import unittest
from entities.node import Node
from algorithms.parser import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parser_recognizes_empty_input(self):
        self.assertRaises(Exception, self.parser.parse, '')

    def test_parser_recognizes_empty(self):
        self.parser.parse('.')
        self.assertEqual(self.parser.result.__str__(), '.')

    def test_parser_recognizes_single(self):
        self.parser.parse('a')
        self.assertEqual(self.parser.result.__str__(), 'a')
        
    def test_parser_recognizes_kleene_star_of_empty(self):
        self.parser.parse('.*')
        self.assertEqual(self.parser.result.__str__(), '(k . None)')

    def test_parser_recognizes_kleene_star_of_one_single(self):
        self.parser.parse('a*')
        self.assertEqual(self.parser.result.__str__(), '(k a None)')

    def test_parser_recognizes_kleene_star_of_concatenation(self):
        self.parser.parse('(ab)*')
        self.assertEqual(self.parser.result.__str__(), '(k (c a b) None)')

    def test_parser_recognizes_kleene_star_of_union(self):
        self.parser.parse('(a|b)*')
        self.assertEqual(self.parser.result.__str__(), '(k (u a b) None)')

    def test_parser_recognizes_kleene_star_of_kleene_star(self):
        self.parser.parse('a**')
        self.assertEqual(self.parser.result.__str__(), '(k (k a None) None)')

    def test_parser_recognizes_concatenation_of_two_empties(self):
        self.parser.parse('..')
        self.assertEqual(self.parser.result.__str__(), '(c . .)')
        
    def test_parser_recognizes_concatenation_of_empty_and_single(self):
        self.parser.parse('.a')
        self.assertEqual(self.parser.result.__str__(), '(c . a)')
        
    def test_parser_recognizes_concatenation_of_empty_and_union(self):
        self.parser.parse('.(a|b)')
        self.assertEqual(self.parser.result.__str__(), '(c . (u a b))')
        
    def test_parser_recognizes_concatenation_of_empty_and_concatenation(self):
        # TODO: Check this. This can be interpret as concatenation of empty and concatenation or
        # concatenation of concatenation and single
        self.parser.parse('.ab')
        self.assertEqual(self.parser.result.__str__(), '(c (c . a) b)')

    def test_parser_recognizes_concatenation_of_empty_and_kleene_star(self):
        self.parser.parse('.a*')
        self.assertEqual(self.parser.result.__str__(), '(c . (k a None))')
        
    def test_parser_recognizes_concatenation_of_single_and_empty(self):
        self.parser.parse('a.')
        self.assertEqual(self.parser.result.__str__(), '(c a .)')

    def test_parser_recognizes_concatenation_of_two_singles(self):
        self.parser.parse('ab')
        self.assertEqual(self.parser.result.__str__(), '(c a b)')

    def test_parser_recognizes_concatenation_of_single_and_kleene_star(self):
        self.parser.parse('ab*')
        self.assertEqual(self.parser.result.__str__(), '(c a (k b None))')

    def test_parser_recognizes_concatenation_of_three_singles(self):
        # TODO: Check this. This can be interpret as concatenation of single and concatenation or
        # concatenation of concatenation and single
        self.parser.parse('abc')
        self.assertEqual(self.parser.result.__str__(), '(c (c a b) c)')

    def test_parser_recognizes_concatenation_of_single_and_union(self):
        self.parser.parse('a(b|c)')
        self.assertEqual(self.parser.result.__str__(), '(c a (u b c))')

    def test_parser_recognizes_concatenation_of_kleene_star_and_single(self):
        self.parser.parse('a*b')
        self.assertEqual(self.parser.result.__str__(), '(c (k a None) b)')

    def test_parser_recognizes_concatenation_of_two_kleene_stars(self):
        self.parser.parse('a*b*')
        self.assertEqual(self.parser.result.__str__(), '(c (k a None) (k b None))')

    def test_parser_recognizes_concatenation_of_kleene_star_and_union(self):
        self.parser.parse('a*(b|c)')
        self.assertEqual(self.parser.result.__str__(), '(c (k a None) (u b c))')

    def test_parser_recognizes_concatenation_of_concatenation_and_kleene_star(self):
        self.parser.parse('abc*')
        self.assertEqual(self.parser.result.__str__(), '(c (c a b) (k c None))')

    def test_parser_recognizes_concatenation_of_concatenation_and_union(self):
        self.parser.parse('ab(c|d)')
        self.assertEqual(self.parser.result.__str__(), '(c (c a b) (u c d))')
        
    def test_parser_recognizes_concatenation_of_union_and_empty(self):
        self.parser.parse('(a|b).')
        self.assertEqual(self.parser.result.__str__(), '(c (u a b) .)')

    def test_parser_recognizes_concatenation_of_union_and_single(self):
        self.parser.parse('(a|b)c')
        self.assertEqual(self.parser.result.__str__(), '(c (u a b) c)')

    def test_parser_recognizes_concatenation_of_union_and_kleene_star(self):
        self.parser.parse('(a|b)c*')
        self.assertEqual(self.parser.result.__str__(), '(c (u a b) (k c None))')

    def test_parser_recognizes_concatenation_of_union_and_concatenation(self):
        self.parser.parse('(a|b)cd')
        
        # TODO: Check this. Actually (a|b)cd is concatenation of concatenation of union and single and single
        self.assertEqual(self.parser.result.__str__(), '(c (c (u a b) c) d)')

    def test_parser_recognizes_concatenation_of_two_unions(self):
        self.parser.parse('(a|b)(c|d)')
        self.assertEqual(self.parser.result.__str__(), '(c (u a b) (u c d))')
        
    def test_parser_recognizes_union_of_two_empties(self):
        self.parser.parse('.|.')
        self.assertEqual(self.parser.result.__str__(), '(u . .)')
        
    def test_parser_recognizes_union_of_empty_and_single(self):
        self.parser.parse('.|a')
        self.assertEqual(self.parser.result.__str__(), '(u . a)')
        
    def test_parser_recognizes_union_of_empty_and_union(self):
        self.parser.parse('.|(a|b)')
        self.assertEqual(self.parser.result.__str__(), '(u . (u a b))')
        
    def test_parser_recognizes_union_of_empty_and_concatenation(self):
        self.parser.parse('.|ab')
        self.assertEqual(self.parser.result.__str__(), '(u . (c a b))')
        
    def test_parser_recognizes_union_of_empty_and_kleen_star(self):
        self.parser.parse('.|a*')
        self.assertEqual(self.parser.result.__str__(), '(u . (k a None))')

    def test_parser_recognizes_union_of_single_and_empty(self):
        self.parser.parse('a|.')
        self.assertEqual(self.parser.result.__str__(), '(u a .)')

    def test_parser_recognizes_union_of_two_singles(self):
        self.parser.parse('a|b')
        self.assertEqual(self.parser.result.__str__(), '(u a b)')

    def test_parser_recognizes_union_of_single_and_kleene_star(self):
        self.parser.parse('a|b*')
        self.assertEqual(self.parser.result.__str__(), '(u a (k b None))')

    def test_parser_recognizes_union_of_single_and_concatenation(self):
        self.parser.parse('a|bc')
        self.assertEqual(self.parser.result.__str__(), '(u a (c b c))')

    def test_parser_recognizes_union_of_single_and_union(self):
        self.parser.parse('a|(b|c)')
        self.assertEqual(self.parser.result.__str__(), '(u a (u b c))')
        
    def test_parser_recognizes_union_of_kleene_star_and_empty(self):
        self.parser.parse('a*|.')
        self.assertEqual(self.parser.result.__str__(), '(u (k a None) .)')

    def test_parser_recognizes_union_of_kleene_star_and_single(self):
        self.parser.parse('a*|b')
        self.assertEqual(self.parser.result.__str__(), '(u (k a None) b)')

    def test_parser_recognizes_union_of_two_kleene_stars(self):
        self.parser.parse('a*|b*')
        self.assertEqual(self.parser.result.__str__(), '(u (k a None) (k b None))')

    def test_parser_recognizes_union_of_kleene_star_and_concatenation(self):
        self.parser.parse('a*|bc')
        self.assertEqual(self.parser.result.__str__(), '(u (k a None) (c b c))')

    def test_parser_recognizes_union_of_kleene_star_and_union(self):
        self.parser.parse('a*|(b|c)')
        self.assertEqual(self.parser.result.__str__(), '(u (k a None) (u b c))')
        
    def test_parser_recognizes_union_of_concatenation_and_empty(self):
        self.parser.parse('ab|.')
        self.assertEqual(self.parser.result.__str__(), '(u (c a b) .)')

    def test_parser_recognizes_union_of_concatenation_and_single(self):
        self.parser.parse('ab|c')
        self.assertEqual(self.parser.result.__str__(), '(u (c a b) c)')

    def test_parser_recognizes_union_of_concatenation_and_kleene_star(self):
        self.parser.parse('ab|c*')
        self.assertEqual(self.parser.result.__str__(), '(u (c a b) (k c None))')

    def test_parser_recognizes_union_of_concatenation_and_concatenation(self):
        self.parser.parse('ab|cd')
        self.assertEqual(self.parser.result.__str__(), '(u (c a b) (c c d))')

    def test_parser_recognizes_union_of_concatenation_and_union(self):
        self.parser.parse('ab|(c|d)')
        self.assertEqual(self.parser.result.__str__(), '(u (c a b) (u c d))')
        
    def test_parser_recognizes_union_of_union_and_empty(self):
        self.parser.parse('(a|b)|.')
        self.assertEqual(self.parser.result.__str__(), '(u (u a b) .)')

    def test_parser_recognizes_union_of_union_and_single(self):
        self.parser.parse('(a|b)|c')
        self.assertEqual(self.parser.result.__str__(), '(u (u a b) c)')

    def test_parser_recognizes_union_of_union_and_kleene_star(self):
        self.parser.parse('(a|b)|c*')
        self.assertEqual(self.parser.result.__str__(), '(u (u a b) (k c None))')

    def test_parser_recognizes_union_of_union_and_concatenation(self):
        self.parser.parse('(a|b)|cd')
        self.assertEqual(self.parser.result.__str__(), '(u (u a b) (c c d))')

    def test_parser_recognizes_union_of_union_and_union(self):
        self.parser.parse('(a|b)|(c|d)')
        self.assertEqual(self.parser.result.__str__(), '(u (u a b) (u c d))')
        
    def test_parser_recognizes_lowercase_letters_of_latin_alphabet(self):
        self.parser.parse('abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(self.parser.result.__str__(), '(c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c a b) c) d) e) f) g) h) i) j) k) l) m) n) o) p) q) r) s) t) u) v) w) x) y) z)')
        
    def test_parser_recognizes_uppercase_letters_of_latin_alphabet(self):
        self.parser.parse('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.assertEqual(self.parser.result.__str__(), '(c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c (c A B) C) D) E) F) G) H) I) J) K) L) M) N) O) P) Q) R) S) T) U) V) W) X) Y) Z)')
        
    def test_parser_recognizes_digits(self):
        self.parser.parse('0123456789')
        self.assertEqual(self.parser.result.__str__(), '(c (c (c (c (c (c (c (c (c 0 1) 2) 3) 4) 5) 6) 7) 8) 9)')

    def test_parser_recognizes_concatenation_of_empty_and_double_kleene_star(self):
        self.parser.parse('.a**')
        self.assertEqual(self.parser.result.__str__(), '(c . (k (k a None) None))')
        
    def test_parser_recognizes_concatenation_of_single_and_double_kleene_star(self):
        self.parser.parse('ab**')
        self.assertEqual(self.parser.result.__str__(), '(c a (k (k b None) None))')
        
    def test_parser_recognizes_concatenation_of_union_and_double_kleene_star(self):
        self.parser.parse('(a|b)c**')
        self.assertEqual(self.parser.result.__str__(), '(c (u a b) (k (k c None) None))')
        
    def test_parser_recognizes_concatenation_of_kleene_star_and_double_kleene_star(self):
        self.parser.parse('a*b**')
        self.assertEqual(self.parser.result.__str__(), '(c (k a None) (k (k b None) None))')
        
    def test_parser_recognizes_concatenation_of_two_double_kleene_stars(self):
        self.parser.parse('a**b**')
        self.assertEqual(self.parser.result.__str__(), '(c (k (k a None) None) (k (k b None) None))')
    
    def test_parser_recognizes_concatenation_of_empty_and_unions_kleene_star(self):
        self.parser.parse('.(a|b)*')
        self.assertEqual(self.parser.result.__str__(), '(c . (k (u a b) None))')
    
    def test_parser_recognizes_concatenation_of_single_and_unions_kleene_star(self):
        self.parser.parse('a(b|c)*')
        self.assertEqual(self.parser.result.__str__(), '(c a (k (u b c) None))')
        
    def test_parser_recognizes_concatenation_of_single_and_unions_kleene_star(self):
        self.parser.parse('(a|b)(c|d)*')
        self.assertEqual(self.parser.result.__str__(), '(c (u a b) (k (u c d) None))')