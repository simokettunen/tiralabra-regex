from parser import Parser
from thompson import thompson
from rabin_scott import rabin_scott

def compile(regex):
    p = Parser()
    p.parse(regex)
    nfa = thompson(p.result)
    dfa = rabin_scott(nfa)
    return dfa