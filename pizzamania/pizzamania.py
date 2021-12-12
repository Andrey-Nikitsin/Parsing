import requests
from bs4 import BeautifulSoup as BS

getr = []

URL = 'https://pizzamania.by/'

def get_html():
    response = requests.get(URL)
    return BS(response.text, features = "html.parser")

Html1 = get_html()
tag = Html1.header
tag.decompose()
bonuse = Html1.select('body > div.fixed-bonus')[0]
bonuse.decompose()
delivery = Html1.select('#delivery')[0]
delivery.decompose()
footer = Html1.footer
footer.decompose()
res = Html1.select('body')[0]

res = res.stripped_strings
for i in res:
    getr.append(i)
getr = getr[:-32]
for elem in getr:
    if elem == '?':
        index = getr.index(elem)
        a = getr[index-1]
        getr[index] = a
        getr[index-1] = '\n'
        getr.insert(index-1,'\n')
        getr.insert(index-2,'\n')
    if elem == 'В корзину':
        getr.pop(getr.index(elem))
getr.insert(0, '')
getr.insert(len(getr)-1,'\n')
' '.join(getr)


with open('info.txt', 'w') as file:
    file.write(' '.join(getr))