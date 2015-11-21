# This variant is f***ing memory-efficient, though not fancy

with open('yazkora.txt', 'r') as fh:
    with open('answer.txt', 'w') as ofile:
        sentence = ''
        adjectives = ''
        for line in fh:
            line = line.rstrip() + ' '
            dots = [x for x, s in enumerate(line) if s == '.']
            dots.append(len(line))
            previous_offset = 0
            for offset in dots:
                sentence += line[previous_offset:offset]
                if offset != len(line):
                    content = sentence.split()
                    for word in content:
                        if word.endswith('yo'):
                            adjectives += word + ' '
                    ofile.write(adjectives + '\n')
                    sentence = ''
                    adjectives = ''
                    previous_offset = offset + 1
