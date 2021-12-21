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
        
    def test_regex_consisting_of_concatenation_is_compiled_correctly(self):
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
        
    def test_regex_consisting_of_two_sequential_concatenations_is_compiled_correctly(self):
        dfa = compile('abcd')
        
        positives = ['abcd']
        negatives = ['.', 'a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_two_sequential_unions_is_compiled_correctly(self):
        dfa = compile('(a|b)(c|d)')
        
        positives = ['ac', 'ad', 'bc', 'bd']
        negatives = ['.', 'a', 'b', 'c', 'd', 'abc', 'abd', 'acd', 'bcd']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_two_sequential_kleenes_is_compiled_correctly(self):
        dfa = compile('a*b*')
        
        positives = ['.', 'a', 'b', 'aa', 'bb', 'ab', 'aab', 'abb', 'aaa', 'bbb']
        negatives = ['ba', 'aba']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_kleene_inside_kleene_is_compiled_correctly(self):
        dfa = compile('a**')
        
        positives = ['.', 'a', 'aa', 'aaa', 'aaaa']
        negatives = ['b', 'ab', 'ba']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_concatenation_inside_kleene_is_compiled_correctly(self):
        dfa = compile('(ab)*')
        
        positives = ['.', 'ab', 'abab', 'ababab', 'abababab']
        negatives = ['a', 'b', 'ba', 'bab', 'baba', 'aba']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_union_inside_kleene_is_compiled_correctly(self):
        dfa = compile('(a|b)*')
        
        positives = ['.', 'a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
        negatives = ['c']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_concatenation_inside_union_is_compiled_correctly(self):
        dfa = compile('ab|c')
        
        positives = ['ab', 'c']
        negatives = ['.', 'a', 'b', 'ac', 'bc', 'ba']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_kleene_inside_union_is_compiled_correctly(self):
        dfa = compile('a|b*')
        
        positives = ['.', 'a', 'b', 'bb', 'bbb', 'bbbb', 'bbbbb']
        negatives = ['ba', 'aa']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_consisting_of_union_inside_union_is_compiled_correctly(self):
        dfa = compile('(a|b)|c')
        
        positives = ['a', 'b', 'c']
        negatives = ['.', 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_accepting_language_in_which_string_has_exactly_one_1(self):
        dfa = compile('0*10*')
        
        positives = ['1', '01', '10', '001', '010', '100', '0001', '0010', '0100', '1000']
        negatives = ['.', '0', '00', '11', '000', '011', '101', '110', '111']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_accepting_language_in_which_string_has_at_least_one_1(self):
        dfa = compile('(0|1)*1(0|1)*')
        
        positives = ['1', '01', '10', '11', '001', '010', '100', '011', '110', '101', '111', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
        negatives = ['.', '0', '00', '000', '0000']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)

    def test_regex_accepting_language_in_which_string_contains_001_as_a_substring(self):
        dfa = compile('(0|1)*001(0|1)*')
        
        positives = ['001', '0001', '1001', '0010', '0011' '00010', '00011', '10010', '10011']
        negatives = ['.', '0', '1', '00', '01', '10', '11', '000', '010', '011', '100', '101', '110', '111', '0000', '0100', '0101', '0110', '0111', '1000', '1010', '1011', '1100', '1101', '1110', '1111']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_accepting_language_in_which_string_is_of_even_length(self):
        dfa = compile('((0|1)(0|1))*')
        
        positives = ['.', '00', '01', '10', '11', '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1110', '1111']
        negatives = ['0', '1', '000', '001', '010', '011', '100', '101', '110', '111']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)
        
    def test_regex_accepting_language_in_which_string_starts_and_ends_with_the_same_symbol(self):
        dfa = compile('((0(0|1)*0|1(0|1)*1)|0)|1')
        
        positives = ['0', '1', '00', '11', '000', '010', '101', '111', '0000', '0010', '0100', '0110', '1001', '1011', '1101', '1111']
        negatives = ['.', '01', '10', '001', '011', '100', '110', '0001', '0011', '0101', '0111', '1000', '1010', '1100', '1110']
        
        res1 = all([dfa.match(string) for string in positives])
        res2 = not any([dfa.match(string) for string in negatives])
        
        self.assertTrue(res1)
        self.assertTrue(res2)