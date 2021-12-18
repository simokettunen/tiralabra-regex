class Node:
    """TODO"""

    def __init__(self, type, label=None):
        self.type = type
        self.left = None
        self.right = None
        
        if type == 'empty':
            self.label = '.'
        elif type in ['single', 'concatenation', 'kleene', 'union']:
            self.label = label
        else:
            raise Exception(f'Incorrect node type: {type}')
  
    def __str__(self):
        if self.type in ['concatenation', 'kleene', 'union']:
            return f'({self.type[0]} {self.left.__str__()} {self.right.__str__()})'
            
        if self.label is None:
            return ''
            
        return self.label