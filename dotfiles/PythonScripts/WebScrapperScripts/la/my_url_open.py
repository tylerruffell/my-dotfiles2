from urllib.request import urlopen

url_site = 'http://pythonscraping.com/pages/page1.html'
html = urlopen(url_site)

print(html.read())