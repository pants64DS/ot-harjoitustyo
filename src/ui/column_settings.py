import numpy
import calculation.fixed_point as fixed_point

class ColumnSettings:
    def __init__(self, on_changed):
        self._on_changed = on_changed
        self._float_parser = numpy.float32
        self._fixed_parser = fixed_point.FixedPointParser(12)
        self._num_display_digits = 12
        self._uses_floats = True

    def uses_floats(self):
        return self._uses_floats

    def get_parser(self):
        if self._uses_floats:
            return self._float_parser

        return self._fixed_parser

    def res_to_string(self, res):
        if isinstance(res, str):
            return res

        if self._uses_floats:
            return str(res)

        return res.to_string(10, self._num_display_digits)

    def enable_float_mode(self, precision=None):
        if precision == 16: self._float_parser = numpy.float16
        if precision == 32: self._float_parser = numpy.float32
        if precision == 64: self._float_parser = numpy.float64

        self._uses_floats = True
        self._on_changed()

    def get_float_precision(self):
        if self._float_parser is numpy.float16: return 16
        if self._float_parser is numpy.float32: return 32
        if self._float_parser is numpy.float64: return 64

        return None

    def enable_fixed_mode(self, num_frac_bits=None, num_display_digits=None):
        if num_frac_bits != None:
            self._fixed_parser = fixed_point.FixedPointParser(num_frac_bits)

        if num_display_digits != None:
            self._num_display_digits = num_display_digits

        self._uses_floats = False
        self._on_changed()

    def get_num_frac_bits(self):
        return self._fixed_parser.get_num_frac_bits()

    def get_num_display_digits(self):
        return self._num_display_digits

    def __str__(self):
        if self._uses_floats:
            return f'float{self.get_float_precision()}'

        return f'Q{self._fixed_parser.get_num_frac_bits()}, {self._num_display_digits} decimals'
