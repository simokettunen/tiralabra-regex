from utils import compile

class App:
    def __init__(self):
        self.dfa = None

    def start(self):
        self._print_instructions()
        
        while True:
            command = input('Command (1/2/3/0): ')
            
            if command == '1':
                self._compile()
            elif command == '2':
                self._match()
            elif command == '3':
                self._print_instructions()
            elif command == '0':
                break
            else:
                print('Incorrect command')
        
    def _compile(self):
        regex = input('Regular expression: ')
        self.dfa = compile(regex)
        
    def _match(self):
        if self.dfa is None:
            print('Please compile regular expression before matching')
        else:
            string = input('String to be matched: ')
            print(self.dfa.match(string))
        
    def _print_instructions(self):
        print('Commands')
        print('  1 - Compile regular expression')
        print('  2 - Match string against regular expression')
        print('  3 - Print instructions')
        print('  0 - Exit')

def main():
    app = App()
    app.start()
    
if __name__ == '__main__':
    main()
    
