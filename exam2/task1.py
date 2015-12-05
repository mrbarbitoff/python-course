# Task 1
from numpy import argmax
import re

with open('hp5.txt', 'r') as ifile:
    text = ifile.read()

whispers = re.findall('whispered ([A-Z][a-z]+([,\"!?]* [A-Z][a-z]+)?)?', text)
whispers_add = re.findall('(([A-Z][a-z]+ )?[A-Z][a-z]+)?[,\'?!]* whispered', text)
whispers.extend(whispers_add)
counts = {}
for whisper in whispers:
    whisperer = whisper[argmax([len(x) for x in whisper])].strip()
    if len(whisperer) > 1:
        counts[whisperer] = counts.get(whisperer, 0) + 1

chatterboxer = None
maxcount = None
for person, count in counts.items():
    if maxcount is None or count > maxcount:
        chatterboxer = (str(count), person)
        maxcount = count

print(" ".join(chatterboxer))
