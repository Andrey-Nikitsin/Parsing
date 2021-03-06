from class_parent import ParentClass
import requests
from bs4 import BeautifulSoup as BS

class MazChildClass(ParentClass):
    def parse(self):
        text_site = []
        res = self.response()
        for i in res:
            if 'МАЗ' in i:
                text_site.append(f'\n\n{i}\n')
            else:
                text_site.append(i)
        return text_site

    def show(self):
        g = self.parse()
        text_site = g.copy()
        return ' '.join(text_site)

maz = MazChildClass()
maz.sew_url('http://maz.by/products/passenger-vehicles')
maz.sew_selector("#bus")
print(maz.show())