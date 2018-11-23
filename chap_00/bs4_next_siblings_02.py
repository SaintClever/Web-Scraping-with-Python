from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

# next_siblings_ = bs.find('table', {'id':'giftList'}).tr.next_siblings

# or ---

# next_siblings_ = bs.table.tr.next_siblings

# or 

next_siblings_ = bs.tr.next_siblings

for next_sibling in next_siblings_:
    print(next_sibling)
