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
    print(dfa.match('ab'))       # True
    print(dfa.match('aac'))      # True
    print(dfa.match('abaac'))    # True
    print(dfa.match('aacaac'))   # True
    print(dfa.match('a'))        # False
    print(dfa.match('acab'))     # False
    
if __name__ == '__main__':
    main()