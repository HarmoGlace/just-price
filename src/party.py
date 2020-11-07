from random import randint


class Party:
    def __init__(self, min_number=1, max_number=1000):
        self.min = min_number
        self.max = max_number

        self.result = randint(self.min, self.max)
        self.tries = set()

    @property
    def finished(self):
        return self.result in self.tries

    @property
    def given_near(self):

        numbers = self.tries.copy()

        numbers.add(self.result)

        sorted_numbers = sorted(list(numbers))

        answer_index = sorted_numbers.index(self.result)
        nears = {'min': self.min, 'max': self.max}

        indexes = [answer_index - 1, answer_index + 1]

        if indexes[0] >= 0:
            nears['min'] = sorted_numbers[indexes[0]]

        if indexes[1] < len(sorted_numbers):
            nears['max'] = sorted_numbers[indexes[1]]

        return nears
