from random import random


class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration




x = RandomIterator(3)

# for i in RandomIterator(10):
#     print(i)
#
# for i in RandomIterator(10):
#     print(i)
#
print(list(RandomIterator(4)))