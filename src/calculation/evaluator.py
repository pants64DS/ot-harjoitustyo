
_unary_operators = {
    '+': lambda a: +a,
    '-': lambda a: -a,
}

_binary_operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '%': lambda a, b: a % b,
    'L': lambda a, b: a * (1 << int(b)),
    'R': lambda a, b: a / (1 << int(b)),
}

# Precedence groups for *binary* operators
# Unary operators all share the same precedence.
_precedence_groups = (
    ('*', '/', '%'),
    ('+', '-'),
    ('L', 'R')
)

def _complete_parentheses(expr):
    """Adds just enough opening parentheses to the start of the expression
    and closing parentheses to the end of the expression to make each
    parenthesis have a pair

    Args:
        expr: The expression to add parentheses to

    Returns:
        The expression with parentheses added on both sides
    """

    level = 0
    min_level = 0

    for char in expr:
        level += int(char == '(') - int(char == ')')
        min_level = min(level, min_level)

    return -min_level * '(' + expr + (level - min_level) * ')'

def _find_binary_op(expr, precedence_group):
    """Finds the rightmost top-level binary operator in the expression
    that's in the given precedence group

    Args:
        expr: The expression to search for the operator in
        precedence_group: A tuple of binary operators to search for

    Returns:
        The index of the rightmost binary operator within the expression
            that's in the given precedence group
    """

    level = 0
    for i in reversed(range(1, len(expr))):
        level += int(expr[i] == ')') - int(expr[i] == '(')

        if level == 0 and expr[i] in precedence_group:
            if expr[i - 1] not in _binary_operators:
                return i
    return None

class Evaluator:
    """A class that evaluates arithmetic expressions.

    Attributes:
        _literal_parser: A class, function or callable object that allows
            creating a scalar value from a string representation
    """

    def __init__(self, literal_parser):
        """Evaluator's constructor.

        Args:
            literal_parser: A class, function or callable object that allows
            creating a scalar value from a string representation
        """

        self._literal_parser = literal_parser

    def _eval_unary_expr(self, expr):
        """Evaluates an expression with no top-level binary operators.
        Args:
            expr: The expression to evaluate
        Returns:
            The result of the expression as a scalar type
        """

        if expr[0] == '(':
            return self._eval_complete(expr[1:-1])

        if expr[0] in _unary_operators:
            operand = self._eval_unary_expr(expr[1:])

            return _unary_operators[expr[0]](operand)

        return self._literal_parser(expr)

    def _eval_binary_expr(self, expr, pos, precedence):
        """Evaluates an expression with a top-level binary operator.

        Args:
            expr: The expression to evaluate
            pos: The index of the rightmost top-level binary
                operator in the expression with the given precedence.
                Therefore the sub-expression on its right side only contains
                top-level binary operators with lower precedence

            precedence: The index of a corresponding precedence group in
                the _precedence_groups array
        Returns:
            The result of the expression as a scalar type
        """

        lhs = self._eval_complete(expr[:pos], precedence)
        rhs = self._eval_complete(expr[pos + 1:], precedence - 1)

        return _binary_operators[expr[pos]](lhs, rhs)

    def _eval_complete(self, expr, precedence=len(_precedence_groups)-1):
        """Evaluates any expression that only contains binary operators
        with the given precedence or lower

        Args:
            expr: The expression to evaluate
            precedence: The index of a corresponding precedence group in
                the _precedence_groups array
        Returns:
            The result of the expression as a scalar type
        """

        if precedence < 0:
            return self._eval_unary_expr(expr) # No precedence groups to check

        op_pos = _find_binary_op(expr, _precedence_groups[precedence])

        if op_pos:
            return self._eval_binary_expr(expr, op_pos, precedence)

        # The expression contains no top-level binary operators from the given
        # precedence group, so the lower precedence group can be checked next
        return self._eval_complete(expr, precedence - 1)

    def evaluate(self, expr):
        """Preprocesses an expression, evaluates it and returns its result as a scalar type

        Args:
            expr: The expression to evaluate
        Returns:
            The result of the expression as a scalar type
        """

        expr = expr.replace(' ', '')

        if not expr:
            return ''

        expr = expr.lower().replace('<<', 'L').replace('>>', 'R')
        expr = _complete_parentheses(expr)

        return self._eval_complete(expr)

    def evaluate_to_string(self, expr):
        """Preprocesses an expression, evaluates it and returns its result as a string

        Args:
            expr: The expression to evaluate
        Returns:
            The result of the expression as a string
        """

        try:
            res = str(self.evaluate(expr))
        except ZeroDivisionError:
            return 'undef'
        except:
            return 'invalid'

        if res.endswith('.0'):
            res = res[:-2]

        return res
