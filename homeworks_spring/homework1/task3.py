# Task 3 - Fibby Iterson <- I am your father!


class fibonacci_sequence:
    def __init__(self, x):
        self.length = x
        self.this = 1
        self.i = 1
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.this <= self.length:
            self.this += 1
            value = self.i
            self.i = self.i + self.j
            self.j = value
            return value
        else:
            raise StopIteration
