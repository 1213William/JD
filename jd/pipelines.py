# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.item import Item
from scrapy.exceptions import DropItem


class JdPipeline(object):
    def process_item(self, item, spider):
        print(item['title'], item['url'])
        return item


class MongoDBPipeline(object):
    DB_URL = 'mongodb://localhost:27017/'
    DB_NAME = 'jd_data'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item, Item) else item
        collection.insert(post)
        return item


class DuplicatesPipeline(object):
    def __init__(self):
        self.shop_set = set()

    def process_item(self, item, spider):
        # 这个是店铺的名字
        name = item['title']
        if name in self.shop_set:
            # 如果这家店铺已经在set集合中了就说明已经存在了
            raise DropItem('这家店铺已经存在了...')
        # 如果没有被上面的异常打断的话就说明不存在就要添加到集合里面去
        self.shop_set.add(name)
        return item

