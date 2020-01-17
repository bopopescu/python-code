# -*- coding: utf-8 -*-
import scrapy
from ..items import DmozItem
class ImoccSpider(scrapy.Spider):
    name = 'imocc'

    allowed_domains = ['www.imooc.com/course/list']
    start_urls=[]
    for i in range(1,21):
        start_urls.append('http://www.imooc.com/course/list/?page=' + str(i))

    def parse(self, response):
        # response.text
        red = response.xpath("//div[@class='course-card-container']")
        item = DmozItem()
        for i in red:
            item['link']='http:'+i.xpath('.//img[@class="course-banner lazy"]/@data-original').get()
            item['title']=i.xpath('.//h3/text()').get()
            item['img']='http://www.imooc.com'+i.xpath('.//a[@class="course-card"]/@href').get()
            # f = open('it.txt', 'a+')
            # items.append(item)
            yield item
        # print(arr)
        # print(arr1)
        # print(arr3)



