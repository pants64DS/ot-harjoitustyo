import tkinter
from ui.settings_window import SettingsWindow
from ui.column_settings import ColumnSettings
from calculation.evaluator import Evaluator

class Column:
    def __init__(self, root, table, column_id):
        self._root = root
        self._table = table
        self._id = column_id
        self._settings_window = None
        self._settings = ColumnSettings(self._on_settings_changed)

        self._button = tkinter.Button(root, text=str(self._settings), \
            command=self._on_button_clicked)

        self._button.grid(row=0, column=column_id+1, padx=10, pady=5, sticky=tkinter.W)

    def get_evaluator(self):
        return Evaluator(self._settings.get_parser())

    def _on_settings_changed(self):
        self._button.config(text=str(self._settings))

        for row in self._table.get_rows():
            res = self.get_evaluator().evaluate_to_string(row.get_expr())

            row.set_result_at(self._id, res)

    def _on_button_clicked(self):
        if self._settings_window:
            self._settings_window.focus()
            return

        x = self._button.winfo_rootx() + self._button.winfo_width()
        y = self._button.winfo_rooty()

        self._settings_window = SettingsWindow(self._root, x, y, self._settings, \
            f'Sarakkeen {self._id} asetukset', self._on_settings_closed)

    def _on_settings_closed(self, event=None):
        if self._settings_window:
            self._settings_window.close()
            self._settings_window = None
