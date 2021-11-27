from utils import compile

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
    
