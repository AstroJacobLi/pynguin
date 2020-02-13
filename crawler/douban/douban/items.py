# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TransItem(scrapy.Item):
    name_chn = scrapy.Field()
    name_eng = scrapy.Field()
    kind = scrapy.Field()
    credit = scrapy.Field()
    score = scrapy.Field()
    gpa = scrapy.Field()


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()
    # Director
    director = scrapy.Field()
    # Year of Production
    year = scrapy.Field()
    # URL
    url = scrapy.Field
    pass

class DoubanPersonalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 代号
    alias = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # Director
    director = scrapy.Field()
    # Year of Production
    year = scrapy.Field()
    # URL
    url = scrapy.Field()
    # Date of watching
    date = scrapy.Field()
    # Comment
    comment = scrapy.Field()
    pass
