import tkinter
from calculation.evaluator import Evaluator

class Row:
	def __init__(self, root, parent_table, row_id):
		self._root = root # needed for creating more rows
		self._parent_table = parent_table

		self._expr = tkinter.StringVar()
		self._expr.trace('w', self._on_expr_changed)
		self._init_expr_field(root)

		self._result_label = tkinter.Label(master=root, font=('Consolas', 15))
		self._result_label.grid(column=1, padx=10, pady=5, sticky=tkinter.W)

		self.set_id(row_id)

	def _init_expr_field(self, root):
		self._expr_field = tkinter.Entry(master=root, \
			width=30, font=('Consolas', 15), textvariable=self._expr)

		self._expr_field.grid(column=0, padx=10, pady=5)

		self._expr_field.bind('<Return>',       self._on_enter)
		self._expr_field.bind('<FocusOut>',     self._on_focus_out)
		self._expr_field.bind('<Tab>',          self._on_tab)
		self._expr_field.bind('<Shift-Tab>',    self._on_shift_tab)
		self._expr_field.bind('<Up>',           self._on_up)
		self._expr_field.bind('<Down>',         self._on_down)
		self._expr_field.bind('<Control-Home>', self._on_ctrl_home)
		self._expr_field.bind('<Control-End>',  self._on_ctrl_end)

	def set_id(self, new_id):
		self._id = new_id
		self._expr_field.grid(row=new_id)
		self._result_label.grid(row=new_id)

	def focus(self):
		self._expr_field.focus()

	def move_focus(self, offset, relative=True, wrap_around=False):
		new_id = offset

		if relative:
			new_id += self._id

		if wrap_around:
			new_id %= len(self._parent_table)
		else:
			new_id = max(new_id, 0)
			new_id = min(new_id, len(self._parent_table) - 1)

		new_row = self._parent_table[new_id]
		cursor_pos = self._expr_field.index(tkinter.INSERT)

		if cursor_pos == len(self._expr.get()):
			cursor_pos = 'end'

		new_row._expr_field.icursor(cursor_pos)
		new_row.focus()

	# Sets the result label
	def _on_expr_changed(self, name, index, mode):
		expr = self._expr.get()

		if not expr:
			self._result_label['text'] = ''
			return

		try:
			res = str(Evaluator(float).evaluate(expr))
		except ZeroDivisionError:
			res = 'Undefined'
		except:
			res = 'Invalid'

		if res.endswith('.0'):
			res = res[:-2]

		self._result_label['text'] = res

	# Adds a row
	def _on_enter(self, event):
		new_id = self._id + 1
		new_row = Row(self._root, self._parent_table, new_id)
		new_row.focus()

		self._parent_table.insert(new_id, new_row)

		for i in range(new_id + 1, len(self._parent_table)):
			self._parent_table[i].set_id(i)

	def _on_focus_out(self, event):
		self._expr_field.select_range(0, 0)

	def _on_tab(self, event):
		self.move_focus(1, wrap_around=True)

		return 'break'

	def _on_shift_tab(self, event):
		self.move_focus(-1, wrap_around=True)

		return 'break'

	def _on_up(self, event):
		self.move_focus(-1)

	def _on_down(self, event):
		self.move_focus(1)

	def _on_ctrl_home(self, event):
		self.move_focus(0, relative=False)

	def _on_ctrl_end(self, event):
		self.move_focus(-1, relative=False, wrap_around=True)
