class Matrix:
    def __init__(self, data):
        self.elements = data
        self.n_rows = len(data)
        self.n_columns = len(data[0])

    def add(self, other_matrix):
        result = []

        for row in range(self.n_rows):
            new_row = []

            for col in range(self.n_columns):
                result_sum = self.elements[row][col] + other_matrix.elements[row][col]
                new_row.append(result_sum)

            result.append(new_row)

        return result
