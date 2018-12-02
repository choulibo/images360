# -*- coding: utf-8 -*-
import scrapy
import json
from images360.items import Images360Item

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']


    def start_requests(self):
        start_url = 'https://image.so.com/zj?ch=photography&sn={}&listtype=new&temp=1'
        url_list = [start_url.format(i*30) for i in range(self.settings.get("MAX_PAGES"))]
        for url in url_list:
            yield scrapy.Request(url,self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = Images360Item()
            item['id'] = image.get('imageid')
            item['imgurl'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item
            print(item)