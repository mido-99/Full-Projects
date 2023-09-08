import scrapy


class Scraper(scrapy.Spider):
    name = 'scraper_app'
    start_urls = ['']