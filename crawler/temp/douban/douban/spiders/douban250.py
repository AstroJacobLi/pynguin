# -*- coding: utf-8 -*-
import scrapy
import unicodedata
from douban.items import DoubanItem
import logging
import numpy as np

class Douban250Spider(scrapy.Spider):
    name = 'douban250'
    #allowed_domains = ['https://movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        item = DoubanItem()
        movies = response.css('ol.grid_view li')
        for movie in movies:
            item['rank'] = movie.css('div.pic em::text').get()
            
            names = movie.css('div.hd a span::text').getall()
            names = [unicodedata.normalize("NFKD", obj) for obj in names]
            item['chn_name'] = names[0]
            item['other_name'] = "".join(names[1:]).replace('/', '').strip()

            desc = ''.join(movie.css('div.bd').css('p::text').getall())
            desc = unicodedata.normalize("NFKD", desc).strip()
            item['director'] = desc.split('   ')[0].strip('导演: ')
            item['actor'] = desc.split('   ')[1].strip('主演: ').strip('\n')
            ## extract director ###
            item['year'] = movie.css(".bd p::text")[1].re(r"[0-9]{4}")[0]
            item['country'] = desc.split('\n')[1].strip().split('/')[1].strip()
            item['movie_type'] = desc.split('\n')[1].strip().split('/')[2].strip()


            rate = movie.css('div.star').css('span::text').getall()
            item['rating_num'] = rate[0]
            item['rating_ppl'] = rate[1].strip('人评价')

            item['quote'] = movie.css('p.quote span.inq::text').get()
            item['url'] = movie.css('div.hd a::attr(href)').get()
            yield item
        
        next_page = response.css("div.paginator span.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)