from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

note = bs.find('span', {'class':'excitingNote'})
print(note)
print('')

print('--- previous_sibling ---')
print(note.parent.previous_sibling)
print('')

print('--- next_sibling ---')
print(note.parent.next_sibling)
print('')

print('--- parent ---')
print(note.parent.parent)