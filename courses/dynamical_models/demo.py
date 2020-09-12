import matplotlib.pyplot as plt

from courses.dynamical_models.circle import Circle, CircleCoord
from courses.dynamical_models.matrix import Matrix
from courses.dynamical_models.sensor import Sensor


def main():
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()


def exercise_1():
    print('###### EXERCISE 1. ######')
    print('--- Create Circle object with r=3 ---')
    circle = Circle(radius=3)
    print("Diameter:", circle.diameter())
    print("Circumference:", circle.circumference())
    print("Area:", circle.area())


def exercise_2():
    print('\n\n###### EXERCISE 2. ######')
    print('\n--- Create CircleCoord object with center=(0,0), r=2 ---')
    circle_coord = CircleCoord(radius=2, center_x=0, center_y=0)
    print('Diameter:', circle_coord.diameter())
    print('Area:', circle_coord.area())
    print('Contains (2,0)?', circle_coord.contains(point=[2, 0]))
    print('Contains (1,0)?', circle_coord.contains(point=[1, 0]))
    print('Contains (3,0)?', circle_coord.contains(point=[3, 0]))

    print('\n--- Create CircleCoord object with center=(2,2), r=1 ---')
    circle_coord_2 = CircleCoord(radius=1, center_x=2, center_y=2)
    print('Intersects CircleCoord with center=(2,2), r=1?', circle_coord.overlaps(other_circle=circle_coord_2))

    print('\n--- Create CircleCoord object with center=(3,3), r=1 ---')
    circle_coord_3 = CircleCoord(radius=1, center_x=3, center_y=3)
    print('Intersects CircleCoord with center=(3,3), r=1?', circle_coord.overlaps(other_circle=circle_coord_3))


def exercise_3():
    print('\n\n###### EXERCISE 3. ######')
    print('\n--- Create Matrix "a" from [[1,2,3],[4,5,6]] ---')
    a = [[1, 2, 3], [4, 5, 6]]
    matrix_a = Matrix(data=a)
    print('\n--- Create Matrix "b" from [[0,-1,2],[-1,-3,-9]] ---')
    b = [[0, -1, 2], [-1, -3, 9]]
    matrix_b = Matrix(data=b)
    print('\n--- Add Matrix "b" to Matrix "a" ---')
    result = matrix_a.add(other_matrix=matrix_b)
    print('Sum of Matrix "a" and Matrix "b":', result)


def exercise_4():
    print('\n\n###### EXERCISE 4. ######')
    # Create Sensor object with sensor_error=0.3 and dt=1.0
    sensor_error = 0.3
    f = 1.0
    sensor = Sensor(sensor_error=sensor_error, frequency=f)
    # print(sensor.f)

    # Run measurement for timespan=40
    timespan = 40
    sensor.run(timespan=timespan)

    # Visualize simulation results
    plt.plot(sensor.measured_t, sensor.measured_v)
    plt.show()

    # Calculate the following quantities
    print("Distance travelled:", None, 'm')
    print("Average velocity:", None, 'm/s')
    print("Average acceleration:", None, 'm/s^2')


if __name__ == '__main__':
    main()
