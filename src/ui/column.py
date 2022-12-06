import tkinter
import numpy
from calculation.evaluator import Evaluator
from ui.settings_window import SettingsWindow

_modes = {
    'float32': numpy.float32,
    'float64': numpy.float64,
}

class Column:
    def __init__(self, root, table, column_id):
        self._root = root
        self._table = table
        self._id = column_id
        self._settings_window = None

        sorted_modes = sorted(list(_modes.keys()))

        self._mode = tkinter.StringVar(value=sorted_modes[0])
        self._mode.trace('w', self._on_mode_changed)

        self._button = tkinter.Button(root, text='asetukset...', command=self._on_button_clicked)
        self._button.grid(row=0, column=column_id+1, padx=10, pady=5, sticky=tkinter.W)

    def get_evaluator(self):
        return Evaluator(_modes[self._mode.get()])

    def _on_mode_changed(self, name, index, mode):
        for row in self._table.get_rows():
            res = self.get_evaluator().evaluate_to_string(row.get_expr())

            row.set_result_at(self._id, res)

    def _on_button_clicked(self):
        if self._settings_window:
            self._settings_window.focus()
            return

        x = self._button.winfo_rootx() + self._button.winfo_width()
        y = self._button.winfo_rooty()

        self._settings_window = SettingsWindow(self._root, self._on_settings_closed, x, y)

    def _on_settings_closed(self, event=None):
        if self._settings_window:
            self._settings_window.close()
            self._settings_window = None
