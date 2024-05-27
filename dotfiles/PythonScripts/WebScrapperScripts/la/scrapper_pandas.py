import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

url = 'http://en.wikipedia.org/wiki/Comparison_of_text_editors'
page = requests.get(url)
print(f'Page Acces status {page.status_code}')

bs = BeautifulSoup(page.text, 'html.parser')
table = bs.find('table', {'class':'wikitable'})

df = pd.read_html(io.StringIO(str(table)))
#print(df)
#conver the datafram to list
df = pd.DataFrame(df[0])
for index in df.index:
    print(f"Col {index} rec {df['Name'][index]}")


#for row in rows:
#    for cell in row.findAll(['td', 'th']):
