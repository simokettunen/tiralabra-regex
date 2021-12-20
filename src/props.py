"""Collection of different properties."""

# The variable alphabet forms an alphabet for an language that regular expression in the program
# accepts.
alphabet_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
alphabet_uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_digits = '0123456789'
alphabet = alphabet_lowercase_letters + alphabet_uppercase_letters + alphabet_digits

# The variable regex_production_rules forms a context-free grammar for regular expression string
# with the following settings:
# 
# Variables:
# - empty
# - single
# - union
# - concatenation
# - kleene
# - top
# 
# Start variable: top
# 
# Terminals:
# - characters a-z, A-Z and 0-9,
# - empty string, denoted as .
# - operation characters * and |
# - control characters ( and )
# 
# Every key in the dictionary is left-hand side of rule and list value of the key forms right-hand
# side of the rule. For example, for the Kleene star, the collection production rules is
# 
#     kleene -> empty *
#             | single *
#             | ( union ) *
#             | ( concatenation ) *
#             | kleene *

regex_production_rules = {
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
        [symbol] for symbol in alphabet
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
    ],
}
