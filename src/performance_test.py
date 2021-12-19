from algorithms.parser import Parser
from utils import compile
from time import time
import random

def random_regex(n):
    items = [
        '.',
        'aa',
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '0123456789',
        '*',
        '((abc|123)|(ABC|DEF))',
        '((a|b)|cd)',
        '((a|b)|c*)'
        '(.|(a|b))'
    ]
    
    regex = 'a'
    
    while len(regex) <= n:
        regex += random.choice(items)
        
    return regex

def execute_match_performance(string):
    dfa = compile('a*')
    
    start = time()
    is_match = dfa.match(string)
    end = time()
    
    result = end - start
    
    return result
    
def execute_parser_performance(string):
    parser = Parser()
    
    start = time()
    dfa = parser.parse(string)
    end = time()
    
    result = end - start
    
    return result
    
def parser_performance():
    print('Parser performance test')
    print('Input length  Time (s)')
    
    test_cases = [
        [
            'a'*(10**1),
            'a'*(10**2),
            'a'*(10**3),
            'a'*(10**4),
            'a'*(10**5),
        ],
        
        [
            'a' + '*'*(10**1),
            'a' + '*'*(10**2),
            'a' + '*'*(10**3),
            'a' + '*'*(10**4),
            'a' + '*'*(10**5),
        ],
        
        [
            '('*(10**1) + 'a' + '|a)'*(10**1) + '|a',
            '('*(10**2) + 'a' + '|a)'*(10**2) + '|a',
            '('*(10**3) + 'a' + '|a)'*(10**3) + '|a',
            '('*(10**4) + 'a' + '|a)'*(10**4) + '|a',
            '('*(10**5) + 'a' + '|a)'*(10**5) + '|a',
        ],
        
        [
            random_regex(10**1),
            random_regex(10**2),
            random_regex(10**3),
            random_regex(10**4),
            random_regex(10**5),
        ],
    ]
    
    for test_case in test_cases:    
        for string in test_case:
            try:
                res = execute_parser_performance(string)
            except:
                print(string)
            print(f'{len(string):12}  {res}')
        
    print('')
        
def match_performance():
    print('Match performance test')
    print('Input length  Time (s)')
    
    for i in range(8):
        string = 'a'*(10**i)
        res = execute_match_performance(string)
        print(f'{len(string):12}  {res}')
    
    print('')
        
    
    
def main():
    parser_performance()
    match_performance()
    
if __name__ == '__main__':
    main()