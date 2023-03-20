import scrapy
from scrapy_marketplace.spiders.base import BaseSpider

class MercadolibreSpider(BaseSpider):
    name = "mercadolibre"
    allowed_domains = ["mercadolivre.com"]
    start_urls = ["https://lista.mercadolivre.com.br/{term}"]


    def parse(self, response):
        print('\n\n')
        print(self.start_urls)
        return None

