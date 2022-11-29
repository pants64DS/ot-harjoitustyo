import tkinter

class Row:
	def __init__(self, root, table, row_id):
		self._table = table

		self._expr = tkinter.StringVar()
		self._expr.trace('w', self._on_expr_changed)
		self._init_expr_field(root)

		self._result_labels = []
		self._id = row_id

		for column_id in range(table.get_width()):
			self.add_label(root, column_id)

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

	def add_label(self, root, column_id):
		new_label = tkinter.Label(master=root, font=('Consolas', 15))
		new_label.grid(row=self._id+1, column=column_id+1, padx=10, pady=5, sticky=tkinter.W)

		self._result_labels.append(new_label)

	def get_expr(self):
		return self._expr.get()

	def set_result_at(self, column_id, res):
		self._result_labels[column_id]['text'] = res

	def set_id(self, new_id):
		self._id = new_id
		self._expr_field.grid(row=new_id+1)

		for label in self._result_labels:
			label.grid(row=new_id+1)

	def focus(self):
		self._expr_field.focus()

	def move_focus(self, offset, relative=True, wrap_around=False):
		new_id = offset

		if relative:
			new_id += self._id

		new_row = self._table.get_row(new_id, wrap_around)
		cursor_pos = self._expr_field.index(tkinter.INSERT)

		if cursor_pos == len(self.get_expr()):
			cursor_pos = 'end'

		new_row._expr_field.icursor(cursor_pos)
		new_row.focus()

	# Sets the result label
	def _on_expr_changed(self, name, index, mode):
		expr = self.get_expr()

		for column, label in zip(self._table.get_columns(), self._result_labels):
			label['text'] = column.get_evaluator().evaluate_to_string(expr)

	def _on_enter(self, event):
		self._table.add_row(self._id + 1) # Adds a row below this one

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
