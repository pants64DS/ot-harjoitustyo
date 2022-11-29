import unittest
import itertools
from calculation.evaluator import Evaluator

def _generate_expressions(length, digits, unary_ops, binary_ops):
    if length <= 0: return set()
    if length == 1: return digits

    res = set()

    for expr in _generate_expressions(length - 1, digits, unary_ops, binary_ops):
        for unary_op in unary_ops:
            res.add(unary_op + expr)

    for expr in _generate_expressions(length - 2, digits, unary_ops, binary_ops):
        res.add('(' + expr + ')')

    for binary_op in binary_ops:
        for binary_op_pos in range(1, length - 1):
            for lhs in _generate_expressions(binary_op_pos, digits, unary_ops, binary_ops):
                for rhs in _generate_expressions(length - binary_op_pos - 1, digits, unary_ops, ()):
                    res.add(lhs + binary_op + rhs)
    return res

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.e = Evaluator(float)

    def test_literal_parsing(self):
        for x in range(0, 1000):
            x /= 10
            self.assertEqual(self.e.evaluate(str(x)), x)

    def test_unary_plus(self):
        for x in range(0, 1000):
            x /= 10
            for i in range(1, 11):
                self.assertEqual(self.e.evaluate(f'{"+" * i}{x}'), x)

    def test_unary_minus(self):
        for x in range(0, 1000):
            x /= 10
            for i in range(1, 11):
                self.assertEqual(self.e.evaluate(f'{"-" * i}{x}'), -x if i & 1 else x)

    def test_addition(self):
        for x in range(-100, 100):
            for y in range(-100, 100):
                expr = f'{x} + {y}'
                self.assertEqual(self.e.evaluate(expr), x + y)

    def test_subtraction(self):
        for x in range(-100, 100):
            for y in range(-100, 100):
                expr = f'{x} - {y}'
                self.assertEqual(self.e.evaluate(expr), x - y)

    def test_multiplication(self):
        for x in range(-100, 100):
            for y in range(-100, 100):
                expr = f'{x} * {y}'
                self.assertEqual(self.e.evaluate(expr), x * y)

    def test_division(self):
        for x in range(-100, 100):
            for y in itertools.chain(range(-100, 0), range(1, 100)): # skip zero
                expr = f'{x} / {y}'
                self.assertEqual(self.e.evaluate(expr), x / y)

    def test_modulo(self):
        for x in range(-100, 100):
            for y in itertools.chain(range(-100, 0), range(1, 100)): # skip zero
                expr = f'{x} % {y}'
                self.assertEqual(self.e.evaluate(expr), x % y)

    def test_precedence(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                for z in range(-10, 10):
                    expr1 = f'{x} + {y} * {z}'
                    expr2 = f'{x} * {y} + {z}'

                    self.assertEqual(self.e.evaluate(expr1), x + y * z)
                    self.assertEqual(self.e.evaluate(expr2), x * y + z)

    def test_parentheses(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                for z in range(-10, 10):
                    expr1 = f'({x} + {y}) * {z}'
                    expr2 = f'{x} * ({y} + {z})'

                    self.assertEqual(self.e.evaluate(expr1), (x + y) * z)
                    self.assertEqual(self.e.evaluate(expr2), x * (y + z))

    # Test all expressions that are less than 8 characters long and only contain literals
    # 2, 3 and 5, and use operators +, - and *, including both unary and binary plus and minus.
    def test_combined(self):
        for i in range(0, 8):
            expressions = _generate_expressions(i, {'2', '3', '5'}, ('+', '-'), ('+', '-', '*'))

            for expr in expressions:
                self.assertEqual(self.e.evaluate(expr), eval(expr))

    def test_formatting(self):
        self.assertEqual(self.e.evaluate_to_string('0.0'), '0')
        self.assertEqual(self.e.evaluate_to_string('1.0'), '1')
        self.assertEqual(self.e.evaluate_to_string('+1.5'), '1.5')
        self.assertEqual(self.e.evaluate_to_string('-1.5'), '-1.5')

    def test_undefined_result(self):
        self.assertEqual(self.e.evaluate_to_string('1/0'), 'undef')
        self.assertEqual(self.e.evaluate_to_string('0/0'), 'undef')

    def test_invalid_expr(self):
        self.assertEqual(self.e.evaluate_to_string('1/'), 'invalid')
        self.assertEqual(self.e.evaluate_to_string(')('), 'invalid')
        self.assertEqual(self.e.evaluate_to_string('#'),  'invalid')

    def test_empty_expr(self):
        self.assertEqual(self.e.evaluate_to_string(''), '')
