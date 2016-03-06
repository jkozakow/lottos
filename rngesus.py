import numpy as np


class Lotto:

    def __init__(self):
        self.balls = np.arange(1, 50)
        self.probabilities = np.array([])
        self.prd_probabilities = np.array([])
        self.pool = []
        for i in range(1, 50):
            self.probabilities = np.append(self.probabilities, [1/49])
            self.prd_probabilities = np.append(self.prd_probabilities, [1/49])

    def mix(self):
        self.pool = np.random.choice(self.balls, 6, p=self.probabilities, replace=False)
        print(self.pool)
        return self.pool

    def randomizeTotalPrize(self):
        pot = np.random.randint(5000000, 20000000, 1)
        return pot

    def checkWin(self, numbers):
        win = 0
        tocheck = np.asarray(numbers)
        for element in self.pool:
            if element in tocheck:
                win += 1

        return win

    def calculatePrize(self, match, pot):
        if match >= 3:
            if match == 3:
                prize = 24
            elif match == 4:
                prize = pot/2000
            elif match == 5:
                prize = pot/500
            else:
                prize = pot
        else:
            prize = 0
        return prize

    def PRDmix(self):
        pass
