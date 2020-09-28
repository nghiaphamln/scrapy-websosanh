import scrapy
from scrapy_splash import SplashRequest
from crawler.items import LazadaItem


class LazadaSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['lazada.vn']
    start_urls = ['https://www.lazada.vn/products/iphone-11-chinh-hang-vna-moi-100-chua-kich-hoat-chua-qua-su-dung-bao-hanh-12-thang-tai-ttbh-apple-tra-gop-lai-suat-0-qua-the-tin-dung-man-hinh-liquid-retina-hd-61inch-face-id-chong-nuoc-i327676340-s524116720.html?spm=a2o4n.searchlistcategory.list.1.6ba225904i7Oy9&search=1']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, endpoint="render.html", callback=self.parse)

    def parse(self, response):
        comment = LazadaItem()
        for data in response.xpath("//div[@class='mod-reviews']/div[@class='item']"):
            comment['name'] = data.xpath("./div[2]/span[1]/text()").extract_first()
            comment['comment'] = data.xpath("./div[3]/div[1]/text()").extract_first()
            yield comment
