import scrapy
from scrapy.extensions import closespider

class SpiderManSpider(scrapy.Spider):
    name = 'spider_man'
    allowed_domains = ['wikipedia.org']
    start_urls = ['http://wikipedia.org/']
    
    def parse(self, response):
        i = 0
        res_urls = response.css('a::attr(href)').extract()
        while i < len(res_urls):# or len(res_urls)==0:
            # if len(res_urls)==0:
            #     return 
            if res_urls[i].startswith("//"):
                res_urls[i] = "https:" + res_urls[i]
            elif not res_urls[i].startswith("//"):
                res_urls[i] = self.url + res_urls[i]
            url = {"url": res_urls[i]}
            
            yield url
            self.url = res_urls[i]
            yield scrapy.Request(url=res_urls[i], callback=self.parse)
            i = i + 1