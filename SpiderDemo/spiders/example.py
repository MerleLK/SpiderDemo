import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from SpiderDemo.items import SpiderdemoItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['x23us.com']
    start_url = 'http://www.x23us.com/class/'
    bash_url = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.start_url + str(i) + '_1' + self.bash_url
            yield Request(url, self.parse)

    def parse(self, response):
        max_num = BeautifulSoup(
            response.text, 'lxml').find_all('div', class_='pagelink')[0].find_all('a')[-1].get_text()
        bash_url = str(response.url)[:-7]
        for num in range(1, int(max_num)+1):
            sim_url = bash_url + '_' + str(num) + self.bash_url
            yield Request(sim_url, callback=self.get_name)

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        category = BeautifulSoup(response.text, 'lxml').find('div', class_='bdsub').find('dt').get_text(
        ).split('-')[0].strip()
        for td in tds:
            novel_name = td.find_all('a')[1].get_text()
            novel_url = td.find_all('a')[1]['href']
            print(novel_url)
            author = td.find_all('td', class_='C')[0].get_text()
            yield Request(novel_url, callback=self.get_chapter_url, meta={
                'name': novel_name, 'url': novel_url, 'category': category, 'author': author})

    def get_chapter_url(self, response):
        item = SpiderdemoItem()
        item['name_id'] = str(response.url)[-8:-1].replace('/', '')
        item['name'] = str(response.meta['name'])
        item['novel_url'] = response.meta['url']
        category = response.meta['category']
        author = response.meta['author']
        item['category'] = str(category).replace('/', '')
        item['author'] = str(author).replace('/', '')
        return item
