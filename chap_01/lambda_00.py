from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

# find tags with 2 attributes
# tag means all elements or captures the entire page
two_attrs = bs.find_all(lambda tag: len(tag.attrs) == 2)
print(two_attrs)