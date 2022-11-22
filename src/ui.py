import tkinter
from row import Row

class UI:
	def __init__(self, root):
		self._root = root
		self._rows = []

	def start(self):
		first_row = Row(self._root, self._rows, 0)
		first_row.focus()
		self._rows.append(first_row)
