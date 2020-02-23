from douban.items import DoubanItem
import scrapy
import logging
import numpy as np

class DoubanMovieTop250Spider(scrapy.Spider):
    name = 'douban250'
    start_urls = ['https://movie.douban.com/top250']
    
    def parse(self, response):
        item = DoubanItem()
        movies = response.css("ol.grid_view li")
        for movie in movies:
            item['ranking'] = movie.css(".pic em::text").get()
            item['movie_name'] = movie.css(".hd span.title::text").get()
            item['score'] = float(movie.css(".star span.rating_num::text").get())
            item['score_num'] = movie.css(".star span::text").getall()[1].replace('人评价', '')
            temp_name = movie.css(".bd p::text")[0].get().strip()
            item['director'] = temp_name.split("\xa0\xa0\xa0")[0].split()[1] # only chinese name of the director
            item['year'] = movie.css(".bd p::text")[1].re(r"[0-9]{4}")[0]
            yield item
        
        next_page = response.css("div.paginator span.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)