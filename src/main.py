from nfa import *
from parser import Node
from thompson import thompson
from rabin_scott import rabin_scott

from dfa import *

def main():

    # regular expression a*b|c
    t = Node('u')
    t.left = Node('c')
    t.right = Node('s', 'c')
    t.left.left = Node('k')
    t.left.right = Node('s', 'b')
    t.left.left.left = Node('s', 'a')
    nfa = thompson(t)
    dfa = rabin_scott(nfa)
    print(dfa.check_string('abb'))  # False
    print(dfa.check_string('aab'))  # True
    print(dfa.check_string('c'))    # True
    print(dfa.check_string('b'))    # True
    print(dfa.check_string('cc'))   # False
    
if __name__ == '__main__':
    main()