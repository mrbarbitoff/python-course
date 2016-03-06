# Task 5 - Bad Anton


import re

# AAAAH, I AM COPYPASTING!!!11
dummy_n = int(input())
exc_defs = {}
for _ in range(dummy_n):
    exc_here = re.findall('\w+', input())
    exc_defs[exc_here[0]] = exc_here[1:] if len(exc_here) > 1 else []


def check_anton(first_exc, second_exc):
    if first_exc in exc_defs[second_exc]:
        return True
    for i in exc_defs[second_exc]:
        found = check_anton(first_exc, i)
        if found:
            return True
    return False

one_more_n = int(input())
caught_exceptions = []
for _ in range(one_more_n):
    this_exc = input()
    for j in caught_exceptions:
        if check_anton(j, this_exc):
            print(this_exc)
            break
    caught_exceptions.append(this_exc)
