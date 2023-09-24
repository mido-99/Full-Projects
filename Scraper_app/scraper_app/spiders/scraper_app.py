import scrapy
from globals import main_app_instance


(url, data_list, parent_tag, parent_attr, 
parent_attr_value) = main_app_instance.get_data()
data_list_len =  len(data_list) # list of dicts, each dict has info for an item in the parent element


class Scraper(scrapy.Spider):
    name = 'scraper_app'
    start_urls = [f'{url}']
    # start_urls = ['https://wuzzuf.net/search/jobs/?q=python&a=hpb']

    def parse(self, response):
        """fetches items in parents elements according to xpath selectors constructed
        by user input. Tries to get the main item first, if failed or None sub item 
        will be used"""

        for parent in self.parse_parents(response):
            
            for i, selector in enumerate(self.generate_selectors()):
                
                result = ''.join(parent.xpath(selector['main']).get()).strip()
                column = f'{data_list[i].get("column")}'

                if 'sub' in selector and not result:   # if there's a sub selector for current item
                    result = ''.join(parent.xpath(selector['sub']).get())
                    regex_tuple = data_list[i+1].get('regex', None)
                    
                else:
                    regex_tuple = data_list[i].get('regex', None)
                
                yield {
                    column : result,
                    'regex': regex_tuple,
                }
    
    def generate_selectors(self):
        """Generator: It passes selectors directly to default parse method. 
        Selectors are passed as dictionary; with the keys: 'main' or 'sub' for main
        item and sub item respectively."""

        i = 0
        while i < data_list_len:# data_list is a list of dicts, each dict has info for an item in the parent element
            diction = data_list[i]
            next_diction = data_list[i + 1] if i + 1 < data_list_len else None
            
            selector = {}

            if diction['type'] == 'main' and next_diction and  next_diction['type'] == 'sub':   #*
                
                selector['sub'] = self.construct_xpath(next_diction)
                i += 1      #*2

            selector['main'] = self.construct_xpath(diction)
            i += 1
            
            yield selector
    
    def parse_parents(self, response):
        """Fetch parent elements from which children items will be scraped""" 
        
        parent_Xpath = f'''//{parent_tag}[@{parent_attr}="{parent_attr_value}"]'''    # ex:'//div[@class="css-12345"]'
        return response.xpath(parent_Xpath)
    
    @staticmethod
    def construct_xpath(diction):
        """Construct xpath string for selectors according to user input"""

        return f'''string(.//{diction['tag']}[@{diction['elem_attr']}="{diction['attr_value']}"])'''
        
        


"""
'''
# Tests:
link:
https://wuzzuf.net/search/jobs/?q=python&a=hpb
big div:
css-pkv5jc
a:
css-o171kl
location span:
css-5wys0k

price in Diff divs site:
https://www.theperfumeshop.com/marc-jacobs/b/50/womens-fragrances/perfect/bc/marcJacobsPerfect?query=:ranking
div:
product-list-item__info
price:
price__current
discount:
discounted-price__price-current
example discount:
Only £81.00 
'''

#* The order of conditions:
NOTE we're checking the existence of i+1 before using it as index to aviod IndexError

#*2 Note +1 to pass the next list item, that will be a sub_item for surprise.

"""