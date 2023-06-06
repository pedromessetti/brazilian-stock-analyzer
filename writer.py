from bs4 import BeautifulSoup
import requests
import csv

URL = "https://fundamentus.com.br/resultado.php"
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
site = requests.get(URL, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

file = 'tabela.csv'
csv_writer = csv.writer(open(file, 'w'))

for tr in soup.find_all('tr'):
    data = []

    for th in tr.find_all('th'):
        data.append(th.text)

    if data:
        csv_writer.writerow(data)
        continue

    for td in tr.find_all('td'):
        value = td.text.strip()
        if '%' in value:
            value = value.replace('%', '')  # Remove percentage symbol
        if '.' in value and ',' in value:
            value = value.replace('.', '')  # Remove dot as thousands separator
        value = value.replace(',', '.')  # Replace comma with dot as decimal separator
        data.append(value)

    if data:
        csv_writer.writerow(data)
