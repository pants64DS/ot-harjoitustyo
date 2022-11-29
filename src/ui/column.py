import tkinter
import numpy
from calculation.evaluator import Evaluator

_modes = {
    'float32': numpy.float32,
    'float64': numpy.float64,
}

class Column:
    def __init__(self, root, table, column_id):
        self._table = table
        self._id = column_id

        sorted_modes = sorted(list(_modes.keys()))

        self._mode = tkinter.StringVar(value=sorted_modes[0])
        self._mode.trace('w', self._on_mode_changed)

        self._mode_selector = tkinter.OptionMenu(root, self._mode, *sorted_modes)
        self._mode_selector.grid(row=0, column=column_id+1, padx=10, pady=5, sticky=tkinter.W)

    def get_evaluator(self):
        return Evaluator(_modes[self._mode.get()])

    def _on_mode_changed(self, name, index, mode):
        for row in self._table.get_rows():
            res = self.get_evaluator().evaluate_to_string(row.get_expr())

            row.set_result_at(self._id, res)
