import matplotlib.pyplot as plt


class Simulation:
    def __init__(self):
        self.width = 10
        self.height = 10

        self.actual_state = self.init_first_state()

    def init_first_state(self):
        init_state = []
        for x in range(self.height):
            row = []
            for y in range(self.width):
                row.append(0.1)
            init_state.append(row)
        return init_state

    def run(self, time):
        pass

    def statistics(self):
        harvest_amount = None
        maximal_harvest = None
        return harvest_amount, maximal_harvest


if __name__ == '__main__':
    # Create Simulation instance
    sim = Simulation()

    # Run simulation
    sim.run(100)
    plt.imshow(sim.actual_state, cmap='Blues')
    plt.colorbar()
    plt.show()

    # Print statistics
    amount, max_harv = sim.statistics()
    print('Number of harvests:', amount)
    print('Maximal harvest:', max_harv)
