from fpdf import FPDF
from bs4 import BeautifulSoup
import requests

URL = "https://fundamentus.com.br/resultado.php"
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
site = requests.get(URL, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

pdf_file = 'tabela.pdf'

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

for tr in soup.find_all('tr'):
    th_tags = [th.text for th in tr.find_all('th')]
    td_tags = [td.text.strip() for td in tr.find_all('td')]

    if th_tags:
        for item in th_tags:
            pdf.cell(40, 10, str(item))
        pdf.ln()
    elif td_tags:
        for item in td_tags:
            pdf.cell(40, 10, str(item))
        pdf.ln()

pdf.output(pdf_file, 'F')