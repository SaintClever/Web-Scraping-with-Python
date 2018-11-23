from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://read.amazon.com/')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.find_all('span', {'class':{'green':'red'}}))