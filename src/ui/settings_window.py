import tkinter
from tkinter import ttk
from ui.fixed_point_settings import FixedPointSettings
from ui.floating_point_settings import FloatingPointSettings
import numpy

class SettingsWindow:
    def __init__(self, root, pos_x, pos_y, column_settings, title, on_closed):
        self._window = tkinter.Toplevel(root)

        self._window.geometry(f'400x200+{pos_x}+{pos_y}')
        self._window.title(title)
        self._window.protocol('WM_DELETE_WINDOW', on_closed)
        self._window.bind('<Escape>', on_closed)
        self._window.columnconfigure((0, 1), weight=1)
        self._window.focus()

        self._column_settings = column_settings
        self._mode = tkinter.BooleanVar(value=column_settings.uses_floats())
        self._mode.trace('w', self._on_mode_changed)
        self._init_repr_select()

        if column_settings.uses_floats():
            self._curr_view = FloatingPointSettings(self._window, column_settings)
        else:
            self._curr_view = FixedPointSettings(self._window, column_settings)

    def _init_repr_select(self):
        mode_label = tkinter.Label(master=self._window, text='Sisäinen esitysmuoto')
        mode_label.grid(row=0, column=0, rowspan=2, padx=(20, 50), sticky=tkinter.W)

        float_button = tkinter.Radiobutton(self._window, text='Liukuluvut', \
            variable=self._mode, value=True)

        fixed_button = tkinter.Radiobutton(self._window, text='Kiintoluvut', \
            variable=self._mode, value=False)

        float_button.grid(row=0, column=1, padx=(0, 20), pady=(10, 0), sticky=tkinter.W)
        fixed_button.grid(row=1, column=1, padx=(0, 20), pady=(0, 10), sticky=tkinter.W)

        separator = ttk.Separator(self._window, orient='horizontal')
        separator.grid(row=2, columnspan=2, sticky='EW')

    def focus(self):
        self._window.focus()

    def close(self):
        self._window.destroy()

    def _on_mode_changed(self, name, index, mode):
        self._curr_view.destroy()

        if isinstance(self._curr_view, FloatingPointSettings):
            self._column_settings.enable_fixed_mode()
            self._curr_view = FixedPointSettings(self._window, self._column_settings)
        else:
            self._column_settings.enable_float_mode()
            self._curr_view = FloatingPointSettings(self._window, self._column_settings)
