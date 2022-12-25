
def _add_prefix(literal, radix):
    if radix == 2:
        return '0b' + literal

    if radix == 16:
        return '0x' + literal

    return literal

def _digits_to_string(digits):
    if '.' not in digits and '0.' not in digits:
        return ''.join(digits[::-1])

    num_digits_to_trim = 0

    while num_digits_to_trim < len(digits) and digits[num_digits_to_trim] == '0':
        num_digits_to_trim += 1

    if num_digits_to_trim < len(digits) and digits[num_digits_to_trim] in ('.', '0.'):
        num_digits_to_trim += 1

    return ''.join(digits[num_digits_to_trim:][::-1])

def _parse_prefix(literal):
    if literal.startswith('0x'):
        return literal[2:], 16
    if literal.startswith('0b'):
        return literal[2:], 2

    return literal, 10

def _add_fractional_point(digits, num_frac_digits):
    if num_frac_digits > 0:
        if num_frac_digits == len(digits):
            digits.insert(num_frac_digits, '0.')
        else:
            digits.insert(num_frac_digits, '.')

    return digits

class FixedPoint:
    def __init__(self, raw, num_frac_bits):
        self._raw = raw
        self._num_frac_bits = num_frac_bits

    def __add__(self, other):
        assert self._num_frac_bits == other._num_frac_bits

        return FixedPoint(self._raw + other._raw, self._num_frac_bits)

    def __sub__(self, other):
        assert self._num_frac_bits == other._num_frac_bits

        return FixedPoint(self._raw - other._raw, self._num_frac_bits)

    def __mul__(self, other):
        raw_result = self._raw * other._raw >> other._num_frac_bits

        return FixedPoint(raw_result, self._num_frac_bits)

    def __truediv__(self, other):
        raw_result = (self._raw << other._num_frac_bits) // other._raw

        return FixedPoint(raw_result, self._num_frac_bits)

    def __mod__(self, other):
        assert self._num_frac_bits == other._num_frac_bits

        return FixedPoint(self._raw % other._raw, self._num_frac_bits)

    def __neg__(self):
        return FixedPoint(-self._raw, self._num_frac_bits)

    def __pos__(self):
        return FixedPoint(+self._raw, self._num_frac_bits)

    def to_string(self, radix, max_frac_digits):
        if self._raw == 0:
            return _add_prefix('0', radix)

        sign = (self._raw < 0) * '-'
        raw = -self._raw if sign else self._raw
        raw *= radix ** max_frac_digits

        if self._num_frac_bits > 0:
            raw += (1 << (self._num_frac_bits - 1))
            raw >>= self._num_frac_bits

        digits = []
        while raw or len(digits) < max_frac_digits:
            digits.append('0123456789abcdef'[raw % radix])
            raw //= radix

        digits = _add_fractional_point(digits, max_frac_digits)
        return sign + _add_prefix(_digits_to_string(digits), radix)

    def __str__(self):
        return self.to_string(10, 12)

    def get_raw(self):
        return self._raw

class FixedPointParser:
    def __init__(self, num_frac_bits):
        self._num_frac_bits = num_frac_bits

    def __call__(self, literal):
        literal, radix = _parse_prefix(literal)
        point_index = literal.find('.')

        if point_index == -1:
            num_frac_digits = 0
        else:
            literal = literal[:point_index] + literal[point_index + 1:]
            num_frac_digits = len(literal) - point_index

        power = radix ** num_frac_digits
        raw = ((int(literal, radix) << self._num_frac_bits) + (power >> 1)) // power

        return FixedPoint(raw, self._num_frac_bits)

    def get_num_frac_bits(self):
        return self._num_frac_bits
