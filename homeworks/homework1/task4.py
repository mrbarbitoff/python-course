# Task 4
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
