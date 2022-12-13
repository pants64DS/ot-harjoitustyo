import tkinter
import calculation.fixed_point as fixed_point

class FixedPointSettings:
    def __init__(self, root, column_settings):
        self._root = root
        self._column_settings = column_settings
        self._width_label = tkinter.Label(master=root, text='Kokonaisosan koko bitteinä:')
        self._width_label.grid(row=3, column=0, rowspan=3, padx=(20, 0), sticky=tkinter.W)

    def destroy(self):
        self._width_label.destroy()
