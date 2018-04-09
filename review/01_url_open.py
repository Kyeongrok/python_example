from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj)

#url http