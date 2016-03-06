# Task 3 - Kto lezhal na moey devushke i pomyal ee?


import re

# Hopefully, autoplagiarism is OK
dummy_n = int(input())
class_defs = {}
for _ in range(dummy_n):
    classes_here = re.findall('\w+', input())
    class_defs[classes_here[0]] = classes_here[1:] if len(classes_here) > 1 else []

one_more = int(input())
methods = {}
for _ in range(one_more):
    this_class, this_method = input().split()
    methods[this_class] = methods.get(this_class, []) + [this_method]


def findmethod(class_name, method_name):
    if method_name in methods[class_name]:
        return class_name
    for i in class_defs[class_name]:
        found = findmethod(i, method_name)
        if found is not None:
            return found
    return None

call_in, call_what = input().split()
print(findmethod(call_in, call_what))
