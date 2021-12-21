from props import regex_production_rules
from entities.node import Node

class Parser:
    """A class for shift-reduce parser to parse regular expressions."""

    def __init__(self):
        self._rules = regex_production_rules

        # Stack for terminals and non-terminals
        self._stack1 = None

        # Assisting stack for just easier determining of prodcution rules
        self._stack2 = None

        self._next = None
        self.result = None

    def __str__(self):
        return f'{self.result}'

    def _reduce_empty(self):
        """Performs a reduce action for rule . -> empty."""

        node = Node('empty')
        self._stack1.append(node)
        self._stack2.append('empty')

    def _reduce_single(self, items):
        """Perfoms a reduce action for rule wherein left side is single."""

        node = Node('single', label=items[0])
        self._stack1.append(node)
        self._stack2.append('single')

    def _reduce_concatenation(self, items):
        """Performs a reduce action for rule wherein left side is concatenation."""

        # Check which one of the rule forms appears: XX, (X)X, X(X), (X)(X)
        if isinstance(items[0], Node) and isinstance(items[1], Node):
            left = items[0]
            right = items[1]
        elif isinstance(items[0], Node) and isinstance(items[2], Node):
            left = items[0]
            right = items[2]
        elif isinstance(items[1], Node) and isinstance(items[3], Node):
            left = items[1]
            right = items[3]
        elif isinstance(items[1], Node) and isinstance(items[4], Node):
            left = items[1]
            right = items[4]
        else:
            raise Exception('Syntax error.')

        node = Node('concatenation', left=left, right=right)

        self._stack1.append(node)
        self._stack2.append('concatenation')

    def _reduce_kleene(self, items):
        """Performs a reduce action for rule wherein left side is kleene."""

        # Check which one of the rule forms appears: X*, (X)*
        if isinstance(items[0], Node):
            left = items[0]
        elif isinstance(items[1], Node):
            left = items[1]
        else:
            raise Exception('Syntax error.')

        node = Node('kleene', left=left)

        self._stack1.append(node)
        self._stack2.append('kleene')

    def _reduce_union(self, items):
        """Performs a reduce action for rule wherein left side is union."""

        # Check which one of the rule forms appears: X|X, X|(X), (X)|X, (X)|(X)
        if isinstance(items[0], Node) and isinstance(items[2], Node):
            left = items[0]
            right = items[2]
        elif isinstance(items[0], Node) and isinstance(items[3], Node):
            left = items[0]
            right = items[3]
        elif isinstance(items[1], Node) and isinstance(items[4], Node):
            left = items[1]
            right = items[4]
        elif isinstance(items[1], Node) and isinstance(items[5], Node):
            left = items[1]
            right = items[5]
        else:
            raise Exception('Syntax error.')

        node = Node('union', left=left, right=right)

        self._stack1.append(node)
        self._stack2.append('union')

    def _reduce_top(self):
        """Performs a reduce action for rule wherein left side is top."""

        item = []
        item.append(self._stack2.pop())

        if item in self._rules['top'] and len(self._stack2) == 0:
            self.result = self._stack1[0]
        else:
            raise Exception('Syntax error.')

    def _match(self):
        """Pops items from stack and reduce if a production rule matches.

        Pops items from stack one by one, and after every pop, tests popped items against
        production rules for a match. Since the longest rule, (union)|(union), contains seven
        items, pop at most seven items from stack. If any production rule matches, then performs
        reduce action and tests again for a new match. If none of the rules matched, then pushs
        items back to stacks.

        """

        popped_items1 = []
        popped_items2 = []

        for _ in range(7):
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

                # This check is for handling rules of the form X(Y|Z)* correctly
                if self._next == '*':
                    break

                self._reduce_concatenation(popped_items1)
                self._match()
                return

            elif popped_items2 in self._rules['kleene']:
                self._reduce_kleene(popped_items1)
                self._match()
                return

            elif popped_items2 in self._rules['union']:
                # This check is for handling rules of the form X|(Y|Z)* and X|(Y|Z)(W) correctly
                if self._next in ['*', '(']:
                    break

                # This check is for handling rules of the form X|YZ correctly where YZ forms
                # concatenation
                if [self._next] in self._rules['empty'] or \
                   [self._next] in self._rules['single']:
                    break

                self._reduce_union(popped_items1)
                self._match()
                return

        for item in popped_items1:
            self._stack1.append(item)

        for item in popped_items2:
            self._stack2.append(item)

    def _match_next_is_asterisk(self):
        """Pops items from stack and reduce if a production rule matches.
        
        The general _match method cannot be used directly if the next input character is an
        asterisk. For example, if the top item in the stack is character a, _match method would
        produce a single, and then it would continue matching. With an asterisk being the next
        input character, the character a in the stack reduces to single and then to kleene in the
        next round.
        
        In order to parse regular expression correctly, a subset of the production rules must be
        checked for a match. If any of these rules matches, then perform reduce action and continue
        to scanning the input. If none of these rules matches, then it is safe to move to the
        regular match method.

        """

        popped_item1 = [self._stack1.pop()]
        popped_item2 = [self._stack2.pop()]

        if popped_item2 in self._rules['empty']:
            self._reduce_empty()
            return

        elif popped_item2 in self._rules['single']:
            self._reduce_single(popped_item1)
            return

        popped_item1.insert(0, self._stack1.pop())
        popped_item2.insert(0, self._stack2.pop())

        if popped_item2 in self._rules['kleene']:
            self._reduce_kleene(popped_item1)
            return

        self._stack1.append(popped_item1[0])
        self._stack1.append(popped_item1[1])
        self._stack2.append(popped_item2[0])
        self._stack2.append(popped_item2[1])
        self._match()

    def parse(self, string):
        """Constructs a parse tree from the given regular expression.

        The given regular expression is parsed character by character from the beginning to the end
        using shift-reduce method and simultaneously constructs the corresponing parse tree by
        bottom-up, i.e. from nodes towards the root.

        On each character, shift action moves the character into stack, after which production
        rules are tested for match in order to perform reduce actions. Finally, parsing is accepted
        or declined.

        If parsing is successful, the parse tree will be stored in the public variable 'result',
        else error will be raised.

        Args:
            string (str): The regular expression to be parsed.

        """

        self.result = None

        # Empty input is not same as empty string, since empty string has own symbol '.'
        # TODO: Empty input could be interpret as empty language
        if string == '':
            raise Exception('Input for parser must not be empty. Empty string is denoted as a dot: . ')

        self._stack1 = []
        self._stack2 = []

        for i in range(len(string)):
        
            # Shift operation here
            self._stack1.append(string[i])
            self._stack2.append(string[i])

            if i < len(string) - 1:
                self._next = string[i+1]
            else:
                self._next = ''

            # Check in match or match_next_is_asterisk if reduce operation can be performed
            if self._next == '*':
                self._match_next_is_asterisk()
            else:
                self._match()

        self._match()
        self._reduce_top()
        self._stack1 = None
        self._stack2 = None
        self._next = None
