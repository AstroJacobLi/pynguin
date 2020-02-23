# Web Crawler 从实战到基础

>  Any content that can be viewed on a webpage can be scraped. Period.



> 版权归作者所有，任何形式转载请联系作者。
> 作者：astrojacobli（来自豆瓣）
> 来源：https://www.douban.com/note/749118764/
>
> 世界就好像一个矛盾结合体，网络世界也不例外。一帮人拥有信息，他们的工作是在展示信息的同时加密信息；另一帮人没有信息，需要信息，所以他们想尽办法抓取和破解信息。
>
> 举个例子：豆瓣拥有用户，用户喜欢电影，于是用户将他们喜欢的电影信息提供给豆瓣，豆瓣收到信息后把这些信息po在网页上。然而有些人好奇某个人看过什么电影，而他能得到的只是那个网页，因此怎么把信息给抓取下来就是个问题（网页的熵显然大于抓取后的信息的熵，因此你需要给这些信息注入能量，这些能量包括但不限于你电脑的电费、你吃的饭还有跟女朋友卖关子时候咽的口水）。
>
> 这个技术就是网络爬虫；但容易想到，在网页发明之前，在信息爆炸之前，没有爬虫这种玩意。所以啊，还是only you can conquer time...
>
> 那这玩意有啥子用呢？就我粗浅的理解，举个例子的话，还是主要跟人相关的问题需要爬虫（因为跟人没关系的事儿也不会po在网站上）。人类的购物偏好是什么？社交网络偏好是什么（这个问题牵扯到图论和图学习）？某个人的观影偏好是什么？云云。
>
> 具体实现起来，道理上讲非常容易：网页是人写的，html格式下载下来，能看见的信息都在文件里，只要把需要的信息取出来就行了。今天带给各位看官的福音是，Python已经有别人开发好的完备工具可以使用，目前最多用的是scrapy。使用起来非常方便，告诉它从哪里开始爬，爬什么内容，如何翻页，保存成什么格式就可以了。但是还是得先知道一点html和css的知识。

爬虫的本质是什么？



## 豆瓣电影 Top250

工具：`scrapy`，命令行工具。

`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scrapy`

网站：https://movie.douban.com/top250

使用帮助：`scrapy -h`



### 1. 新建scrapy项目

`scrapy startproject douban`, 察看文件结构

### 2. 小试牛刀？

`scrapy shell https://movie.douban.com/top250`

`view(response)`

不行？为什么？

>  在HTTP中，User-Agent字符串通常被用於[内容协商](https://zh.wikipedia.org/wiki/内容协商)，而原始服务器为该响应选择适当的内容或操作参数。例如，User-Agent字符串可能被网络服务器用以基于特定版本的客户端软件的已知功能选择适当的变体。
>
> 通过使用[robots.txt](https://zh.wikipedia.org/wiki/Robots.txt)文件的可以設定[网络抓取工具](https://zh.wikipedia.org/w/index.php?title=网络抓取工具&action=edit&redlink=1)對網站的部分訪問與否，而其設定標準之一就是用户代理字符串。換句話說，藉由[robots.txt](https://zh.wikipedia.org/wiki/Robots.txt)文件的設定，可以讓網站不能被特定的瀏覽器訪問。



`settings.py`中：

```py
ROBOTSTXT_OBEY = False
```

```py
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
```

```py
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
```



### 3. 爬虫的本质是什么？（不是复读机）

使用Safari开发者工具：inspect elements，观察之。

本质就是把这些code里的特殊字段识别出来！



### 4. 小试牛刀！

`scrapy shell https://movie.douban.com/top250`

`view(response)`

使用Safari开发者工具：inspect elements，并观察。

这是一个挨个实验的过程！！！千万不要以为一次可以写好！

```python
movie = response.css('ol.grid_view li')[0] # Selector

movie.css('div.item').getall()

movie.css('div.item div.pic a').attrib['href']

movie.css('div.item div.hd a').attrib['href']

movie.css('div.item div.hd span.title').getall()
movie.css('div.item div.hd span.title::text')
movie.css('div.item div.hd span.title::text').getall()

movie.css('div.item div.bd p::text').getall()
movie.css('div.item div.bd div.star span.rating_num::text').getall()
movie.css('div.item div.bd div.star span::text').getall()

movie.css('.bd p.quote::text').getall()
movie.css('.bd p.quote ::text').getall()
movie.css('.bd p.quote span.inq::text').getall()
movie.css('.bd p.quote span.inq::text').get()
```



现在我们明白了怎么信息藏在网页何处，但是如何处理这些信息呢？如何把他们弄得更整洁？

举个🌰！

```python
name_list = movie.css('div.item div.hd span.title::text').getall()
chn_name = name_list[0]
eng_name = name_list[1].strip('\xa0/\xa0')

score_num = movie.css('div.item div.bd div.star span::text').getall()[1].strip('人评价')

quote = movie.css('div.item div.bd p.quote span.inq::text').get()
```

请完成剩下的 (不会的留着😛)：

```python
ranking =  # 排第几名
score = # 评分
director = # 导演是谁
year = # 哪年的电影
url = # 电影的链接
```

下课休息30min



### 5. 批量生产

- 建立items

  在item.py里：

  ```python
  class DoubanItem(scrapy.Item):
      # define the fields for your item here like:
      # name = scrapy.Field()
      # 排名
      ranking = scrapy.Field()
      # 电影名称
      chn_name = scrapy.Field()
      eng_name = scrapy.Field()
      # 评分
      score = scrapy.Field()
      # 评论人数
      score_num = scrapy.Field()
      # Director
      director = scrapy.Field()
      # Year of Production
      year = scrapy.Field()
      # URL
      url = scrapy.Field()
      # Quote
      quote = scrapy.Field()
      pass
    
  ```

- 建立spider

  `cd douban/spider`

  `touch douban_spider.py`

  ```python
  from douban.items import DoubanItem
  import scrapy
  import logging
  import numpy as np
  
  # spider class
  class DoubanMovieTop250Spider(scrapy.Spider):
      name = 'douban250' # name of this spider
      start_urls = ['https://movie.douban.com/top250']
      
      def parse(self, response):
          item = DoubanItem()
          movies = response.css("ol.grid_view li")
          for movie in movies:
            	## 
              item['score'] = float(movie.css(".star span.rating_num::text").get())
              ##
              yield item
          ## 翻页！
          next_page = response.css("div.paginator span.next a::attr(href)").get()
          if next_page is not None:
              yield response.follow(next_page, callback=self.parse)
  ```

- 让spider爬！

  退出到最初的douban文件夹

  `scrapy crawl douban250 -o douban_movie.csv`

- 在pandas里读取文件

  `pd.read_csv('douban_movie.csv')`

  









## 爬虫



https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/



XPath:

https://www.w3.org/TR/xpath/all/

https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors

http://zvon.org/comp/r/tut-XPath_1.html

http://plasmasturm.org/log/xpath101/



Scrapy on notebook: https://www.jitsejan.com/using-scrapy-in-jupyter-notebook.html



https://monkeylearn.com/blog/filtering-startup-news-machine-learning/



Exercise: [Regular Expression](https://github.com/ziishaned/learn-regex)



Awesone-spider: https://github.com/facert/awesome-spider

有趣的Python爬虫和数据分析小项目: https://github.com/Alfred1984/interesting-python

Python入门网络爬虫之精华版: https://github.com/lining0806/PythonSpiderNotes