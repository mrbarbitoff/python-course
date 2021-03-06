# Task 4
import re
import sys

test_code = sys.stdin.read()
lines = test_code.split('\n')
itervar = 1
assignments = []

for line in lines:
    line = line.strip()
    if len(re.findall('\.\.', line)) > 0:
        itervar += 1
        continue
    assign_here = re.findall('^([^#.[\]]+\.?[^#[\]]*?) = .*', line)
    if len(assign_here) == 1:
        assignments.append(str(itervar) + ' ' + ' '.join(assign_here[0].split(',')))
    itervar += 1
    
print('\n'.join(assignments))
