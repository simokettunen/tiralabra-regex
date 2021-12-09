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