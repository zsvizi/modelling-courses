import matplotlib.pyplot as plt

from courses.dynamical_models.circles import Circle, CircleCoord
from courses.dynamical_models.simulation import Simulation


def main():
    exercise_1()
    exercise_2()


def exercise_1():
    print('###### EXERCISE 1. ######')

    print('--- Create Circle object with r=3 ---')
    circle = Circle(3)
    print("Diameter:", circle.diameter())
    print("Circumference:", circle.circumference())
    print("Area:", circle.area())

    print('\n--- Create CircleCoord object with center=(0,0), r=2 ---')
    circle_coord = CircleCoord((0, 0), 2)
    print('Diameter:', circle_coord.diameter())
    print('Area:', circle_coord.area())
    print('Contains (2,0)?', circle_coord.contains((2, 0)))
    print('Contains (1,0)?', circle_coord.contains((1, 0)))
    print('Contains (3,0)?', circle_coord.contains((3, 0)))

    print('\n--- Create CircleCoord object with center=(2,2), r=1 ---')
    other_circlecoord = CircleCoord((2, 2), 1)
    print('Intersects CircleCoord with center=(2,2), r=1?', circle_coord.intersects(other_circlecoord))

    print('\n--- Create CircleCoord object with center=(3,3), r=1 ---')
    other_circlecoord_2 = CircleCoord((3, 3), 1)
    print('Intersects CircleCoord with center=(3,3), r=1?', circle_coord.intersects(other_circlecoord_2))


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


if __name__ == '__main__':
    main()
