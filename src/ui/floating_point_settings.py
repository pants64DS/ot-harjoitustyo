import tkinter
import numpy

def _get_float_type(precision):
    if precision == 16:
        return numpy.float16

    if precision == 32:
        return numpy.float32

    if precision == 64:
        return numpy.float64

    return None

def _get_float_precision(float_type):
    if float_type is numpy.float16:
        return 16

    if float_type is numpy.float32:
        return 32

    if float_type is numpy.float64:
        return 64

    return None

class FloatingPointSettings:
    def __init__(self, root, curr_type, on_scalar_type_changed):
        self._root = root
        self._precision = tkinter.IntVar(value=_get_float_precision(curr_type))
        self._precision.trace('w', self._on_precision_changed)
        self._on_scalar_type_changed = on_scalar_type_changed

        width_label = tkinter.Label(master=root, text='Tarkkuus bitteinä')
        width_label.grid(row=3, column=0, rowspan=3, padx=(20, 50), sticky=tkinter.W)

        _16_bit_button = tkinter.Radiobutton(root, text='16', \
            variable=self._precision, value=16)

        _32_bit_button = tkinter.Radiobutton(root, text='32', \
            variable=self._precision, value=32)

        _64_bit_button = tkinter.Radiobutton(root, text='64', \
            variable=self._precision, value=64)

        _16_bit_button.grid(row=3, column=1, padx=(0, 20), pady=(10, 0), sticky=tkinter.W)
        _32_bit_button.grid(row=4, column=1, padx=(0, 20), pady=(0,  0), sticky=tkinter.W)
        _64_bit_button.grid(row=5, column=1, padx=(0, 20), pady=(0, 10), sticky=tkinter.W)

    def _on_precision_changed(self, name, index, mode):
        self._on_scalar_type_changed(_get_float_type(self._precision.get()))
