# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    table = scrapy.Field()
