from algorithms.parser import Parser
from algorithms.rabin_scott import rabin_scott
from algorithms.thompson import thompson

def compile(regex):
    """Compile the given regular expression to deterministic finite automaton."""
    
    parser = Parser()
    parser.parse(regex)
    nfa = thompson(parser.result)
    dfa = rabin_scott(nfa)
    return dfa