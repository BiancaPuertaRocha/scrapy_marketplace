import scrapy
from scrapy_marketplace.spiders.base import BaseSpider

class MercadolibreSpider(BaseSpider):
    name = "mercadolibre"
    allowed_domains = ["mercadolivre.com"]
    start_urls = ["https://lista.mercadolivre.com.br/{term}"]


    def parse(self, response):
        for product in response.css('.ui-search-result__content'):
            name = product.css('h2 ::text').get()
            value = ""
            for part in product.css('div.ui-search-price--size-medium .price-tag-amount span[class^="price-tag-"]'):
                value += part.css('::text').get()

            yield {
                'source': 'mercadolibre',
                'name': name,
                'price': value,
            }

