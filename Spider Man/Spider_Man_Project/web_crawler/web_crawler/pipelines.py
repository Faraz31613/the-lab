# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import json
import scrapy
from itemadapter import ItemAdapter
from urllib.parse import quote


class WebCrawlerPipeline:
    def open_spider(self, spider):
        self.file = open('spider_man.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
    # async def process_item(self, item, spider):
    #     adapter = ItemAdapter(item)
    #     encoded_item_url = quote(adapter["url"])
    #     screenshot_url = self.SPLASH_URL.format(encoded_item_url)
    #     request = scrapy.Request(screenshot_url)
    #     response = await spider.crawler.engine.download(request, spider)
    #     return item