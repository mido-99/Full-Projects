# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re


class ScraperAppPipeline:
    def process_item(self, item, spider):   #*
        
        self.apply_regex(item)
        item = self.filter_columns(item)
        
        return item
    
    def apply_regex(self, item):
        """Apply regex to scraped item"""
        
        regex_setting = item['regex']
        if regex_setting:
            pattern, repl = regex_setting
            column = item['column']
            item[column] = re.sub(pattern, repl, item[column])
        return item
    
    def filter_columns(self, item):
        '''Filters out unwanted columns in final exported file'''
        
        Unwanted_keys = {'regex', 'column'}
        kept_keys = set(item.keys()) - Unwanted_keys
        return {key: item[key] for key in kept_keys}
        # return {key: item[key] for key in item if key not in Unwanted_keys}

"""
#* Item is a dict-like object, representing current yielded keys and values pairs.
So it's literally an 'item' of a dict. thus values of keys can be accessed in current
file, and processed by the pipeLines in order

NOTE: order of pipelines is set in settings.py file; so that ones with lower numbers
are the first to be executed.

"""