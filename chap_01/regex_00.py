from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

imgs = bs.find_all('img')

for img in imgs:
    # print(img)
    # print(img.attrs)
    print(img.attrs['src'])
print('')
# or

img_path = re.compile('\.\.\/img\/gifts/img.*\.jpg')
images = bs.find_all('img', {'src':img_path})

for image in images:
    print(image['src']) # key:value pair located