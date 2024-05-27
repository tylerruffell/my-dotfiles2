import requests
from bs4 import BeautifulSoup

# url_site = 'http://pythonscraping.com/pages/warandpeace.html'
url_site = 'http://icarus.cs.weber.edu/~hvalle/cs3030_flex/pages/warandpeace.html'
page = requests.get(url_site)
print(f'Page Acces status {page.status_code}')
print(page.text)

bs = BeautifulSoup(page.text, 'html.parser')
name_list = bs.find_all('span',{'class':'green'})
for name in name_list:
    print(name.get_text())

# fir multiple filters
name_list = bs.find_all('span',{'class':['green', 'red']})
for name in name_list:
    print(name.get_text())
