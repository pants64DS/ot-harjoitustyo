import tkinter
from tkinter import ttk
from ui.floating_point_settings import FloatingPointSettings
import numpy

class SettingsWindow:
    def __init__(self, root, pos_x, pos_y, scalar_type, title, on_closed, on_scalar_type_changed):
        self._window = tkinter.Toplevel(root)

        self._window.geometry(f'300x200+{pos_x}+{pos_y}')
        self._window.title(title)
        self._window.protocol('WM_DELETE_WINDOW', on_closed)
        self._window.bind('<Escape>', on_closed)
        self._window.columnconfigure((0, 1), weight=1)
        self._window.focus()

        uses_floats = numpy.issubdtype(scalar_type, numpy.floating)
        self._uses_floats = tkinter.BooleanVar(value=uses_floats)
        self._uses_floats.trace('w', self._on_uses_floats_changed)
        self._init_repr_select()

        if uses_floats:
            self._curr_view = FloatingPointSettings(self._window, scalar_type, on_scalar_type_changed)
        else:
            pass # TODO: self._curr_view = FixedPointSettings(...)

    def _init_repr_select(self):
        mode_label = tkinter.Label(master=self._window, text='Sisäinen esitysmuoto')
        mode_label.grid(row=0, column=0, rowspan=2, padx=(20, 50), sticky=tkinter.W)

        float_button = tkinter.Radiobutton(self._window, text='Liukuluvut', \
            variable=self._uses_floats, value=True)

        fixed_button = tkinter.Radiobutton(self._window, text='Kiintoluvut', \
            variable=self._uses_floats, value=False, state=tkinter.DISABLED)

        float_button.grid(row=0, column=1, padx=(0, 20), pady=(10, 0), sticky=tkinter.W)
        fixed_button.grid(row=1, column=1, padx=(0, 20), pady=(0, 10), sticky=tkinter.W)

        separator = ttk.Separator(self._window, orient='horizontal')
        separator.grid(row=2, columnspan=2, sticky='EW')

    def focus(self):
        self._window.focus()

    def close(self):
        self._window.destroy()

    def _on_uses_floats_changed(self, name, index, mode):
        pass
