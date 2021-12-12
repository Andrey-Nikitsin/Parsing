import requests
from bs4 import BeautifulSoup as BS

getr = []

URL = 'http://maz.by/products/passenger-vehicles'

def get_html():
    response = requests.get(URL)
    return BS(response.text, features = "html.parser")

Html1 = get_html()
res = Html1.select('#bus')[0]
res = res.stripped_strings
for i in res:
    if 'МАЗ' in i:
        getr.append(f'\n\n{i}\n')
    else:
        getr.append(i)
with open('info.txt', 'w') as file:
    file.write(' '.join(getr))