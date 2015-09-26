# Task 3 - correected using specific features (many thx to KZ)
inp = input()
numbers = inp.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
even = sorted(numbers[0::2])
odd = sorted(numbers[1::2], reverse=True)
out = []
for i in range(len(even)):
    out.append(even[i])
    out.append(odd[i])
output = ' '.join([str(number) for number in out])
print(output)
