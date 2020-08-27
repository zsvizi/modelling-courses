import random

from courses.dynamical_models.matrix import Matrix


def main():
    exercise_1()


def exercise_1():
    row = 5
    column = 5

    print('--- Create Matrix object ---')
    matrix_list = generate_matrix(column, row)
    print("Matrix_list:", matrix_list)
    matrix = Matrix(matrix_list)
    print("Matrix object", matrix)

    print('\n--- Add two matrices ---')
    matrix_list_2 = generate_matrix(column, row)
    matrix_2 = Matrix(matrix_list_2)
    matrix_sum = matrix + matrix_2
    print('Matrix_1:', matrix)
    print('Matrix_2', matrix_2)
    print('Sum matrix:', matrix_sum)

    print('\n--- Transpose matrix ---')
    matrix_transpose = matrix.transpose()
    print('Transposed matrix:', matrix_transpose)


def generate_matrix(column, row):
    matrix_list = []
    for i in range(row):
        matrix_row = []
        for j in range(column):
            matrix_row.append(random.random())
        matrix_list.append(matrix_row)
    return matrix_list


if __name__ == '__main__':
    main()
