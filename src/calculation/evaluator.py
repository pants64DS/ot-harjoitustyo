
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
}

# Precedence groups for *binary* operators
# Unary operators all share the same precedence
_precedence_groups = (
	('*', '/', '%'),
	('+', '-'),
)

# Adds just enough opening parentheses to the start of the expression
# and closing parentheses to the end of the expression to make each
# parenthesis have a pair 
def _complete_parentheses(expr):
	level = 0
	min_level = 0

	for c in expr:
		level += int(c == '(') - int(c == ')')
		min_level = min(level, min_level)

	return -min_level * '(' + expr + (level - min_level) * ')'

# Finds the rightmost top-level binary operator in the expression
# that's in the given precedence group
def _find_binary_op(expr, precedence_group):
	level = 0
	for i in reversed(range(1, len(expr))):
		level += int(expr[i] == ')') - int(expr[i] == '(')

		if level == 0 and expr[i] in precedence_group:
			if expr[i - 1] not in _binary_operators:
				return i

class Evaluator:
	def __init__(self, literal_parser):
		self.literal_parser = literal_parser

	# Evaluates an expression with no top-level binary operators
	def _eval_unary_expr(self, expr):
		if expr[0] == '(':
			return self._eval_complete(expr[1:-1])

		if expr[0] in _unary_operators:
			operand = self._eval_unary_expr(expr[1:])

			return _unary_operators[expr[0]](operand)

		return self.literal_parser(expr)

	# "pos" is assumed to be the index of the rightmost top-level
	# binary operator in the expression with the given precedence.
	# Therefore the sub-expression on its right side only contains
	# top-level binary operators with lower precedence.
	def _eval_binary_expr(self, expr, pos, precedence):
		lhs = self._eval_complete(expr[:pos], precedence)
		rhs = self._eval_complete(expr[pos + 1:], precedence - 1)

		return _binary_operators[expr[pos]](lhs, rhs)

	def _eval_complete(self, expr, precedence=len(_precedence_groups)-1):
		if precedence < 0:
			return self._eval_unary_expr(expr) # No precedence groups to check

		op_pos = _find_binary_op(expr, _precedence_groups[precedence])

		if op_pos:
			return self._eval_binary_expr(expr, op_pos, precedence)

		# The expression contains no top-level binary operators from the given
		# precedence group, so the lower precedence group can be checked next
		return self._eval_complete(expr, precedence - 1)

	def evaluate(self, expr):
		expr = expr.replace(' ', '')
		expr = expr.lower()
		expr = _complete_parentheses(expr)

		return self._eval_complete(expr)
