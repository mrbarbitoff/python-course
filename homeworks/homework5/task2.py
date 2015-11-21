import re
import sys

all_phones = sys.stdin.read()
cool = re.findall('(\d*(111|222|333|444|555|666|777|888|999|000)\d*)', all_phones)
print('\n'.join([x[0] for x in cool]))
