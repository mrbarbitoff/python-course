#Task 3 - having a little headache with formatting output
inp = input()
numbers = inp.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
even = []
odd = []
for i in range(len(numbers)//2):
    even.append(numbers[i*2])
    odd.append(numbers[i*2 + 1])
even.sort()
odd.sort()
odd = list(reversed(odd))
out = []
for i in range(len(even)):
    out.append(even[i])
    out.append(odd[i])
output = ''
for elem in out:
    output += str(elem) + ' '
print(output.rstrip())     
