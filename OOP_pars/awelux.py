from class_parent import ParentClass
import requests
from bs4 import BeautifulSoup as BS

class AweluxChildClass(ParentClass):
    def response(self):
        response = requests.get(self.get_url())
        html = BS(response.text, features="html.parser")
        res = html.select(self.get_selector())
        return res
    def parse(self):
        text_site = []
        res = self.response()
        for elem in res:
            header = elem.find("h1")
            text_site.append(header.text)
            prise = elem.find("p")
            text_site.append(prise.text)
            size = elem.find("h4")
            text_site.append(size.text)
            power = elem.find("table")
            power = power.stripped_strings
            power_list = ''
            for i in power:
                power_list += i
            power_list += '\n'
            text_site.append(power_list)
        return text_site
    def show(self):
        text_site = self.parse()
        for elem in text_site:
            print(elem)

awelux = AweluxChildClass()
awelux.sew_url('https://avelux.by/katalog.html')
awelux.sew_selector('#vidy > div > div > div')
print(awelux.show())