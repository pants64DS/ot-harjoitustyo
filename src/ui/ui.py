import tkinter
import numpy
from ui.table import Table

class UI:
    """A class that manages the UI of the whole app."""

    def __init__(self, root):
        """The constructor of the UI class.

        Args:
            root: A window to contain the UI
        """

        self._root = root
        self._table = Table(root)

    def start(self):
        """Stars the UI."""
        self._root.bind("<Control-n>", self._on_ctrl_n)

        numpy.seterr('ignore') # inf and nan are valid results

    def _on_ctrl_n(self, event):
        self._table.add_column()
