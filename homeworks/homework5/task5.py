# Final task here
import re
import sys

text = sys.stdin.read()
text_nonewlines = re.sub('\n', ' ', text)
print(re.sub('[.,?!]', '', text_nonewlines))
