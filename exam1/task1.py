# Task 1 on exam 1

# This variant is f***ing memory-efficient, though not fancy
with open('yazkora.txt', 'r') as fh:
    with open('answer.txt', 'w') as ofile:
        sentence = ''
        adjectives = ''
        for line in fh:
            line = line.rstrip()
            checkpoint = len(line)
            dots = [x for x, s in enumerate(line) if s == '.']
            dots.append(len(line))
            for offset in dots:
                sentence += line[:offset]
                if offset != checkpoint:
                    content = sentence.split()
                    for word in content:
                        if word.endswith('yo'):
                            adjectives += word + ' '
                    ofile.write(adjectives + '\n')
                    sentence = ''
                    adjectives = ''
                    line = line[offset + 1:]
                                 
                
                        
        
