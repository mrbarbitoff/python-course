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
