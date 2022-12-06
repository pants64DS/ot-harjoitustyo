import tkinter
from tkinter import ttk
import numpy
from calculation.evaluator import Evaluator

class SettingsWindow:
    def __init__(self, root, on_closed, x, y):
        self._window = tkinter.Toplevel(root)

        self._window.geometry(f'300x400+{x}+{y}')
        self._window.title('Sarakkeen asetukset')
        self._window.protocol('WM_DELETE_WINDOW', on_closed)
        self._window.bind('<Escape>', on_closed)
        self._window.focus()

        self._repr = tkinter.StringVar(value='floating-point')
        self._repr.trace('w', self._on_repr_changed)
        self._init_repr_select()

    def _init_repr_select(self):
        mode_label = tkinter.Label(master=self._window, text='Sisäinen esitysmuoto')
        mode_label.grid(row=0, column=0, rowspan=2, padx=10)

        float_button = tkinter.Radiobutton(self._window, text='Liukuluvut', \
            variable=self._repr, value='floating-point')

        fixed_button = tkinter.Radiobutton(self._window, text='Kiintoluvut', \
            variable=self._repr, value='fixed-point')

        float_button.grid(row=0, column=1, padx=50, pady=(10, 0), sticky=tkinter.E)
        fixed_button.grid(row=1, column=1, padx=50, pady=(0, 10), sticky=tkinter.E)

        separator = ttk.Separator(self._window, orient='horizontal')
        separator.grid(row=2, columnspan=2, sticky='EW')

    def focus(self):
        self._window.focus()

    def close(self):
        self._window.destroy()

    def _on_repr_changed(self, name, index, mode):
        pass
