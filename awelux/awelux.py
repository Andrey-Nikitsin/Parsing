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
    lis.append(header.text)
    prise = elem.find("p")
    lis.append(prise.text)
    size = elem.find("h4")
    lis.append(size.text)
    power = elem.find("table")
    power = power.stripped_strings
    power_list = ''
    for i in power:
        power_list+=i
    power_list += '\n'
    lis.append(power_list)
for elem in lis:
    print(elem)