import requests
from bs4 import BeautifulSoup

res = requests.get("http://lolipop.jp")
soup = BeautifulSoup(res.text)

#print(soup)
title_tag = soup.head.title
print(type(title_tag))
print("tag name: " + title_tag.name)
print("value: " + title_tag.string)

a_tag = soup.findAll('a')
for link in a_tag:
    print(link.get('href'))
