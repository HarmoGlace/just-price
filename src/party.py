from random import randint


class Party:
    def __init__(self, min=1, max=1000):
        self.min = min
        self.max = max

        self.result = randint(self.min, self.max)
        self.tries = set()

    @property
    def finished(self):
        return self.result in self.tries
