import matplotlib.pyplot as plt


def main():
    exercise_1()
    exercise_2()


def exercise_1():
    print('###### EXERCISE 1. ######')

    print('--- Create Circle object with r=3 ---')
    pass
    print("Diameter:", None)
    print("Circumference:", None)
    print("Area:", None)

    print('\n--- Create CircleCoord object with center=(0,0), r=2 ---')
    pass
    print('Diameter:', None)
    print('Area:', None)
    print('Contains (2,0)?', None)
    print('Contains (1,0)?', None)
    print('Contains (3,0)?', None)

    print('\n--- Create CircleCoord object with center=(2,2), r=1 ---')
    pass
    print('Intersects CircleCoord with center=(2,2), r=1?', None)

    print('\n--- Create CircleCoord object with center=(3,3), r=1 ---')
    pass
    print('Intersects CircleCoord with center=(3,3), r=1?', None)


def exercise_2():
    print('\n\n###### EXERCISE 2. ######')
    # Create Sensor object with sensor_error=0.3 and dt=1.0
    sensor_error = 0.3
    dt = 1.0
    pass

    # Run measurement for timespan=40
    timespan = 40
    pass

    # Visualize simulation results
    t = [1, 2, 3]
    velocities = [0, 0, 0]
    plt.plot(t, velocities)
    plt.show()

    # Calculate the following quantities
    print("Distance travelled:", None, 'm')
    print("Average velocity:", None, 'm/s')
    print("Average acceleration:", None, 'm/s^2')


if __name__ == '__main__':
    main()
