import unittest
from utils import compile

class TestCompileAndMatch(unittest.TestCase):
    def test_regex_consisting_of_empty_string_compiled_correctly(self):
        dfa = compile('.')
        
        positives = ['.', '..']
        negatives = ['a']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)

    def test_regex_consisting_of_single_character_is_compiled_correctly(self):
        dfa = compile('a')
        
        positives = ['a', 'a.', '.a', '..a', 'a..']
        negatives = ['.', 'aa', 'b', 'A']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_two_characters_is_compiled_correctly(self):
        dfa = compile('aa')
        
        positives = ['aa', 'a.a', 'a..a']
        negatives = ['.', 'a', 'aaa', 'bb', 'AA']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_union_is_compiled_correctly(self):
        dfa = compile('a|b')
        
        positives = ['a', 'b']
        negatives = ['.', 'ab', 'ba', 'aa', 'bb']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_kleene_star_is_compiled_correctly(self):
        dfa = compile('a*')
        
        positives = ['.', 'a', 'aa', 'aaa', 'aaaa']
        negatives = ['b', 'ab', 'ba']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_kleene_star_is_compiled_correctly(self):
        dfa = compile('a*')
        
        positives = ['.', 'a', 'aa', 'aaa', 'aaaa']
        negatives = ['b', 'ab', 'ba']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        