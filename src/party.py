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

        nears = []

        sorted_numbers = sorted(list(filter(lambda given: given != self.result, self.tries)))
        for number in self.tries:
            number_index = sorted_numbers.index(number)
            if number_index > len(self.tries) - 1: break
            if number < self.result < sorted_numbers[number_index + 1]:
                nears.append(number)
                nears.append(sorted_numbers[number_index + 1])

        if not len(nears) and len(sorted_numbers):
            nears.append(sorted_numbers[0])
            nears.append(sorted_numbers[0])

        while len(nears) < 2:
            nears.append(None)

        return nears
