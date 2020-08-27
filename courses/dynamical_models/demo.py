import random

import matplotlib.pyplot as plt

from courses.dynamical_models.matrix import Matrix
from courses.dynamical_models.simulation import Simulation


def main():
    exercise_1()
    exercise_2()


def exercise_1():
    print('###### EXERCISE 1. ######')
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


def exercise_2():
    print('\n\n###### EXERCISE 2. ######')
    sensor_error = 0.3
    dt = 1.0
    simulation = Simulation(sensor_error, dt)
    timespan = 40
    simulation.run(timespan)
    # Visualize simulation results
    plt.plot(simulation.t, simulation.velocities)
    plt.show()
    # Call member functions
    print("Distance travelled:", simulation.distance_traveled(), 'm')
    print("Average velocity:", simulation.average_velocity(), 'm/s')
    print("Average acceleration:", simulation.average_acceleration(), 'm/s^2')


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
