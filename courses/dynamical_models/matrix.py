import copy


class Matrix:
    def __init__(self, data):
        is_rectangular = check_format(data)
        if is_rectangular:
            self.data = data
            self.rows = len(data)
            self.columns = len(data[0])
        else:
            raise Exception('The input data is not a rectangular table!')

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = []
            for (row1, row2) in zip(self.data, other.data):
                result_row = []
                for (element1, element2) in zip(row1, row2):
                    result_row.append(element1 + element2)
                result.append(result_row)
            return Matrix(result)
        else:
            raise Exception('The matrices are not compatible!')

    def transpose(self):
        result = copy.deepcopy(self.data)
        for i in range(self.rows):
            for j in range(self.columns):
                result[j][i] = self.data[i][j]
        return Matrix(result)


def check_format(data):
    is_valid = isinstance(data, list)  # check whether the input is a list
    if is_valid:
        if isinstance(data[0], list):  # check whether the first element of the input list is also a list
            first_row_size = len(data[0])
            for row in data:
                # check whether all elements of the input list is also a list AND
                # check whether all list have the same size in the input list
                if not isinstance(row, list) or len(row) != first_row_size:
                    is_valid = False
                    break  # break once is_valid is set to False and go to return
        else:
            is_valid = False
    return is_valid
