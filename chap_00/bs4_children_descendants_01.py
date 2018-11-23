from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

children = bs.find('table', {'id':'giftList'}).children
# print(children)

for child in children:
    print(child)