# Web Crawler

>  Any content that can be viewed on a webpage can be scraped. Period.

## 基础知识

### HTML: HyperText Markup Language 超文本标记语言

详细教程：https://www.w3school.com.cn/html/index.asp

HTML是一种建立网页文件的语言，通过标记式的指令(**Tag**)，将影像、声音、图片、文字动画、影视等内容显示出来。事实上，每一个HTML文档都是一种静态的网页文件，这个文件里面包含了HTML指令代码，这些指令代码并不是一种程序语言，只是一种排版网页中资料显示位置的**标记**结构语言，易学易懂，非常简单。

网页的本质就是超级文本**标记语言**.

例子：欢颜的主页（怕不是要被打死）

例子：http://kiaa.pku.edu.cn/~yuqj/

```
<em>
<i>
<b>
<del>
<li>
```

`<div>`: 定义文档中的分区或节 (division/section), 由于它属于块级元素，浏览器会在其前后显示折行。



### CSS: Cascading Style Sheets 层叠样式表

详细教程：https://www.w3school.com.cn/css/css_jianjie.asp

样式定义如何显示 HTML 元素

当**样式**需要被应用到很多页面的时候，外部样式表将是理想的选择。使用外部样式表，你就可以通过更改一个文件来改变整个站点的外观。

CSS 规则由两个主要的部分构成：选择器，以及一条或多条声明。style写在head里。

```css
h1 {color:red; font-size:14px;}
p {font-family: "sans serif";}
p {
  text-align: center;
  color: black;
  font-family: arial;
}
```



**作业**：把《谈恋爱》的内容制作成一个html网页，不要通篇白底黑字嗷。

##

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