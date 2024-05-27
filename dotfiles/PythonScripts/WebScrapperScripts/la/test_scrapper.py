
from urllib.request import urlopen
from bs4 import BeautifulSoup

# url_site = 'http://pythonscraping.com/pages/page1.html'
url_site = 'http://icarus.cs.weber.edu/~hvalle/cs3030_flex/pages/page1.html'
html = urlopen(url_site)

bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.title)
print(bs.h1)
