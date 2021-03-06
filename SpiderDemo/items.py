# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderdemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    novel_url = scrapy.Field()
    category = scrapy.Field()
    name_id = scrapy.Field()


class SportNewsItem(scrapy.Item):

    title = scrapy.Field()
    created_time = scrapy.Field()
    source = scrapy.Field()
    content = scrapy.Field()
    keywords = scrapy.Field()
    url = scrapy.Field()
