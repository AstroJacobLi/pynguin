from douban.items import DoubanItem, DoubanPersonalItem, TransItem
import scrapy
import logging
import numpy as np

# spider class
class Transcript(scrapy.Spider):
    name = 'transcript'
    start_urls = ['http://astrojacobli.github.io/meander']
    custom_settings = {
        'LOG_LEVEL': logging.DEBUG,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    
    def parse(self, response):
        item = TransItem()
        table = response.css('table.row-border-table tr.ng-scope')
        for course in table:
            data = course.css('td::text').getall()
            item['name_chn'] = data[0]
            item['name_eng'] = data[1]
            item['kind'] = data[2]
            item['credit'] = data[3]
            item['score'] = data[4]
            if data[4] == 'W':
                item['gpa'] = np.nan
            else:
                item['gpa'] = data[5]
            yield item
            

# spider class
class DoubanMovieTop250Spider(scrapy.Spider):
    name = 'douban250'
    start_urls = ['https://movie.douban.com/top250']
    custom_settings = {
        'LOG_LEVEL': logging.DEBUG,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    
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
            

            #item['movie_name'] = {'CHN': temp_name[0], 'ENG': temp_name[1].replace(u'\xa0/\xa0', u' ').strip()}
            #temp_name = movie.css(".bd p::text")[0].re(r"导演: (\w+.\w+)\s(\w+.\w+)")
            #item['director'] = {'CHN': temp_name[0], 'ENG': temp_name[1]}
            
            
# spider class
class DoubanPerson(scrapy.Spider):
    name = 'douban_person'
    def __init__(self, person_id):
        self.id = person_id
        self.start_urls = ['https://movie.douban.com/people/{}/collect'.format(self.id)]
        super().__init__()
    
    custom_settings = {
            'LOG_LEVEL': logging.DEBUG,
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        }
    
    def parse(self, response):
        item = DoubanPersonalItem()
        movies = response.css("div.grid-view div.item")
        for movie in movies:
            item['movie_name'] = movie.css(".title a em::text").get().split(" / ")[0]
            item['alias'] = movie.css("a").attrib['title']
            item['url'] = movie.css("a").attrib['href']
            item['date'] = movie.css(".date::text").get()
            for num in range(1, 6):
                if movie.css("span.rating{}-t".format(num)).get():
                    item['score'] = num
            try:
                item['year'] = movie.css(".intro::text").re(r"[0-9]{4}")[0]
            except:
                item['year'] = "0000"
            item['comment'] = movie.css(".comment::text").get()
            yield item
        
        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            