import requests
from bs4 import BeautifulSoup
import csv

url = 'http://en.wikipedia.org/wiki/Comparison_of_text_editors'
page = requests.get(url)
print(f'Page Acces status {page.status_code}')

bs = BeautifulSoup(page.text, 'html.parser')
table = bs.find('table', {'class':'wikitable'})
rows = table.findAll('tr')

csv_file = open('editors.csv', 'wt+')
writer = csv.writer(csv_file)
for row in rows:
    csvRow = []
    for cell in row.findAll(['td', 'th']):
        csvRow.append(cell.get_text().strip())
    writer.writerow(csvRow)
csv_file.close()