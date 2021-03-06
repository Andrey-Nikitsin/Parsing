import requests
from bs4 import BeautifulSoup as BS

class pars:
    url = None
    selector = None
    def sew_url(self,url):
        self.url = url
    def get_url(self):
        return self.url
    def get_selector(self):
        return self.selector
    def sew_selector(self,selector):
        self.selector = selector
    def response(self):
        response = requests.get(self.get_url())
        html = BS(response.text, features="html.parser")
        res = html.select(self.get_selector())[0]
        res = res.stripped_strings
        return res
    def parse(self):
        text_site = []
        res = self.response()
        for elem in res:
            text_site.append(elem)
        return text_site[17:-55]
    def show(self):
        g = self.parse()
        text_site = g.copy()
        for elem in text_site:
            if elem == '?':
                index = text_site.index(elem)
                a = text_site[index - 1]
                text_site[index] = a
                text_site[index - 1] = '\n'
                text_site.insert(index - 1, '\n')
                text_site.insert(index - 2, '\n')
            if elem == 'В корзину':
                text_site.pop(text_site.index(elem))
        text_site.insert(0, '')
        text_site.insert(len(text_site) - 1, '\n')
        return ' '.join(text_site)
pizza = pars()
pizza.sew_url('https://pizzamania.by/')
pizza.sew_selector("body")
print(pizza.show())






