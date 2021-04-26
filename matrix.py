from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        """Instantiate a Matrix object with given values separated by a newline."""
        self.split_matrix = matrix_string.splitlines()
        self.nums_list = [list(map(int, item.split())) for item in self.split_matrix]

    def row(self, index: int) -> List[int]:
        """Return the values in the row of a Matrix object from the index of a row."""
        row = self.nums_list[index - 1]
        return row

    def column(self, index: int) -> List[int]:
        """Return the values in the column of a Matrix object from the index of a column."""
        column = [x[index - 1] for x in self.nums_list]
        return column
