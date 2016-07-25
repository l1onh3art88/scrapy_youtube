import scrapy

from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from youtube.items import YoutubeItem

class YoutubeSpider(CrawlSpider):
    name = 'youtube'
    allowed_domains = ['youtube.com']
    start_urls = ['http://www.youtube.com']

    
    # def parse_dir_contents(self, response):
    #     for href in response.css("iv.content >div.yt-lockup-dismissable> div.yt-lockup-content>h3> a::attr('href')"):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request("http://www.youtube.com/" + url, callback=self.parse_dir_contents)
            
    
    def parse_youtube(self,response):
        video = YoutubeItem()
        video['title'] = response.path("//h3/a/@title/text()").extract()
        rel = response.xpath("//h3/a/@href/text()").extract()
        video['video_urls'] = ['http:' + rel[0]]
        return video
