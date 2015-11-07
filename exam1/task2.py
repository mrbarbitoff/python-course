# Task 2
import math


nouns = set()
adjectives = set()
verbs = set()

with open('dict.txt', 'r') as fh:
    for line in fh:
        line = line.rstrip()
        if line.endswith('ka'):
            nouns.add(line)
        elif line.endswith('yo'):
            adjectives.add(line)
        else:
            verbs.add(line)

adjcomb = 0
wheretostop = 7 if len(adjectives) > 7 else len(adjectives)
for i in range(1, wheretostop + 1):
    adjcomb += math.factorial(len(adjectives))/(math.factorial(len(adjectives) - i)*math.factorial(i))        
numsentences = int(len(nouns)*len(verbs)*adjcomb)
print(numsentences)
