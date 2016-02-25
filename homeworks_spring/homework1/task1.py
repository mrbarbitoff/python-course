# Task 1 - Safe sum ('... without the condom the sex is better...' LINDEMANN - Praise Abort (c))


def sum(x, y):
    if type(x) is not int or type(y) is not int:
        raise TypeError
    elif x <= 0 or y <= 0:
        raise ValueError
    return x + y
