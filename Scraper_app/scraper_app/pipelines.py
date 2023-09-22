# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re


class ScraperAppPipeline:
    def process_item(self, item, spider):
        
        self.replace_text(item)
        
        return item
    
    def replace_text(self, item):
        """Replace text in scraped data with new text"""
        
        replace_setting = item['replace']
        
        if replace_setting:
            pattern, repl = replace_setting
            item['data'] = re.sub(pattern, repl, item['data'])
        
        print(item['data'])        
        return item