import tkinter
from evaluator import Evaluator

class Row:
	def set_result(self, name, index, mode):
		expr = self._expr.get()

		if not expr:
			self._result_label['text'] = ''
			return

		try:
			res = Evaluator(float).evaluate(expr)
		except Exception as e:
			self._result_label['text'] = e
		else:
			self._result_label['text'] = res

	def add_row(self, event):
		self._ui.add_row(self._id + 1)

	def lift(self):
		self._expr_field.lift()

	def set_id(self, new_id):
		self._id = new_id
		self._expr_field.grid(row=new_id)
		self._result_label.grid(row=new_id)

	def focus(self):
		self._expr_field.focus()

	def __init__(self, ui, row_id):
		self._ui = ui

		self._expr = tkinter.StringVar()
		self._expr.trace('w', self.set_result)

		self._expr_field = tkinter.Entry(master=ui._root, \
			width=30, font=('Consolas', 15), textvariable=self._expr)

		self._expr_field.grid(column=0, padx=10, pady=5)
		self._expr_field.bind('<Return>', self.add_row)

		self._result_label = tkinter.Label(master=ui._root, \
			font=('Consolas', 15))

		self._result_label.grid(column=1, padx=10, pady=5, sticky=tkinter.W)

		self.set_id(row_id)
		self.focus()

class UI:
	def __init__(self, root):
		self._root = root
		self._rows = []

	def add_row(self, row_id):
		self._rows.insert(row_id, Row(self, row_id))

		for i in range(row_id + 1, len(self._rows)):
			self._rows[i].set_id(i)
			self._rows[i].lift()

	def start(self):
		first_row = Row(self, 0)
		first_row.focus()
		self._rows.append(first_row)
