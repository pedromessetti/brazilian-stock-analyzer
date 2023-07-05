from bs4 import BeautifulSoup
import requests
import csv

def generate_csv():
    url = "https://fundamentus.com.br/resultado.php"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
            
        with open('stocks.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for tr in soup.find_all('tr'):
                data = []
                for th in tr.find_all('th'):
                    data.append(th.text.strip().upper())
                if data:
                    writer.writerow(data)
                    continue
                data = [td.text.strip().replace('%', '').replace('.', '').replace(',', '.') for td in tr.find_all('td')]
                try:
                    writer.writerow([float(val) if val else None for val in data])
                except ValueError:
                    writer.writerow(data)
        print('CSV successfully generated!')
    else:
        print(f'Error: Response Status Code {self.response.status_code}')
