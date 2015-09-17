#Homework number 1, just to refresh memory
#Task 0 - ECHO
a = input()		
print(a)

#Task 1
obj = input()
num = int(input())
if obj == 'утюг':
    sclon = ['утюг', 'утюга', 'утюгов']
else:
    sclon = ['ложка', 'ложки', 'ложек']
if num % 10 == 1 and num % 100 != 11:
    print(num, sclon[0])
elif 2 <= num % 10 <= 4 and (12 > num % 100 or num % 100 > 14):
    print(num, sclon[1])
else:
    print(num, sclon[2])

#Task 2
inp = input()
prepr = inp.split()
numbers = []
for number in prepr:
    numbers.append(int(number))
print(sum(numbers)/len(numbers)) 
#Alternatively, could use numpy.mean() that does not work in Stepic

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

#Task 4
string = input()
counts = dict()
for letter in string:
    counts[letter] = counts.get(letter, 0) + 1
ordered = []
for kvpair in counts.items():
    ordered.append(kvpair)
ordered.sort()
for kvpair in ordered:
    print(kvpair[0], kvpair[1])