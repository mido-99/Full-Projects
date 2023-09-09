import scrapy
# from empty_tester import url
from globals import main_app_instance


class Scraper(scrapy.Spider):
    name = 'scraper_app'
    # start_urls = [f'{url}']
    start_urls = ['https://wuzzuf.net/search/jobs/?q=python&a=hpb']

    def parse(self, response):
        
        data_list = main_app_instance.get_data()
        for h in response.css('h2.css-m604qf'):
            print(h.css('a::text').get())
        
        print(data_list)
    
    # def scrape_data(self):
    #     for row in data_list:
    #         print (row)

