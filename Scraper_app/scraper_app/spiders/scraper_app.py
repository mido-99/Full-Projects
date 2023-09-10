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
        
        for parent in response.css(f'{parent_tag}.{parent_attr_value}'):
            
            for diction in data_list:                
                print(parent.css(
                    f'''{diction['tag']}.{diction['attr_value']}::text''').get()
                    )
                
        
        # for h in response.css('h2.css-m604qf'):
        #     print(h.css('a::text').get())