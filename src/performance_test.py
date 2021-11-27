from utils import compile
from time import time

def match_performance(string):
    dfa = compile('a*')
    
    start = time()
    is_match = dfa.match(string)
    end = time()
    
    result = end - start
    
    return result
    
def main():
    print('Pituus   Aika (s)')
    
    for i in range(8):
        string = 'a'*(10**i)
        res = match_performance(string)
        print(f'{len(string):8} {res}')
    
if __name__ == '__main__':
    main()