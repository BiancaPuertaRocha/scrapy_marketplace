import scrapy
from selenium import webdriver

class BaseSpider(scrapy.Spider):
    def __init__(self, term='', **kwargs):
        self.start_urls = [url.replace('{term}', term) for url in self.start_urls] 
        self.webdriver = webdriver.Chrome()
        super(scrapy.Spider).__init__()

    def parse(self, response):
        pass