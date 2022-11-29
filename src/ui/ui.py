import tkinter
import numpy
from ui.table import Table

class UI:
	def __init__(self, root):
		self._root = root
		self._table = Table(root)

	def start(self):
		numpy.seterr('ignore') # inf and nan are valid results
