import tkinter
import calculation.fixed_point as fixed_point

_max_frac_bits = 65536

def _validate_bit_select(new_value):
    if not new_value:
        return True

    try:
        num_frac_bits = int(new_value)
    except ValueError:
        return False

    return 0 <= num_frac_bits <= _max_frac_bits

class FixedPointSettingsView:
    def __init__(self, root, column_settings):
        self._column_settings = column_settings

        self._width_label = tkinter.Label(master=root, text='Murto-osan koko bitteinä')
        self._width_label.grid(row=3, column=0, padx=(20, 0), pady=(10, 0), sticky=tkinter.W)

        self._num_frac_bits = tkinter.StringVar(value=column_settings.get_num_frac_bits())
        self._num_frac_bits.trace('w', self._on_num_frac_bits_changed)

        validator = (root.register(_validate_bit_select), '%P')
        self._bit_selector = tkinter.ttk.Spinbox(master=root, width=5, from_=0, to=_max_frac_bits, \
            textvariable=self._num_frac_bits, validate='all', validatecommand=validator)

        self._bit_selector.grid(row=3, column=1, padx=(0, 50), pady=(10, 0), sticky=tkinter.E)

    def destroy(self):
        self._width_label.destroy()
        self._bit_selector.destroy()

    def _on_num_frac_bits_changed(self, name, index, mode):
        try:
            num_frac_bits = int(self._num_frac_bits.get())
        except ValueError:
            return

        self._column_settings.enable_fixed_mode(num_frac_bits)
