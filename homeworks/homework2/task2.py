import math


def prime(number):
    if number == 2 or ((number - 1)/2) % 1 == 0 and (math.factorial(number - 3) - int((number - 1)/2)) % number == 0:
        print(True)
    else:
        print(False)


n = int(input())
for _ in range(n):
    prime(int(input()))
