import requests
from bs4 import BeautifulSoup as BS

getr = []

URL = 'https://pizzamania.by/'
def get_html():
    response = requests.get(URL)
    return BS(response.text, features = "html.parser")

site_html = get_html()

class pars:
    url = None

    def get_url(self):
        return self.url

    def set_url(self,url):
        self.url = url

    def select(self):
        text_site = []
        res = site_html.select(self.get_url())[0]
        res = res.stripped_strings
        for elem in res:
            text_site.append(elem)
        return text_site

    def get_text(self):
        list_text = self.select()
        for elem in list_text:
            if elem == '?':
                index = list_text.index(elem)
                a = list_text[index-1]
                list_text[index] = a
                list_text[index-1] = '\n'
                list_text.insert(index-1,'\n')
                list_text.insert(index-2,'\n')
            if elem == 'В корзину':
                list_text.pop(list_text.index(elem))
        list_text.insert(0, '')
        list_text.insert(len(getr)-1,'\n')
        return list_text

pizza = pars()
pizza_1metr = pars()
combo = pars()
burgers = pars()
salads = pars()
pasta = pars()
pizza.set_url('#pizza')
pizza_1metr.set_url('#Pmmetr')
combo.set_url('#combo')
burgers.set_url('#burger')
salads.set_url('#salads')
pasta.set_url("#Pasta")

print(pasta.get_text())

with open('info.txt', 'w') as file:
    file.write(' '.join(pasta.get_text()))