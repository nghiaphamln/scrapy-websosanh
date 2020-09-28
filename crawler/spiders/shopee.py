import scrapy
from crawler.items import ShopeeItem
from scrapy_splash import SplashRequest


class ShopeeSpider(scrapy.Spider):
    name = 'shopee'
    allowed_domains = ['shopee.vn']
    start_urls = ['https://shopee.vn/product/104376285/7837436093']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, endpoint="render.html", callback=self.parse)

    def parse(self, response):
        item = ShopeeItem()
        for data in response.xpath("//div[@class='shopee-product-rating__main']"):
            item['name'] = data.xpath("./a/text()").extract_first()
            item['comment'] = data.xpath("./div[2]/text()").extract_fist()
            item['time'] = data.xpath("./div[5]/text()").extract_first()
            yield item
            yield {
                'data': data
            }
