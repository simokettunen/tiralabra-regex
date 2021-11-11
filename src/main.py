from nfa import *

def main():
    # regular expression ""
    nfa = empty()
    print(nfa)
    
    # regular expression a
    nfa = single('a')
    print(nfa)
    
    # regular expression a|b
    nfa1 = single('a')
    nfa2 = single('b')
    nfa = union(nfa1, nfa2)
    print(nfa)
    
    # regular expression a*
    nfa1 = single('a')
    nfa = kleene_star(nfa1)
    print(nfa)
    
    # regular expression ab
    nfa1 = single('a')
    nfa2 = single('b')
    nfa = concatenation(nfa1, nfa2)
    print(nfa)

    # regular expression a*b|c
    nfa_a = single('a')
    nfa_b = single('b')
    nfa_c = single('c')
    nfa_aO = kleene_star(nfa_a)
    nfa_aOb = concatenation(nfa_aO, nfa_b)
    nfa_aOb_c = union(nfa_aOb, nfa_c)
    print(nfa_aOb_c)
    
if __name__ == '__main__':
    main()