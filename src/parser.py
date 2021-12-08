from rules import rules
    
class Parser:
    """TODO"""

    def __init__(self):
        self.rules = rules
        
        # stack for terminals and non-terminals
        self._stack1 = None
        
        # assisting stack for just easier determining of rules with following equivalences
        self._stack2 = None
        
        self.result = None

    def __str__(self):
        return f'{self.result}'

    # TODO: break this into smaller components
    def _reduce(self):
        """TODO"""
        
        item1 = []
        item2 = []
        
        # Loop at most seven items since longest rule is (union)|(union)
        for i in range(7):
            if len(self._stack1) == 0:
                break
        
            item1.insert(0, self._stack1.pop())
            item2.insert(0, self._stack2.pop())
            
            if item2 in self.rules['empty']:
                node = Node('e')
                self._stack1.append(node)
                self._stack2.append('empty')
                
                self._reduce()
                return
                
            elif item2 in self.rules['single']:
                node = Node('s', item1[0])
                self._stack1.append(node)
                self._stack2.append('single')
                
                self._reduce()
                return
            
            elif item2 in self.rules['concatenation']:
                node = Node('c')
                
                # Check which one of the rule forms appears: XX, (X)X, X(X), (X)(X)
                if isinstance(item1[0], Node) and isinstance(item1[1], Node):
                    node.left = item1[0]
                    node.right = item1[1]
                elif isinstance(item1[0], Node) and isinstance(item1[2], Node):
                    node.left = item1[0]
                    node.right = item1[2]
                elif isinstance(item1[1], Node) and isinstance(item1[3], Node):
                    node.left = item1[1]
                    node.right = item1[3]
                elif isinstance(item1[1], Node) and isinstance(item1[4], Node):
                    node.left = item1[1]
                    node.right = item1[4]
                
                self._stack1.append(node)
                self._stack2.append('concatenation')
                
                self._reduce()
                return
                
            elif item2 in self.rules['kleene']:
                node = Node('k')
                
                # Check which one of the rule forms appears: X*, (X)*
                if isinstance(item1[0], Node):
                    node.left = item1[0]
                elif isinstance(item1[1], Node):
                    node.left = item1[1]
                
                self._stack1.append(node)
                self._stack2.append('kleene')
                
                self._reduce()
                return
                
            elif item2 in self.rules['union']:
                node = Node('u')
                
                # This is for handling rules of the form X|YZ correctly where YZ forms concatenation
                if [self._next] in self.rules['empty'] or [self._next] in self.rules['single']:
                    break
                
                # Check which one of the rule forms appears: X|X, X|(X), (X)|X, (X)|(X)
                if isinstance(item1[0], Node) and isinstance(item1[2], Node):
                    node.left = item1[0]
                    node.right = item1[2]
                elif isinstance(item1[0], Node) and isinstance(item1[3], Node):
                    node.left = item1[0]
                    node.right = item1[3]
                elif isinstance(item1[1], Node) and isinstance(item1[4], Node):
                    node.left = item1[1]
                    node.right = item1[4]
                elif isinstance(item1[1], Node) and isinstance(item1[5], Node):
                    node.left = item1[1]
                    node.right = item1[5]
                    
                self._stack1.append(node)
                self._stack2.append('union')
                
                self._reduce()
                return
        
        # Push popped items back to stacks if none of the rules matched
        for i in item1:
            self._stack1.append(i)
            
        for i in item2:
            self._stack2.append(i)

    def parse(self, string):
        """Create an abstract syntax tree from the given regular experssion."""
        
        # Empty input is not same as empty string, since empty string has own symbol '.'
        # TODO: Empty input could be interpret as empty language
        if string == '':
            raise Exception('Input for parser must not be empty. Empty string is denoted as a dot: . ')
        
        self._stack1 = []
        self._stack2 = []

        for i in range(len(string)):
            self._stack1.append(string[i])
            self._stack2.append(string[i])
            
            # The next character is needed in some cases to interpret input correctly
            if i < len(string) - 1:
                self._next = string[i+1]
            else:
                self._next = ''
            
            # TODO: this if statement needs refactoring
            if self._next == '*':
                item1 = self._stack1.pop()
                item2 = [self._stack2.pop()]
                if item2 in self.rules['single']:
                    node = Node('s', item1[0])
                    self._stack1.append(node)
                    self._stack2.append('single')
                elif item2 in self.rules['empty']:
                    node = Node('e')
                    self._stack1.append(node)
                    self._stack2.append('single')
                elif string[i] == '*':
                    self._reduce()
                else:
                    self._stack1.append(item1)
                    self._stack2.append(item2[0])
                    self._reduce()
                    
                continue
            
            self._reduce()
        
        # TODO: There is a production rule with start symbol 'top', and it should be used to check if parsing was successful
        self.result = self._stack1[0]

class Node:
    """TODO"""

    def __init__(self, type, label=None):
        self.type = type
        self.left = None
        self.right = None
        
        if type == 'e':
            self.label = '.'
        else:
            self.label = label
  
    def __str__(self):
        if self.type in ['c', 'k', 'u']:
            return f'({self.type} {self.left.__str__()} {self.right.__str__()})'
            
        if self.label is None:
            return ''
            
        return self.label