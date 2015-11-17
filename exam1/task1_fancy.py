import re

# This variant is f**king not memory-efficient, though cute
with open('yazkora.txt', 'r') as fh:
    text = ''
    for line in fh:
        text += line.rstrip() + ' '
             
with open('answer.txt', 'w') as ofile:
    sentences = text.split('.')
    for sentence in sentences:        
        ofile.write(" ".join(re.findall('[a-z]+yo', sentence)) + '\n')
