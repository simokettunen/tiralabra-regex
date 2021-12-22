from utils import compile
from time import time
import random
import math

import matplotlib.pyplot as plt

def random_regex(n):
    items = [
        '.',
        'aa',
        'abcdefghijk',
        'ABCDEFGHIJK',
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

def execute_match_performance(regex, string):
    dfa = compile(regex)

    start = time()
    is_match = dfa.match(string)
    end = time()
    
    result = end - start
    
    return result
    
def execute_compile_performance(regex):
    start = time()
    dfa = compile(regex)
    end = time()
    
    result = end - start
    
    return result
    
def run_test_cases(test_cases, test, xlabel, ylabel, title):
    data_x = []
    data_y = []
    
    i = 0
    for test_case in test_cases:
        data_x.append([])
        data_y.append([])

        for string in test_case[2]:
        
            if test == 'compile':
                res = execute_compile_performance(string)
            elif test == 'match':
                res = execute_match_performance(test_case[1], string)
                
            data_x[i].append(len(string))
            data_y[i].append(res)
        
        i += 1
        
    print('')
    
    for j in range(i):
        plt.plot(data_x[j], data_y[j], f'{test_cases[j][0]}.')
        
    plt.legend([test_case[1] for test_case in test_cases])
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

    
def compile_performance():
    
    lengths = [
        10**1*1,
        10**1*3,
        10**1*5,
        10**1*8,
        10**2*1,
        10**2*2,
        10**2*3,
        10**2*4,
        10**2*5,
        10**2*6,
    ]
    
    test_cases = [
        ['b', 'Concatenations', ['a'*n for n in lengths]],
        ['g', 'Kleene stars', ['a' + '*'*n for n in lengths]],
        ['r', 'Unions', ['('*math.floor(n/4) + 'a' + '|a)'*math.floor(n/4) + '|a' for n in lengths]],
        ['c', 'Random regular expression', [random_regex(n) for n in lengths]],
    ]
    
    run_test_cases(
        test_cases,
        'compile',
        'Length of regular expression (characters)',
        'Time (s)',
        'Compiling regular expression to DFA',
    )
        
def match_performance():

    lengths = [
        10**5*1,
        10**5*5,
        10**6*1,
        10**6*2,
        10**6*3,
        10**6*4,
        10**6*5,
        10**6*6,
        10**6*7,
        10**6*8,
        10**6*9,
        10**7*1,
    ]
    
    test_cases = [
    
        # Any number of ones
        ['g', '1*', ['1'*n for n in lengths]],
        
        # At least single one
        ['r', '(0|1)*1(0|1)*', ['1'*n for n in lengths]],
        
        # String starts and ends with same char (0 or 1)
        ['c', '((0(0|1)*0|1(0|1)*1)|0)|1', ['1'*n for n in lengths]],
    ]
    
    run_test_cases(
        test_cases,
        'match',
        'Length of string (characters)',
        'Time (s)',
        'Matching string',
    )
    
def main():
    compile_performance()
    match_performance()
    
if __name__ == '__main__':
    main()