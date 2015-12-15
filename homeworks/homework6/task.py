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
