import tkinter

class FloatingPointSettings:
    def __init__(self, root, column_settings):
        self._root = root
        self._column_settings = column_settings
        self._precision = tkinter.IntVar(value=column_settings.get_float_precision())
        self._precision.trace('w', self._on_precision_changed)

        self._width_label = tkinter.Label(master=root, text='Tarkkuus bitteinä')
        self._width_label.grid(row=3, column=0, rowspan=3, padx=(20, 50), sticky=tkinter.W)

        self._16_bit_button = tkinter.Radiobutton(root, text='16', \
            variable=self._precision, value=16)

        self._32_bit_button = tkinter.Radiobutton(root, text='32', \
            variable=self._precision, value=32)

        self._64_bit_button = tkinter.Radiobutton(root, text='64', \
            variable=self._precision, value=64)

        self._16_bit_button.grid(row=3, column=1, padx=(0, 20), pady=(10, 0), sticky=tkinter.W)
        self._32_bit_button.grid(row=4, column=1, padx=(0, 20), pady=(0,  0), sticky=tkinter.W)
        self._64_bit_button.grid(row=5, column=1, padx=(0, 20), pady=(0, 10), sticky=tkinter.W)

    def destroy(self):
        self._width_label.destroy()
        self._16_bit_button.destroy()
        self._32_bit_button.destroy()
        self._64_bit_button.destroy()

    def _on_precision_changed(self, name, index, mode):
        self._column_settings.enable_float_mode(self._precision.get())
