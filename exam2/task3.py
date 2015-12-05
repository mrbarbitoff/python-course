# Task 3
import re
import requests
from lxml import etree

twittor = requests.get('https://twitter.com/googlefacts').text
parser = etree.HTMLParser()

tree = etree.fromstring(twittor, parser)

for tweet in tree.iter("p"):
    if 'tweet-text' in str(tweet.attrib):
        print(tweet.text)
