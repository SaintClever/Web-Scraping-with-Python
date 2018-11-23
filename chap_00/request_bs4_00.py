from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# print(html.read())

bs = BeautifulSoup(html.read(), 'html.parser')
# print(bs)
# print(bs.h1)
# print(bs.findAll('span', {'class':'green'}))

nameList = bs.findAll('span', {'class':'green'})

for name in nameList:
    print(name.get_text())