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
