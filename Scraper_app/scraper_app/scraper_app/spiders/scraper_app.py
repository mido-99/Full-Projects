import scrapy
from scrapy.crawler import CrawlerProcess
from shared_data import url, data_list, START


class Scraper(scrapy.Spider):
    name = 'scraper_app'
    start_urls = [f'{url}']
    
    def parse(self):
        pass
    
    def scrape_data(self):
        for row in data_list:
            print (row)

    # process = CrawlerProcess()
    # process.crawl(Scraper)
    # process.start()