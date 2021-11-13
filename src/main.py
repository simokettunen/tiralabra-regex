from nfa import *
from parser import Node
from thompson import thompson

def main():
    
    # regular expression ""
    t = Node('s', '.')
    nfa = thompson(t)
    print(nfa)
    
    # regular expression a
    t = Node('s', 'a')
    nfa = thompson(t)
    print(nfa)

    # regular expression a|b
    t = Node('u')
    t.left = Node('s', 'a')
    t.right = Node('s', 'b')
    nfa = thompson(t)
    print(nfa)
    
    # regular expression a*
    t = Node('k')
    t.left = Node('s', 'a')
    nfa = thompson(t)
    print(nfa)
    
    # regular expresion ab
    t = Node('c')
    t.left = Node('s', 'a')
    t.right = Node('s', 'b')
    nfa = thompson(t)
    print(nfa)
    
    # regular expression a*b|c
    t = Node('u')
    t.left = Node('c')
    t.right = Node('s', 'c')
    t.left.left = Node('k')
    t.left.right = Node('s', 'b')
    t.left.left.left = Node('s', 'a')
    nfa = thompson(t)
    print(nfa)
  
if __name__ == '__main__':
    main()