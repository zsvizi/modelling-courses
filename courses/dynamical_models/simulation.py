import numpy as np


class Simulation:
    def __init__(self, sensor_error, dt):
        self.car_max_speed = 15.0
        self.error = sensor_error
        self.dt = dt
        self.t = None
        self.velocities = None

    def run(self, time):
        t = np.arange(0, time, self.dt)
        v_ideal = np.minimum(0.01 * (t-10.0)**2, self.car_max_speed)
        v_meas = v_ideal + np.random.normal(0, self.error, v_ideal.shape)
        self.t = t
        self.velocities = v_meas

    def distance_traveled(self):
        return np.sum(self.velocities * self.dt)

    def average_velocity(self):
        return self.distance_traveled() / np.max(self.t)

    def average_acceleration(self):
        return np.sum((np.diff(self.velocities) / self.dt) * self.dt) / np.max(self.t)
