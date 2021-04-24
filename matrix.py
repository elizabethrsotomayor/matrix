from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        """ Instantiates a Matrix object with given values separated by a newline """
        self.matrix_string = matrix_string
        self.split_list = self.matrix_string.split('\n')
        self.matrix_list = []
        # loop through rows in matrix list
        for item in self.split_list:
            # each item is converted to a list of ints and appended to self.matrix_list
            num_list = list(map(int, item.split()))
            self.matrix_list.append(num_list)

    def row(self, index: int) -> List[int]:
        """ Takes in the index of a row in a Matrix object and returns the values in the row """
        row = self.matrix_list[index - 1]
        return row

    def column(self, index: int) -> List[int]:
        """ Takes in the index of a column in a Matrix object and returns the values in the column """
        column = []
        for item in self.matrix_list:
            column.append(item[index-1])
        return column
