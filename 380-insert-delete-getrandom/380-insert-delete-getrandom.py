import random


class RandomizedSet:
    def __init__(self):
        self.random_set = {}
        self.values = []

    def insert(self, val: int) -> bool:
        in_the_set = val in self.random_set
        index = len(self.values)
        if not in_the_set:
            self.random_set[val] = index
            self.values.append(val)
        return not in_the_set

    def remove(self, val: int) -> bool:
        in_the_set = val in self.random_set
        if in_the_set:
            index = self.random_set[val]
            last_value = self.values[-1]
            self.values[index] = last_value
            self.values.pop()
            self.random_set[last_value] = index
            del self.random_set[val]
        return in_the_set

    def getRandom(self) -> int:
        return random.choice(self.values)
