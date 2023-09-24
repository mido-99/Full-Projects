# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re


class ScraperAppPipeline:
    def process_item(self, item, spider):
        
        self.apply_regex(item)
        item = self.filter_columns(item)
        
        return item
    
    def apply_regex(self, item):
        """Apply regex to scraped item"""
        
        regex_setting = item['regex']
        
        if regex_setting:
            pattern, repl = regex_setting
            item['data'] = re.sub(pattern, repl, item['data'])
        
        # print(item['data'], item['column'])
        return item
    
    def filter_columns(self, item):
        '''Filters out unwanted columns in final exported file'''
        
        kept_keys = set(item.keys()) - {'regex'}
        return {key: item[key] for key in kept_keys}