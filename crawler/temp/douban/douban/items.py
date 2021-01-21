# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    chn_name = scrapy.Field()
    other_name = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    year = scrapy.Field()
    country = scrapy.Field()
    movie_type = scrapy.Field()
    rating_num = scrapy.Field()
    rating_ppl = scrapy.Field()
    quote = scrapy.Field()
    url = scrapy.Field()

    
    pass
