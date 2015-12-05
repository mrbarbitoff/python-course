# Final task here
import re
import sys

text = sys.stdin.read()
print(re.sub('[\t:;\-\n,\.!?\'\"_\(\)\[\]\{\}~\*\+=/\\\^&%\$#` ]+', ' ', text))

