# Task 2
inp = input()
prepr = inp.split()
numbers = []
for number in prepr:
    numbers.append(int(number))
print(sum(numbers)/len(numbers))
# Alternatively, could use numpy.mean() that does not work in Stepic
