# Task 2 - people say a tricky one

import re


dummy_n = int(input())
class_defs = {}
for _ in range(dummy_n):
    classes_here = re.findall('\w+', input())
    class_defs[classes_here[0]] = classes_here[1:] if len(classes_here) > 1 else []


def checkinheritance(first, second):
    if first == second:
        return True
    if first in class_defs[second]:
        return True
    for i in class_defs[second]:
        inh = checkinheritance(first, i)
        if inh:
            return True
    return False

dummy_n = int(input())
for _ in range(dummy_n):
    if checkinheritance(*input().split()):
        print('Yes')
    else:
        print('No')
