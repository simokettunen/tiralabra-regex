class Node:
    def __init__(self, type, label=None):
        self.label = label
        self.type = type
        self.left = None
        self.right = None
        
    def __str__(self):
        if self.type in ['c', 'k', 'u']:
            return f'({self.type} {self.left.__str__()} {self.right.__str__()})'
            
        if self.label is None:
            return ''
            
        return self.label
               