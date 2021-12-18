from rules import rules
from entities.node import Node
    
class Parser:
    """A class for shift-reduce parser to parse regular expressions."""

    def __init__(self):
        self._rules = rules
        
        # stack for terminals and non-terminals
        self._stack1 = None
        
        # assisting stack for just easier determining of rules with following equivalences
        self._stack2 = None
        
        self._next = None
        self.result = None

    def __str__(self):
        return f'{self.result}'
        
    def _reduce_empty(self):
        node = Node('e')
        self._stack1.append(node)
        self._stack2.append('empty')

    def _reduce_single(self, items):
        node = Node('s', items[0])
        self._stack1.append(node)
        self._stack2.append('single')
        
    def _reduce_concatenation(self, items):
        node = Node('c')
        
        # Check which one of the rule forms appears: XX, (X)X, X(X), (X)(X)
        if isinstance(items[0], Node) and isinstance(items[1], Node):
            node.left = items[0]
            node.right = items[1]
        elif isinstance(items[0], Node) and isinstance(items[2], Node):
            node.left = items[0]
            node.right = items[2]
        elif isinstance(items[1], Node) and isinstance(items[3], Node):
            node.left = items[1]
            node.right = items[3]
        elif isinstance(items[1], Node) and isinstance(items[4], Node):
            node.left = items[1]
            node.right = items[4]
        else:
            raise Exception('Syntax error.')
        
        self._stack1.append(node)
        self._stack2.append('concatenation')
        
    def _reduce_kleene(self, items):
        node = Node('k')
        
        # Check which one of the rule forms appears: X*, (X)*
        if isinstance(items[0], Node):
            node.left = items[0]
        elif isinstance(items[1], Node):
            node.left = items[1]
        else:
            raise Exception('Syntax error.')
        
        self._stack1.append(node)
        self._stack2.append('kleene')
        
    def _reduce_union(self, items):
        node = Node('u')
        
        # Check which one of the rule forms appears: X|X, X|(X), (X)|X, (X)|(X)
        if isinstance(items[0], Node) and isinstance(items[2], Node):
            node.left = items[0]
            node.right = items[2]
        elif isinstance(items[0], Node) and isinstance(items[3], Node):
            node.left = items[0]
            node.right = items[3]
        elif isinstance(items[1], Node) and isinstance(items[4], Node):
            node.left = items[1]
            node.right = items[4]
        elif isinstance(items[1], Node) and isinstance(items[5], Node):
            node.left = items[1]
            node.right = items[5]
        else:
            raise Exception('Syntax error.')
            
        self._stack1.append(node)
        self._stack2.append('union')
        
    def _reduce_top(self):
        item = []
        item.append(self._stack2.pop())
        
        if item in self._rules['top'] and len(self._stack2) == 0:
            self.result = self._stack1[0]
        else:
            raise Exception('Syntax error.')

    def _match(self):
        """Pop items from stack and check if some rule matches, then reducee"""
        
        # Lists for popping items from self._stack1 and self._stack2
        popped_items1 = []
        popped_items2 = []
        
        # Scan at most seven items since the longest rule is (union)|(union)
        for i in range(7):
            if len(self._stack1) == 0:
                break
        
            popped_items1.insert(0, self._stack1.pop())
            popped_items2.insert(0, self._stack2.pop())
            
            if popped_items2 in self._rules['empty']:
                self._reduce_empty()
                self._match()
                return
                
            elif popped_items2 in self._rules['single']:
                self._reduce_single(popped_items1)
                self._match()
                return
            
            elif popped_items2 in self._rules['concatenation']:
                self._reduce_concatenation(popped_items1)
                self._match()
                return
                
            elif popped_items2 in self._rules['kleene']:
                self._reduce_kleene(popped_items1)
                self._match()
                return
                
            elif popped_items2 in self._rules['union']:
            
                # This check is for handling rules of the form X|YZ correctly where YZ forms concatenation
                if [self._next] in self._rules['empty'] or [self._next] in self._rules['single']:
                    break
                else:
                    self._reduce_union(popped_items1)
                    self._match()
                    return
        
        # Push popped items back to stacks if none of the rules matched
        for i in popped_items1:
            self._stack1.append(i)
            
        for i in popped_items2:
            self._stack2.append(i)
            
    def _match_next_is_kleene(self):
        popped_item1 = [self._stack1.pop()]
        popped_item2 = [self._stack2.pop()]
        
        if popped_item2 in self._rules['empty']:
            self._reduce_empty()
            return
            
        elif popped_item2 in self._rules['single']:
            self._reduce_single(popped_item1)
            return
        
        self._stack1.append(popped_item1[0])
        self._stack2.append(popped_item2[0])
        self._match()

    def parse(self, string):
        """Create a parse tree from the given regular experssion."""
        
        # Empty input is not same as empty string, since empty string has own symbol '.'
        # TODO: Empty input could be interpret as empty language
        if string == '':
            raise Exception('Input for parser must not be empty. Empty string is denoted as a dot: . ')
        
        self._stack1 = []
        self._stack2 = []

        for i in range(len(string)):
            self._stack1.append(string[i])
            self._stack2.append(string[i])
            
            if i < len(string) - 1:
                self._next = string[i+1]
            else:
                self._next = ''
            
            if self._next == '*':
                self._match_next_is_kleene()
            else:
                self._match()
            
        self._reduce_top()
        self._stack1 = None
        self._stack2 = None
        self._next = None
