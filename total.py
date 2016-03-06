#!/usr/bin/env python3

import os
import subprocess


# all_files = subprocess.call('ls')

file_names = []
for i in os.walk('.'):
    prefix, subdir, files = i
    files_wpref = [prefix + '/' + x for x in files]
    file_names.extend(files_wpref)
    
file_names = [file_name for file_name in file_names if file_name.endswith('.py')]

code = []
for fn in file_names:
    p = subprocess.Popen(["cat", fn], stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    code.append(stdout.decode("utf-8"))
    
with open('total.py', 'w') as ofile:
     ofile.write('\n'.join(code))

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

# Task 2
# Order of symdols matters a lot, huh
import re
import requests

addresses = []
with open('links.txt', 'r') as ifile:
    for line in ifile:
        addresses.append(line.strip())


mailinglst = set()
for lnk in addresses:
    data = requests.get(lnk)
    mails = re.findall('[.\w]+@[.\w]+', data.text)  # re.findall('[\w\.]+@[\w\.]+', data.text) yields 10 mails, as well as \.\w and \w.
    for mail in mails:
        if len(re.findall('^\.|\.$|\.@|@\.', mail)) == 0:
            mailinglst.add(mail)

print("\n".join(mailinglst))

# Task 3
import re
import requests
from lxml import etree

twittor = requests.get('https://twitter.com/googlefacts').text
parser = etree.HTMLParser()

tree = etree.fromstring(twittor, parser)

for tweet in tree.iter("p"):
    if 'class' in tweet.attrib:
        if 'tweet-text' in tweet.attrib['class']:
            print(tweet.text)

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

# Task 2
import math


nouns = set()
adjectives = set()
verbs = set()

with open('dict.txt', 'r') as fh:
    for line in fh:
        line = line.rstrip()
        if line.endswith('ka'):
            nouns.add(line)
        elif line.endswith('yo'):
            adjectives.add(line)
        else:
            verbs.add(line)

adjcomb = 0
wheretostop = 7 if len(adjectives) > 7 else len(adjectives)
for i in range(1, wheretostop + 1):
    adjcomb += math.factorial(len(adjectives))/math.factorial(len(adjectives) - i)       
numsentences = int(len(nouns)*len(verbs)*adjcomb)
print(numsentences)

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

# Task 0 - ECHO
a = print(input())

# Task 1
obj = input()
num = int(input())
if obj == 'утюг':
    sclon = ['утюг', 'утюга', 'утюгов']
else:
    sclon = ['ложка', 'ложки', 'ложек']
if num % 10 == 1 and num % 100 != 11:
    print(num, sclon[0])
elif 2 <= num % 10 <= 4 and (12 > num % 100 or num % 100 > 14):
    print(num, sclon[1])
else:
    print(num, sclon[2])

# Task 2
inp = input()
prepr = inp.split()
numbers = []
for number in prepr:
    numbers.append(int(number))
print(sum(numbers)/len(numbers))
# Alternatively, could use numpy.mean() that does not work in Stepic

# Task 3 - correected using specific features (many thx to KZ)
inp = input()
numbers = inp.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
even = sorted(numbers[0::2])
odd = sorted(numbers[1::2], reverse=True)
out = []
for i in range(len(even)):
    out.append(even[i])
    out.append(odd[i])
output = ' '.join([str(number) for number in out])
print(output)

# Task 4
string = input()
counts = dict()
for letter in string:
    counts[letter] = counts.get(letter, 0) + 1
ordered = []
for kvpair in counts.items():
    ordered.append(kvpair)
ordered.sort()
for kvpair in ordered:
    print(kvpair[0], kvpair[1])

#!/usr/bin/env python3
# Wiki player
import re
import requests
from lxml import etree

prsr = etree.HTMLParser()

# Find valid wiki links
def findLinks(lnk):
    links = set()
    page = requests.get(lnk).text
    tree = etree.fromstring(page, prsr)
    for sth in tree.iter("div"):
        if 'class' in sth.attrib and sth.attrib['class'] == "mw-body-content":
            for a in sth.iterdescendants('a'):
                if 'href' in a.attrib:
                   links_here = re.findall('wiki/\S+', a.attrib['href'])
                   for some_link in links_here:
                       if len(re.findall(':|[^i]/|Main_Page', some_link)) == 0:
                           links.add('https://en.wikipedia.org/' + some_link)
    return links

# Get links to take care of
link_in = input()
link_out = input()

# DFS-like searching - no recursion/reusage for more convenience in using global variables. Prints for easier tracking.
# Needed variables
seen_links = []
route = [link_in]
found = False
second_level = findLinks(link_in)

# Search per se
if link_out in second_level:
    found = True
else:
    for i, lnk in enumerate(second_level):
        print('Searching link', i + 1,  'out of', len(second_level), 'on level 2...', lnk)
        seen_links.append(lnk)
        route.append(lnk)
        third_level = findLinks(lnk)
        if link_out in third_level:
            found = True
            break
        for j, lnk2 in enumerate(third_level):
            print('Searching link', j + 1, 'out of', len(third_level), 'on final level...', lnk2)
            if lnk2 in seen_links:
                continue
            seen_links.append(lnk2)
            route.append(lnk2)
            if link_out in findLinks(lnk2):
                found = True
                break
            else:
                route = route[:2]
        if found:
            break
        route = route[:1]

#Output
if found:
    route.append(link_out)
    print('\n'.join(route))
else:
    # Deeply sorry for being rough :(
    print('GFY')

def plural(n, forms):
    if n % 10 == 1 and n % 100 != 11:
        return forms[0]
    elif 2 <= n % 10 <= 4 and (12 > n % 100 or n % 100 > 14):
        return forms[1]
    else:
        return forms[2]


words = {"утюг": ["утюг", "утюга", "утюгов"],
         "ложка": ["ложка", "ложки", "ложек"],
         "гармошка": ["гармошка", "гармошки", "гармошек"],
         "чайник": ["чайник", "чайника", "чайников"]}

thing = input()
number = int(input())
print(" ".join((str(number), plural(number, words[thing]))))

def combinations(n, k):
    if k > n:
        return 0
    if k == n or k == 0:
        return 1
    return combinations(n - 1, k - 1) + combinations(n - 1, k)


print(combinations(*(int(x) for x in input().split())))

import math


def prime(number):
    if number == 2 or ((number - 1)/2) % 1 == 0 and (math.factorial(number - 3) - int((number - 1)/2)) % number == 0:
        return True
    else:
        return False


n = int(input())
for _ in range(n):
    print(prime(int(input())))

def euclid(n, m):
    if max(n, m) % min(n, m) == 0:
        return min(n, m)
    return euclid(min(n, m), max(n, m) % min(n, m))


hcd = euclid(*(int(x) for x in input().split()))
print(hcd)

def euclid(n, m):
    if max(n, m) % min(n, m) == 0:
        return min(n, m)
    return euclid(min(n, m), max(n, m) % min(n, m))


def rpfilter(a, *args):
    rp_numbers = []
    for number in args:
        if euclid(number, a) == 1:
            rp_numbers.append(number)
    return rp_numbers


rp_list = rpfilter(*(int(x) for x in input().split()))
print(" ".join((str(x) for x in rp_list)) if len(rp_list) > 0 else None)

import re
import sys

text = sys.stdin.read()
print(len(re.findall('you', text)))

import re
import sys

text = sys.stdin.read()
print(len(re.findall('[Yy]ou', text)))

import re
import sys

all_phones = sys.stdin.read()
cool = re.findall('(\d*(111|222|333|444|555|666|777|888|999|000)\d*)', all_phones)
print('\n'.join([x[0] for x in cool]))

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

# Final task here
import re
import sys

text = sys.stdin.read()
print(re.sub('[\t:;\-\n,\.!?\'\"_\(\)\[\]\{\}~\*\+=/\\\^&%\$#` ]+', ' ', text))


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

# Task 2
import math


nouns = set()
adjectives = set()
verbs = set()

with open('dict.txt', 'r') as fh:
    for line in fh:
        line = line.rstrip()
        if line.endswith('ka'):
            nouns.add(line)
        elif line.endswith('yo'):
            adjectives.add(line)
        else:
            verbs.add(line)

adjcomb = 0
wheretostop = 7 if len(adjectives) > 7 else len(adjectives)
for i in range(1, wheretostop + 1):
    adjcomb += math.factorial(len(adjectives))/math.factorial(len(adjectives) - i)       
numsentences = int(len(nouns)*len(verbs)*adjcomb)
print(numsentences)

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

from random import shuffle
import re


class Song:
    def __init__(self, name, artist, album, position, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = position
        self.year = int(year)
        self.duration = int(duration)

    def __repr__(self):
        song = "Song \"%s\" by %s from album \"%s\" (%d) - position %s, %d" % (self.name, self.artist, self.album, self.year, self.position, self.duration)
        return song

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False


def import_songs(input_file):
    with open(input_file, 'r') as fh:
        songs = []
        for line in input_file:
            line.rstrip()
            songs.append(Song(*line.split('\t')))
    return songs


def export_songs(songs, target_file):
    with open(target_file, 'w') as ofile:
        for song in songs:
            ofile.write('\t'.join([song.name, song.artist, song.album, song.position, str(song.year), str(song.duration)]) + '\n')


def shuffle_songs(songs):
    shuffle(songs)
    return songs


# Most frequent artist
counts = {}
for song in songs:
    artist_name = song.artist
    counts[artist_name] = counts.get(artist_name, 0) + 1
max_count = None
for artist_name, count in counts.items():
    if max_count is None or count > max_count:
        popular = artist_name
        max_count = count
print(popular)


# Longest song
max_length = None
for song in songs:
    if max_length is None or song.duration > max_length:
        long_song = (song.name, song.artist)
        max_length = song.duration
print("\t".join(long_song))


# Longest album
album_lengths = {}
for song in songs:
    key = song.album + "\t" + song.artist
    album_lengths[key] = album_lengths.get(key, 0) + song.duration
max_duration = None
for album, duration in album_lengths.items():
    if max_duration is None or duration > max_duration:
        our_victim = album
        max_duration = duration
print(our_victim)


# Most frequent word
words = {}
for song in songs:
    song_words = re.findall('[a-zA-Z]+', song.name)
    for word in song_words:
        word = word.lower()
        words[word] = words.get(word, 0) + 1
word_counts = sorted([(x[1], x[0]) for x in list(words.items())], reverse=True)
num_words = 10 if len(word_counts) > 10 else len(word_counts)
print("\t".join([x[1].lower() for x in word_counts[:num_words]]))


# Highest album count
album_counts = {}
for song in songs:
    album_counts[song.artist] = album_counts.get(song.artist, []) + [song.album]
max_count = None
for artist, albums in album_counts.items():
    albums = set(albums)
    if max_count is None or len(albums) > max_count:
        cool_artist = artist
        max_count = len(albums)
print(cool_artist)

# Task 1 - Safe sum ('... without the condom the sex is better...' LINDEMANN - Praise Abort (c))


def sum(x, y):
    if type(x) is not int or type(y) is not int:
        raise TypeError
    elif x <= 0 or y <= 0:
        raise ValueError
    return x + y

# Task 2 - Catch me if you can!


try:
    foo()
except AssertionError:
    print('Caught AssertionError')
except MemoryError:
    print('Caught MemoryError')
except RuntimeError:
    print('Caught RuntimeError')

# Task 3 - Fibby Iterson <- I am your father!


class fibonacci_sequence:
    def __init__(self, x):
        self.length = x
        self.this = 1
        self.i = 1
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.this <= self.length:
            self.this += 1
            value = self.i
            self.i = self.i + self.j
            self.j = value
            return value
        else:
            raise StopIteration

# Task 4 - People say this is tricky, though it seems not at all

stack_size = int(input())
callstack = input().split()
dummy_number = int(input())
exception_handling = {}
for _ in range(dummy_number):
    fun, inex, outex = input().split()
    if fun in exception_handling:
        exception_handling[fun][inex] = outex
    else:
        exception_handling[fun] = {inex: outex}
this_exception = input()

output_stack = callstack.copy()
for i in range(1, stack_size + 1):
    can = this_exception in exception_handling[callstack[-i]]
    if can:
        if exception_handling[callstack[-i]][this_exception] == '_':
            break
        else:
            this_exception = exception_handling[callstack[-i]][this_exception]
            output_stack = output_stack[:-1]
    else:
        output_stack = output_stack[:-1]
        continue

print(' '.join(output_stack))
