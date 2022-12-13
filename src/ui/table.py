import tkinter
from ui.row import Row
from ui.column import Column

class Table:
    """A class that handles a table whose rows correspond to expressions
    provided by the user, columns correspond to different evaluation settings
    and cells contain different results."""
    def __init__(self, root):
        self._root = root
        self._columns = [Column(root, self, 0)]
        self._rows = [Row(root, self, 0)]

        self._rows[0].focus()

    def add_row(self, row_id):
        """Adds a row to the table.

        Args:
            row_id: The number of rows above the new row after insertion.
        """
        new_row = Row(self._root, self, row_id)
        new_row.focus()
        self._rows.insert(row_id, new_row)

        for i in range(row_id + 1, len(self._rows)):
            self._rows[i].set_id(i)

    def get_row(self, row_id, wrap_around):
        """Gets a row with the given ID.

        Args:
            row_id: The number of rows above the row to get
            wrap_around: If True, row_id wraps to the other end of the table
                when it goes out of range. Otherwise, if row_id goes out of
                range gets it gets clamped.

        Returns:
            A row with the given ID.
        """
        if wrap_around:
            row_id %= len(self._rows)
        else:
            row_id = max(row_id, 0)
            row_id = min(row_id, len(self._rows) - 1)

        return self._rows[row_id]

    def get_width(self):
        """Gets the number of columns in the table
        
        Returns:
            The number of columns in the table.
        """
        return len(self._columns)

    def get_height(self):
        """Gets the number of rows in the table.

        Returns:
            The number of rows in the table.
        """
        return len(self._rows)

    def get_rows(self):
        """Gets a list of rows in the table.

        Returns:
            A list of rows in the table.
        """
        return self._rows

    def get_columns(self):
        """Gets a list of columns in the table.

        Returns:
            A list of columns in the table.
        """
        return self._columns

    def add_column(self):
        """Adds a new column with default settings to the table.
        """

        new_column_id = len(self._columns)
        new_column = Column(self._root, self, new_column_id)

        self._columns.append(new_column)

        for row in self._rows:
            res = new_column.get_evaluator().evaluate_to_string(row.get_expr())

            row.add_label(self._root, new_column_id)
            row.set_result_at(new_column_id, res)
