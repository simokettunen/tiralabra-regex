from nfa import *
from parser import Parser
from thompson import thompson
from rabin_scott import rabin_scott

from dfa import *

def compile(regex):
    p = Parser()
    p.parse(regex)
    nfa = thompson(p.result)
    dfa = rabin_scott(nfa)
    return dfa

def main():

    dfa = compile('(ab|aac)*')
    print(dfa.check_string('ab'))       # True
    print(dfa.check_string('aac'))      # True
    print(dfa.check_string('abaac'))    # True
    print(dfa.check_string('aacaac'))   # True
    print(dfa.check_string('aacaac'))   # True
    print(dfa.check_string('a'))        # False
    print(dfa.check_string('acab'))     # False
    
if __name__ == '__main__':
    main()