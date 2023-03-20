import scrapy
from scrapy_marketplace.spiders.base import BaseSpider

class MagaluSpider(BaseSpider):
    name = "magalu"
    allowed_domains = ["www.magazineluiza"]
    start_urls = ["https://www.magazineluiza.com.br/busca/{term}"]

    def parse(self, response):
        for product in response.xpath('//div[@data-testid="product-card-content"]'):
            name = product.css('h2 ::text').get()
            value = product.xpath('//p[@data-testid="price-value"]/text()').get()
            yield {
                'name': name,
                'value': value,
            }
