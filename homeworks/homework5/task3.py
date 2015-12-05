# Task 3
import re
import sys


test_code = sys.stdin.read()
lines = test_code.split('\n')
itervar = 1
assignments = []

for line in lines:
    assign_here = re.findall('(\w+) = .*', line)
    if len(assign_here) == 1:
        assignments.append(str(itervar) + ' ' + assign_here[0])
    itervar += 1
    
print('\n'.join(assignments))    
