import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from SpiderDemo.items import SportNewsItem


class SportNewsSpider(scrapy.Spider):
    """
        get the http://sports.sina.com.cn/ news main content.
    """
    name = 'sport_news'
    allowed_domains = ['sina.com.cn']
    start_url = 'http://sports.sina.com.cn/'
    bash_url = '.shtml'

    def start_requests(self):
        urls = ['http://sports.sina.com.cn/nba/1.shtml', 'http://sports.sina.com.cn/nba/5.shtml']
        for url in urls:
            yield Request(url, self.parse)

    def parse(self, response):
        sub_news = BeautifulSoup(response.text, 'lxml').find_all('div', id='right')
        links = sub_news[0].find_all('div')[0].find_all('a')
        for tag in links:
            sub_url = str(tag.get('href'))
            if sub_url:
                yield Request(sub_url, self.get_new_content)

    def get_new_content(self, response):
        main_new = BeautifulSoup(response.text, 'lxml')
        content = ''
        for p in main_new.find('div', class_='article-a__content').find_all('p'):
            content += p.get_text()

        keywords = ''
        for k in main_new.find('section', class_='article-a_keywords').find_all('a'):
            keywords += ' ' + k.get_text()
        item = SportNewsItem()
        item['title'] = str(main_new.find('title').text)
        item['url'] = response.url
        item['content'] = content
        item['created_time'] = main_new.find('span', class_='article-a__time').get_text()
        item['source'] = main_new.find('span', class_='article-a__source').get_text()
        return item
