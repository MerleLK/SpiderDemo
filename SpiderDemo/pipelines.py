# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class SpiderdemoPipeline(object):

    def __init__(self):
        self._file = codecs.open('news.json', 'w', encoding='utf-8')
        print('Begin to write the news......')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        print(line)
        self._file.write(line)
        return item

    def spider_closed(self, spider):
        self._file.close()
