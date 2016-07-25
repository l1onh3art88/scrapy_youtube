# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoutubeItem(scrapy.Item):
    title = scrapy.Field()
    embed = scrapy.Field()
    video_urls = scrapy.Field()
    
    