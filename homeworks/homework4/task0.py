import re
import sys

text = sys.stdin.read()
print(len(re.findall('you', text)))
