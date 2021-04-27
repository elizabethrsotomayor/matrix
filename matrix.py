from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        """Instantiate a Matrix object with given values separated by a newline."""
        self.matrix = [i.split() for i in matrix_string.splitlines()]
        self.nums = [[int(y) for y in x] for x in self.matrix]

    def row(self, index: int) -> List[int]:
        """Return the values in the row of a Matrix object from the index of a row."""
        return self.nums[index - 1]

    def column(self, index: int) -> List[int]:
        """Return the values in the column of a Matrix object from the index of a column."""
        return [x[index - 1] for x in self.nums]
