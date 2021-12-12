import requests
from bs4 import BeautifulSoup as BS

URL = 'https://avelux.by/katalog.html'

def get_html():
    response = requests.get(URL)
    return BS(response.text, features = "html.parser")

Html1 = get_html()
lis = []
res = Html1.select('#vidy > div > div > div')
for elem in res:
    header = elem.find("h1")
    print(header.text)
    prise = elem.find("p")
    print(prise.text)
    size = elem.find("h4")
    print(size.text)
    power = elem.find("table")
    power = power.stripped_strings
    for i in power:
        print(f'{i}',end=' ')
    print('\n')
