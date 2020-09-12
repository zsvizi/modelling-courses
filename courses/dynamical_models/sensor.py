import numpy as np


class Sensor:
    def __init__(self, sensor_error, frequency):
        self.error = sensor_error
        self.f = frequency

        self.measured_v = None
        self.measured_t = None

    def run(self, timespan):
        # generates a list from 0.0 to timespan with (1/self.f) increment
        t = np.arange(0.0, timespan, 1/self.f)
        # ideal measurement (sensor cannot produce it due to its error)
        v_ideal = 0.01*(t-10)**2
        # sensor measurement = ideal + random error (for all time points)
        v_measured = v_ideal + np.random.normal(0, self.error, len(v_ideal))
        # save the measurement (velocities)
        self.measured_v = v_measured
        # save the time points of the measurement
        self.measured_t = t
