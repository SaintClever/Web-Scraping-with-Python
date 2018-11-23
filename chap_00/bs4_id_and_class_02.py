from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

green = bs.find_all(class_='green')
print(green)
print('')

green = bs.find_all('', {'class':'green'})
print(green)
print('')

red = bs.find_all(class_='red')
print(red)
print('')

red = bs.find_all('', {'class':'red'})
print(red)
