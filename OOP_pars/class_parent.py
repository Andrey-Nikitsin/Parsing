import requests
from bs4 import BeautifulSoup as BS

class ParentClass:
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