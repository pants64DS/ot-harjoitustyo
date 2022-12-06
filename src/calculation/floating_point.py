import numpy

def get_type(precision):
    if precision == 16:
        return numpy.float16

    if precision == 32:
        return numpy.float32

    if precision == 64:
        return numpy.float64

    return None

def get_precision(float_type):
    if float_type is numpy.float16:
        return 16

    if float_type is numpy.float32:
        return 32

    if float_type is numpy.float64:
        return 64

    return None
