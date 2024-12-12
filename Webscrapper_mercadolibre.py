import requests
from bs4 import BeautifulSoup
from beautifultable import BeautifulTable

def GetSoup(url,search):
    URL_FINAL = f'{URL_BASE}{search}'
    r = requests.get(URL_FINAL)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
def AveragePrice(soup):
    pricelist = []
    for article in soup.find_all('li', class_='ui-search-layout__item'):
        price = article.find(class_='andes-money-amount andes-money-amount--cents-superscript').get('aria-label')
        pricelist.append(int(price.split()[0]))
        avg = round(sum(pricelist) / len(pricelist),2)
    return avg

URL_BASE = 'https://listado.mercadolibre.com.ve/'
search_list=['chromebook','laptop','lampara de mesa']
dic = {}

for page in search_list:
    if " " in page:
        page = page.replace(" ", "-")
    soup = GetSoup(URL_BASE,page)
    aveg_price = AveragePrice(soup)
    dic[page] = aveg_price

table = BeautifulTable()

# Añadir las columnas a la tabla
table.columns.header = ["Artículo", "Precio"]

for articulo, precio in dic.items():
    table.rows.append([articulo, precio])

print(table)





