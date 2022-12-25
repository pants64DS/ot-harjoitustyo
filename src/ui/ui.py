import tkinter
import numpy
from ui.table import Table

class UI:
    """A class that manages the UI of the whole app."""

    def __init__(self):
        """The constructor of the UI class."""

        self._root = tkinter.Tk()
        self._canvas = tkinter.Canvas(self._root)
        self._vertScrollbar = tkinter.Scrollbar(self._root, orient='vertical', command=self._canvas.yview)
        self._horzScrollbar = tkinter.Scrollbar(self._root, orient='horizontal', command=self._canvas.xview)
        self._table_frame = tkinter.ttk.Frame(self._canvas)
        self._table = Table(self._table_frame)

    def start(self):
        """Stars the UI."""

        self._root.bind("<Control-n>", self._on_ctrl_n)
        self._root.title("Ohjelmoijan laskin")
        self._root.geometry("600x300")

        self._table_frame.bind("<Configure>", \
            lambda e: self._canvas.configure(scrollregion=self._canvas.bbox("all")))

        self._canvas.create_window((0, 0), window=self._table_frame, anchor="nw")
        self._canvas.configure(xscrollcommand=self._horzScrollbar.set, yscrollcommand=self._vertScrollbar.set)

        self._vertScrollbar.pack(side=tkinter.RIGHT,  fill=tkinter.Y)
        self._horzScrollbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self._canvas.pack(side="left", fill="both", expand=True)

        numpy.seterr('ignore') # inf and nan are valid results
        self._root.mainloop()

    def _on_ctrl_n(self, event):
        self._table.add_column()
