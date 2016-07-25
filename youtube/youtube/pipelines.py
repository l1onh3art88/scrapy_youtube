# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class YoutubePipeline(ImagesPipeline):
    def set_filename(self,response):
        return '/full/{0}.html'.format(response.meta['title'][0])
        
    def get_media_requests(self,item,info):
        for video_url in item['video_urls']:
            yield scrapy.Request(video_url, meta = {"title": item['title']})
            
    def get_images(self,response,request,info):
        for key, image, buf in super(YoutubePipeline, self).get_images(\
            response,request,info):
            key = self.set_filename(response)
            
        yield key, image, buf
            