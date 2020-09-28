import scrapy
from crawler.items import CrawlerItem
from scrapy_splash import SplashRequest


class WebsosanhSpider(scrapy.Spider):
    name = 'wss'
    allowed_domains = ['websosanh.vn']
    start_urls = ['https://websosanh.vn/dien-thoai-may-tinh-bang/cat-85.htm']

    script = """
            function main(splash)
                assert(splash:go(splash.args.url))
                assert(splash:runjs("$('.next')[0].click();"))
                assert(splash:wait(1))
                return {
                    html = splash:html(),
                    url = splash:url()
                }
            end
            """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, endpoint="render.html", callback=self.parse)

    def parse(self, response):
        item = CrawlerItem()
        for data in response.xpath("//li[@class='product-item']"):
            item['name'] = data.xpath("./a/h3/text()").extract_first()
            item['price'] = data.xpath("./a/span[3]/span/text()").extract_first()
            item['image'] = data.xpath("./a/span[1]/img/@src").extract_first()
            yield item

        yield SplashRequest(
            url=response.url,
            callback=self.parse,
            meta={
                "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            },
        )
