import unittest
import itertools
from calculation.fixed_point import FixedPoint, FixedPointParser

class TestFixedPoint(unittest.TestCase):
    def setup(self):
        pass

    def test_get_raw(self):
        for q in range(32):
            for a in range(-32, 33):
                x = FixedPoint(a, q)
                self.assertEqual(x.get_raw(), a)

    def test_addition(self):
        for q in range(32):
            for a in range(-32, 33):
                for b in range(-32, 33):
                    x = FixedPoint(a, q)
                    y = FixedPoint(b, q)

                    self.assertEqual((x + y).get_raw(), a + b)

    def test_subtraction(self):
        for q in range(32):
            for a in range(-32, 33):
                for b in range(-32, 33):
                    x = FixedPoint(a, q)
                    y = FixedPoint(b, q)

                    self.assertEqual((x - y).get_raw(), a - b)

    def test_multiplication(self):
        for q in range(32):
            for a in range(-32, 33):
                for b in range(-32, 33):
                    x = FixedPoint(a, q)
                    y = FixedPoint(b, q)

                    self.assertEqual((x * y).get_raw(), a * b >> q)

    def test_division(self):
        for q in range(32):
            for a in range(-32, 33):
                for b in itertools.chain(range(-32, 0), range(1, 32)):
                    x = FixedPoint(a, q)
                    y = FixedPoint(b, q)

                    self.assertEqual((x / y).get_raw(), (a << q) // b)

    def test_modulo(self):
        for q in range(32):
            for a in range(-32, 33):
                for b in itertools.chain(range(-32, 0), range(1, 32)):
                    x = FixedPoint(a, q)
                    y = FixedPoint(b, q)

                    self.assertEqual((x % y).get_raw(), a % b)

    def test_left_shift(self):
        for q in range(32):
            for a in range(-32, 33):
                for b in range(0, 33):
                    x = FixedPoint(a, q)

                    self.assertEqual((x * (1 << b)).get_raw(), a << b)

    def test_right_shift(self):
        for q in range(32):
            for a in range(-32, 33):
                for b in range(0, 33):
                    x = FixedPoint(a, q)

                    self.assertEqual((x / (1 << b)).get_raw(), a >> b)

    def test_negation(self):
        for q in range(32):
            for a in range(-32, 33):
                x = FixedPoint(a, q)
                self.assertEqual((-x).get_raw(), -a)

    def test_identity(self):
        for q in range(32):
            for a in range(-32, 33):
                x = FixedPoint(a, q)
                self.assertEqual((+x).get_raw(), +a)

    def test_integer_to_dec_string(self):
        for q in range(32):
            for n in range(10):
                for a in range(33):
                    x = FixedPoint(a << q, q)
                    self.assertEqual(x.to_string(10, n), str(a))

    def test_integer_to_hex_string(self):
        for q in range(32):
            for n in range(10):
                for a in range(33):
                    x = FixedPoint(a << q, q)
                    self.assertEqual(x.to_string(16, n), hex(a))

    def test_integer_to_bin_string(self):
        for q in range(32):
            for n in range(10):
                for a in range(33):
                    x = FixedPoint(a << q, q)
                    self.assertEqual(x.to_string(2, n), bin(a))

    def test_fraction_to_dec_string(self):
        for n in range(32):
            for s, q in (('.5', 1), ('.25', 2), ('.125', 3), ('.0625', 4)):
                for i in range(4):
                    self.assertEqual(FixedPoint((n << q << i) + (1 << i), q + i).to_string(10, 4), str(n) + s)

    def test_fraction_to_hex_string(self):
        for n in range(32):
            for s, q in (('.8', 1), ('.4', 2), ('.2', 3), ('.1', 4)):
                for i in range(4):
                    self.assertEqual(FixedPoint((n << q << i) + (1 << i), q + i).to_string(16, 4), hex(n) + s)

    def test_fraction_to_bin_string(self):
        for n in range(256):
            for q in range(1, 32):
                s = f'.{"0" * (q - 1)}1'
                for i in range(4):
                    self.assertEqual(FixedPoint((n << q << i) + (1 << i), q + i).to_string(2, q), bin(n) + s)

    def test_to_int(self):
        for q in range(32):
            for a in range(256):
                x = FixedPoint(a, q)
                self.assertEqual(int(x), a >> q)

    def test_default_string(self):
        for q in range(32):
            for a in range(33):
                x = FixedPoint(a << q, q)
                self.assertEqual(str(x), str(a))

class TestFixedPointParser(unittest.TestCase):
    def setUp(self):
        self.parsers = [FixedPointParser(i) for i in range(32)]

    def test_get_num_frac_bits(self):
        for q in range(len(self.parsers)):
            self.assertEqual(self.parsers[q].get_num_frac_bits(), q)

    def test_parsing_dec_integers(self):
        for q in range(len(self.parsers)):
            for i in range(-255, 256):
                self.assertEqual(self.parsers[q](str(i)).get_raw(), i << q)

    def test_parsing_zero(self):
        for q in range(len(self.parsers)):
            self.assertEqual(self.parsers[q]('0'   ).get_raw(), 0)
            self.assertEqual(self.parsers[q]('0.'  ).get_raw(), 0)
            self.assertEqual(self.parsers[q]('.0'  ).get_raw(), 0)
            self.assertEqual(self.parsers[q]('0.0' ).get_raw(), 0)
            self.assertEqual(self.parsers[q]('0.00').get_raw(), 0)
            self.assertEqual(self.parsers[q]('00.0').get_raw(), 0)

    def test_dec_parsing_when_rounding_down(self):
        self.assertEqual(self.parsers[0]('.1'    ).get_raw(), 0)
        self.assertEqual(self.parsers[0]('.20'   ).get_raw(), 0)
        self.assertEqual(self.parsers[1]('.220'  ).get_raw(), 0)
        self.assertEqual(self.parsers[1]('.210'  ).get_raw(), 0)
        self.assertEqual(self.parsers[2]('.124'  ).get_raw(), 0)
        self.assertEqual(self.parsers[2]('.1199' ).get_raw(), 0)
        self.assertEqual(self.parsers[3]('.0555' ).get_raw(), 0)
        self.assertEqual(self.parsers[3]('.00625').get_raw(), 0)

        for i in range(256):
            self.assertEqual(self.parsers[0](f'{i}.1'    ).get_raw(), i << 0)
            self.assertEqual(self.parsers[0](f'{i}.20'   ).get_raw(), i << 0)
            self.assertEqual(self.parsers[1](f'{i}.22'   ).get_raw(), i << 1)
            self.assertEqual(self.parsers[1](f'{i}.210'  ).get_raw(), i << 1)
            self.assertEqual(self.parsers[2](f'{i}.124'  ).get_raw(), i << 2)
            self.assertEqual(self.parsers[2](f'{i}.1199' ).get_raw(), i << 2)
            self.assertEqual(self.parsers[3](f'{i}.0555' ).get_raw(), i << 3)
            self.assertEqual(self.parsers[3](f'{i}.00625').get_raw(), i << 3)

    def test_hex_parsing_when_rounding_down(self):
        self.assertEqual(self.parsers[0]('0x.1'    ).get_raw(), 0)
        self.assertEqual(self.parsers[0]('0x.3f'   ).get_raw(), 0)
        self.assertEqual(self.parsers[1]('0x.1a'   ).get_raw(), 0)
        self.assertEqual(self.parsers[1]('0x.0d0'  ).get_raw(), 0)
        self.assertEqual(self.parsers[2]('0x.1e'   ).get_raw(), 0)
        self.assertEqual(self.parsers[2]('0x.1fff' ).get_raw(), 0)
        self.assertEqual(self.parsers[3]('0x.03'   ).get_raw(), 0)
        self.assertEqual(self.parsers[3]('0x.0ffff').get_raw(), 0)

        for i in range(256):
            self.assertEqual(self.parsers[0](f'{hex(i)}.1'    ).get_raw(), i << 0)
            self.assertEqual(self.parsers[0](f'{hex(i)}.3f'   ).get_raw(), i << 0)
            self.assertEqual(self.parsers[1](f'{hex(i)}.1a'   ).get_raw(), i << 1)
            self.assertEqual(self.parsers[1](f'{hex(i)}.0d0'  ).get_raw(), i << 1)
            self.assertEqual(self.parsers[2](f'{hex(i)}.1e'   ).get_raw(), i << 2)
            self.assertEqual(self.parsers[2](f'{hex(i)}.1fff' ).get_raw(), i << 2)
            self.assertEqual(self.parsers[3](f'{hex(i)}.03'   ).get_raw(), i << 3)
            self.assertEqual(self.parsers[3](f'{hex(i)}.0ffff').get_raw(), i << 3)

    def test_bin_parsing_when_rounding_down(self):
        self.assertEqual(self.parsers[0]('0b.01'   ).get_raw(), 0)
        self.assertEqual(self.parsers[0]('0b.0111' ).get_raw(), 0)
        self.assertEqual(self.parsers[1]('0b.001'  ).get_raw(), 0)
        self.assertEqual(self.parsers[1]('0b.00111').get_raw(), 0)
        self.assertEqual(self.parsers[2]('0b.0001' ).get_raw(), 0)
        self.assertEqual(self.parsers[2]('0b.00011').get_raw(), 0)
        self.assertEqual(self.parsers[3]('0b.00001').get_raw(), 0)
        self.assertEqual(self.parsers[3]('0b.00000').get_raw(), 0)

        for i in range(256):
            self.assertEqual(self.parsers[0](f'{bin(i)}.01'   ).get_raw(), i << 0)
            self.assertEqual(self.parsers[0](f'{bin(i)}.0111' ).get_raw(), i << 0)
            self.assertEqual(self.parsers[1](f'{bin(i)}.001'  ).get_raw(), i << 1)
            self.assertEqual(self.parsers[1](f'{bin(i)}.00111').get_raw(), i << 1)
            self.assertEqual(self.parsers[2](f'{bin(i)}.0001' ).get_raw(), i << 2)
            self.assertEqual(self.parsers[2](f'{bin(i)}.00011').get_raw(), i << 2)
            self.assertEqual(self.parsers[3](f'{bin(i)}.00001').get_raw(), i << 3)
            self.assertEqual(self.parsers[3](f'{bin(i)}.00000').get_raw(), i << 3)

    def test_dec_parsing_when_rounding_up(self):
        self.assertEqual(self.parsers[0]('.6'    ).get_raw(), 1)
        self.assertEqual(self.parsers[0]('.99'   ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('.3'    ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('.47'   ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('.13'   ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('.126'  ).get_raw(), 1)
        self.assertEqual(self.parsers[3]('.07'   ).get_raw(), 1)
        self.assertEqual(self.parsers[3]('.11111').get_raw(), 1)

        for i in range(256):
            self.assertEqual(self.parsers[0](f'{i}.6'    ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[0](f'{i}.99'   ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[1](f'{i}.3'    ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[1](f'{i}.47'   ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[2](f'{i}.13'   ).get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[2](f'{i}.126'  ).get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[3](f'{i}.07'   ).get_raw(), (i << 3) + 1)
            self.assertEqual(self.parsers[3](f'{i}.11111').get_raw(), (i << 3) + 1)

    def test_hex_parsing_when_rounding_up(self):
        self.assertEqual(self.parsers[0]('0x.9'    ).get_raw(), 1)
        self.assertEqual(self.parsers[0]('0x.ff'   ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('0x.5'    ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('0x.7ff0' ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('0x.22'   ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('0x.2001' ).get_raw(), 1)
        self.assertEqual(self.parsers[3]('0x.11'   ).get_raw(), 1)
        self.assertEqual(self.parsers[3]('0x.1ffff').get_raw(), 1)

        for i in range(256):
            self.assertEqual(self.parsers[0](f'{hex(i)}.9'    ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[0](f'{hex(i)}.ff'   ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[1](f'{hex(i)}.5'    ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[1](f'{hex(i)}.7ff0' ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[2](f'{hex(i)}.22'   ).get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[2](f'{hex(i)}.2001' ).get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[3](f'{hex(i)}.11'   ).get_raw(), (i << 3) + 1)
            self.assertEqual(self.parsers[3](f'{hex(i)}.1ffff').get_raw(), (i << 3) + 1)

    def test_bin_parsing_when_rounding_down(self):
        self.assertEqual(self.parsers[0]('0b.01'   ).get_raw(), 0)
        self.assertEqual(self.parsers[0]('0b.0111' ).get_raw(), 0)
        self.assertEqual(self.parsers[1]('0b.001'  ).get_raw(), 0)
        self.assertEqual(self.parsers[1]('0b.00111').get_raw(), 0)
        self.assertEqual(self.parsers[2]('0b.0001' ).get_raw(), 0)
        self.assertEqual(self.parsers[2]('0b.00011').get_raw(), 0)
        self.assertEqual(self.parsers[3]('0b.00001').get_raw(), 0)
        self.assertEqual(self.parsers[3]('0b.00000').get_raw(), 0)

        for i in range(256):
            self.assertEqual(self.parsers[0](f'{bin(i)}.01'   ).get_raw(), i << 0)
            self.assertEqual(self.parsers[0](f'{bin(i)}.0111' ).get_raw(), i << 0)
            self.assertEqual(self.parsers[1](f'{bin(i)}.001'  ).get_raw(), i << 1)
            self.assertEqual(self.parsers[1](f'{bin(i)}.00111').get_raw(), i << 1)
            self.assertEqual(self.parsers[2](f'{bin(i)}.0001' ).get_raw(), i << 2)
            self.assertEqual(self.parsers[2](f'{bin(i)}.00011').get_raw(), i << 2)
            self.assertEqual(self.parsers[3](f'{bin(i)}.00001').get_raw(), i << 3)
            self.assertEqual(self.parsers[3](f'{bin(i)}.00000').get_raw(), i << 3)

    def test_dec_parsing_edge_cases(self):
        self.assertEqual(self.parsers[0]('.5'    ).get_raw(), 1)
        self.assertEqual(self.parsers[0]('.50'   ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('.25'   ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('.250'  ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('.125'  ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('.1250' ).get_raw(), 1)
        self.assertEqual(self.parsers[3]('.0625' ).get_raw(), 1)
        self.assertEqual(self.parsers[3]('.06250').get_raw(), 1)

        for i in range(256):
            self.assertEqual(self.parsers[0](f'{i}.5'    ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[0](f'{i}.50'   ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[1](f'{i}.25'   ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[1](f'{i}.250'  ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[2](f'{i}.125'  ).get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[2](f'{i}.1250' ).get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[3](f'{i}.0625' ).get_raw(), (i << 3) + 1)
            self.assertEqual(self.parsers[3](f'{i}.06250').get_raw(), (i << 3) + 1)

    def test_hex_parsing_edge_cases(self):
        self.assertEqual(self.parsers[0]('0x.8'    ).get_raw(), 1)
        self.assertEqual(self.parsers[0]('0x.800'  ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('0x.4'    ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('0x.40'   ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('0x.2'    ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('0x.2000' ).get_raw(), 1)
        self.assertEqual(self.parsers[3]('0x.1'    ).get_raw(), 1)
        self.assertEqual(self.parsers[3]('0x.10000').get_raw(), 1)

        for i in range(256):
            self.assertEqual(self.parsers[0](f'{hex(i)}.8'    ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[0](f'{hex(i)}.800'  ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[1](f'{hex(i)}.4'    ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[1](f'{hex(i)}.40'   ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[2](f'{hex(i)}.2'    ).get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[2](f'{hex(i)}.2000' ).get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[3](f'{hex(i)}.1'    ).get_raw(), (i << 3) + 1)
            self.assertEqual(self.parsers[3](f'{hex(i)}.10000').get_raw(), (i << 3) + 1)

    def test_bin_parsing_edge_cases(self):
        self.assertEqual(self.parsers[0]('0b.1'    ).get_raw(), 1)
        self.assertEqual(self.parsers[0]('0b.100'  ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('0b.01'   ).get_raw(), 1)
        self.assertEqual(self.parsers[1]('0b.010'  ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('0b.001'  ).get_raw(), 1)
        self.assertEqual(self.parsers[2]('0b.00100').get_raw(), 1)
        self.assertEqual(self.parsers[3]('0b.0001' ).get_raw(), 1)
        self.assertEqual(self.parsers[3]('0b.00010').get_raw(), 1)

        for i in range(256):
            self.assertEqual(self.parsers[0](f'{bin(i)}.1'    ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[0](f'{bin(i)}.100'  ).get_raw(), (i << 0) + 1)
            self.assertEqual(self.parsers[1](f'{bin(i)}.01'   ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[1](f'{bin(i)}.010'  ).get_raw(), (i << 1) + 1)
            self.assertEqual(self.parsers[2](f'{bin(i)}.001'  ).get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[2](f'{bin(i)}.00100').get_raw(), (i << 2) + 1)
            self.assertEqual(self.parsers[3](f'{bin(i)}.0001' ).get_raw(), (i << 3) + 1)
            self.assertEqual(self.parsers[3](f'{bin(i)}.00010').get_raw(), (i << 3) + 1)

    def test_parsing_hex_integers(self):
        for q in range(len(self.parsers)):
            for i in range(-255, 256):
                self.assertEqual(self.parsers[q]('0x' + hex(i)).get_raw(), i << q)

    def test_parsing_hex_fractions(self):
        for q in range(4, 32):
            for d in range(1, 5):
                literal = f'0x.{1 << (4 - d)}'

                self.assertEqual(self.parsers[q](literal      ).get_raw(), 1 << (q - d))
                self.assertEqual(self.parsers[q](literal + '0').get_raw(), 1 << (q - d))

                for i in range(256):
                    literal = f'{hex(i)}.{1 << (4 - d)}'
                    correct = (i << q) + (1 << (q - d))

                    self.assertEqual(self.parsers[q](literal      ).get_raw(), correct)
                    self.assertEqual(self.parsers[q](literal + '0').get_raw(), correct)

    def test_parsing_bin_integers(self):
        for q in range(len(self.parsers)):
            for i in range(-255, 256):
                self.assertEqual(self.parsers[q]('0b' + bin(i)).get_raw(), i << q)

    def test_parsing_bin_fractions(self):
        for q in range(1, 32):
            self.assertEqual(self.parsers[q](f'0b.1' ).get_raw(), 1 << (q - 1))
            self.assertEqual(self.parsers[q](f'0b.10').get_raw(), 1 << (q - 1))

            for i in range(256):
                correct = (i << q) + (1 << (q - 1))

                self.assertEqual(self.parsers[q](f'{bin(i)}.1' ).get_raw(), correct)
                self.assertEqual(self.parsers[q](f'{bin(i)}.10').get_raw(), correct)
