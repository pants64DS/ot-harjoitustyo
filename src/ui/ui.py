import tkinter
import numpy
from ui.table import Table

class UI:
    def __init__(self, root):
        self._root = root
        self._table = Table(root)

    def start(self):
        self._root.bind("<Control-n>", self._on_ctrl_n)

        numpy.seterr('ignore') # inf and nan are valid results

    def _on_ctrl_n(self, event):
        self._table.add_column()
