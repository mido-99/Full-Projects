import scrapy
# from empty_tester import url
from globals import main_app_instance

(url, data_list, parent_tag, parent_attr, 
parent_attr_value) = main_app_instance.get_data()

class Scraper(scrapy.Spider):
    name = 'scraper_app'
    start_urls = [f'{url}']
    # start_urls = ['https://wuzzuf.net/search/jobs/?q=python&a=hpb']

    def parse(self, response):
        
        for parent in response.xpath(
            f'''//{parent_tag}[@{parent_attr}="{parent_attr_value}"]'''     # ex: '//div[@class="css-12345"]'
            ):
        
            for diction in data_list:   # data_list is a list of dicts, each dict has info for an item in the parent element
                print(''.join(
                    parent.xpath(
                    f'''//./{diction['tag']}[@{diction['elem_attr']}="{diction['attr_value']}"]/text()''').getall()
                    ))
                
        
        # for h in response.css('h2.css-m604qf'):
        #     print(h.css('a::text').get())

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

'''