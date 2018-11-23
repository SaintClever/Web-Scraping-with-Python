from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

# print(bs)

id_ = bs.find_all(id='text')
print(id_)

id_ = bs.find_all('', {'id':'text'})
print(id_)