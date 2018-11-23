from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.buybuybaby.com/store/?enginename=google&mcid=PS_google_brand_brand_&adpos=1t1&creative=264981613824&device=c&matchtype=e&network=g&mrkgadid=350266178&mrkgcl=611&rkg_id=0&gclid=Cj0KCQiA28nfBRCDARIsANc5BFCi5XbE5py5jTjzP4oTfd5bhSDnIpAO33Bd4bjkcRn1Vy0kRli1-VwaAj3hEALw_wcB&gclsrc=aw.ds')
# print(html.read())

bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.title)
# print(bs.findAll('span', {'class':'hide'}))

hidden_content = bs.findAll('span', {'class':'hide'})
# print(hidden_content)
for content in hidden_content:
    print(content.get_text())