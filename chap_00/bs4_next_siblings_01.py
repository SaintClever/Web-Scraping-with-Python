from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

next_siblings_ = bs.find('table', {'id':'giftList'}).tr.next_siblings
print(next_siblings_)

for next_sibling in next_siblings_:
    print(next_sibling)