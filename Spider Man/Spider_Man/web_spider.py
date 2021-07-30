import scrapy
#crapy genspider name website_name
#command for running
#scrapy runspider web_spider.py -o web_spider.json


class WebSpiderSpider(scrapy.Spider):
    name = 'web_spider'
    allowed_domains = ['wikipedia.org']
    start_urls = ['http://wikipedia.org/']
    url = ""

    def parse(self, response):

        i = 0
        res_urls = response.css('a::attr(href)').extract()
        while i < len(res_urls):
            if res_urls[i].startswith("//"):
                res_urls[i] = "https:" + res_urls[i]
            elif not res_urls[i].startswith("//"):
                res_urls[i] = self.url + res_urls[i]
            url = {i: res_urls[i]}
            # closespider_itemcount = 500
            yield url
            self.url = res_urls[i]
            yield scrapy.Request(url=res_urls[i], callback=self.parse)
            i = i + 1

    # name = 'web_spider'
    # allowed_domains = ['wikipedia.org']
    # start_urls = ['http://wikipedia.org/']
    # url = ""
    # i=0
    # def parse(self, response):

    #     #i = 0
    #     res_urls = response.css('a::attr(href)').extract()
    #     while (res_urls[self.i]):
    #         if res_urls[self.i].startswith("//"):
    #             res_urls[self.i] = "https:" + res_urls[self.i]
    #         elif not res_urls[self.i].startswith("//"):
    #             res_urls[self.i] = self.url + res_urls[self.i]
    #         url = {self.i: res_urls[self.i]}
    #         # closespider_itemcount = 500
    #         yield url
    #         self.url = res_urls[self.i]
    #         self.i = self.i + 1
    #         yield scrapy.Request(url=res_urls[self.i-1], callback=self.parse)
