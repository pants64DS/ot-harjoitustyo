import tkinter
import numpy
from ui.settings_window import SettingsWindow
from calculation.evaluator import Evaluator
import calculation.floating_point as floating_point

def _get_display_name(scalar_type):
    if numpy.issubdtype(scalar_type, numpy.floating):
        return f'float{floating_point.get_precision(scalar_type)}'

    return ''

class Column:
    def __init__(self, root, table, column_id):
        self._root = root
        self._table = table
        self._id = column_id
        self._settings_window = None
        self._scalar_type = numpy.float32

        self._button = tkinter.Button(root, text=_get_display_name(self._scalar_type), \
            command=self._on_button_clicked)

        self._button.grid(row=0, column=column_id+1, padx=10, pady=5, sticky=tkinter.W)

    def get_evaluator(self):
        return Evaluator(self._scalar_type)

    def _on_scalar_type_changed(self, new_type):
        self._scalar_type = new_type
        self._button.config(text=_get_display_name(new_type))

        for row in self._table.get_rows():
            res = self.get_evaluator().evaluate_to_string(row.get_expr())

            row.set_result_at(self._id, res)

    def _on_button_clicked(self):
        if self._settings_window:
            self._settings_window.focus()
            return

        x = self._button.winfo_rootx() + self._button.winfo_width()
        y = self._button.winfo_rooty()

        self._settings_window = SettingsWindow(self._root, x, y, self._scalar_type, \
            f'Sarakkeen {self._id} asetukset', self._on_settings_closed, \
            self._on_scalar_type_changed, )

    def _on_settings_closed(self, event=None):
        if self._settings_window:
            self._settings_window.close()
            self._settings_window = None
