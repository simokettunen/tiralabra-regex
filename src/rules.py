"""
Collection of the production rules of context-free grammar of regular expression string.

Basically, this file forms a context-free grammar for regular expression string with the following
settings:

Variables:
- empty
- single
- union
- concatenation
- kleene
- top

Start variable: top

Terminals:
- characters a-z, A-Z and 0-9,
- empty string, denoted as .
- operation characters * and |
- control characters ( and )

The dictionary "rules" forms the collection of production rules. Every key in the dictionary is
left-hand side of rule and list value of the key forms right-hand side of the rule. For example,
for the Kleene star, production rule is

    kleene -> empty *
            | single *
            | ( union ) *
            | ( concatenation ) *
            | kleene *

"""

rules = {
    'top': [
        ['empty'],
        ['single'],
        ['union'],
        ['concatenation'],
        ['kleene'],
    ],
   
    'empty': [
        ['.'],
    ],
    
    'single': [
        ['a'],
        ['b'],
        ['c'],
        ['d'],
        ['e'],
        ['f'],
        ['g'],
        ['h'],
        ['i'],
        ['j'],
        ['k'],
        ['l'],
        ['m'],
        ['n'],
        ['o'],
        ['p'],
        ['q'],
        ['r'],
        ['s'],
        ['t'],
        ['u'],
        ['v'],
        ['w'],
        ['x'],
        ['y'],
        ['z'],
        ['A'],
        ['B'],
        ['C'],
        ['D'],
        ['E'],
        ['F'],
        ['G'],
        ['H'],
        ['I'],
        ['J'],
        ['K'],
        ['L'],
        ['M'],
        ['N'],
        ['O'],
        ['P'],
        ['Q'],
        ['R'],
        ['S'],
        ['T'],
        ['U'],
        ['V'],
        ['W'],
        ['X'],
        ['Y'],
        ['Z'],
        ['0'],
        ['1'],
        ['2'],
        ['3'],
        ['4'],
        ['5'],
        ['6'],
        ['7'],
        ['8'],
        ['9'],
    ],
    
    'union': [
        ['empty', '|', 'empty'],
        ['empty', '|', 'single'],
        ['empty', '|', '(', 'union', ')'],
        ['empty', '|', 'concatenation'],
        ['empty', '|', 'kleene'],
        ['single', '|', 'empty'],
        ['single', '|', 'single'],
        ['single', '|', '(', 'union', ')'],
        ['single', '|', 'concatenation'],
        ['single', '|', 'kleene'],
        ['(', 'union', ')', '|', 'empty'],
        ['(', 'union', ')', '|', 'single'],
        ['(', 'union', ')', '|', '(', 'union', ')'],
        ['(', 'union', ')', '|', 'concatenation'],
        ['(', 'union', ')', '|', 'kleene'],
        ['concatenation', '|', 'empty'],
        ['concatenation', '|', 'single'],
        ['concatenation', '|', '(', 'union', ')'],
        ['concatenation', '|', 'concatenation'],
        ['concatenation', '|', 'kleene'],
        ['kleene', '|', 'empty'],
        ['kleene', '|', 'single'],
        ['kleene', '|', '(', 'union', ')'],
        ['kleene', '|', 'concatenation'],
        ['kleene', '|', 'kleene'],
    ],
    
    'concatenation': [
        ['empty', 'empty'],
        ['empty', 'single'],
        ['empty', '(', 'union', ')'],
        ['empty', 'concatenation'],
        ['empty', 'kleene'],
        ['single', 'empty'],
        ['single', 'single'],
        ['single', '(', 'union', ')'],
        ['single', 'concatenation'],
        ['single', 'kleene'],
        ['(', 'union', ')', 'empty'],
        ['(', 'union', ')', 'single'],
        ['(', 'union', ')', '(', 'union', ')'],
        ['(', 'union', ')', 'concatenation'],
        ['(', 'union', ')', 'kleene'],
        ['concatenation', 'empty'],
        ['concatenation', 'single'],
        ['concatenation', '(', 'union', ')'],
        ['concatenation', 'concatenation'],
        ['concatenation', 'kleene'],
        ['kleene', 'empty'],
        ['kleene', 'single'],
        ['kleene', '(', 'union', ')'],
        ['kleene', 'concatenation'],
        ['kleene', 'kleene'],
    ],
    
    'kleene': [
        ['empty', '*'],
        ['single', '*'],
        ['(', 'union', ')', '*'],
        ['(', 'concatenation', ')', '*'],
        ['kleene', '*'],
    ]
}
