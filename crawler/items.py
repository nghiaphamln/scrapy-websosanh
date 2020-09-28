# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()


class ShopeeItem(scrapy.Item):
    name = scrapy.Field()
    comment = scrapy.Field()
    time = scrapy.Field()


class LazadaItem(scrapy.Item):
    name = scrapy.Field()
    comment = scrapy.Field()
