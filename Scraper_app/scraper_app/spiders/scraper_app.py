import scrapy
from globals import main_app_instance

(url, data_list, parent_tag, parent_attr, 
parent_attr_value) = main_app_instance.get_data()

# Xpath to be used for finding parent elements
parent_Xpath = f'''//{parent_tag}[@{parent_attr}="{parent_attr_value}"]'''    # ex:'//div[@class="css-12345"]'


class Scraper(scrapy.Spider):
    name = 'scraper_app'
    start_urls = [f'{url}']
    # start_urls = ['https://wuzzuf.net/search/jobs/?q=python&a=hpb']

    def parse(self, response):
        
        i = 0
        data_list_len =  len(data_list)
        # data_list is a list of dicts, each dict has info for an item
        # in the parent element

        for parent in response.xpath(parent_Xpath): 
            
            for i in range(data_list_len):    # data_list is a list of dicts, each dict has info for an item in the parent element
                diction = data_list[i]

                if diction['type'] == 'main':
                    
                    item_Xpath =f"""
                            string(.//{diction['tag']}[@{diction['elem_attr']}="{diction['attr_value']}"])
                            """.strip()
                    
                    result = ''.join(parent.xpath(item_Xpath).get())
                    print(result)
                    
                    if not result and i+1 < data_list_len and data_list[i+1]['type'] =='sub':     #*
                        
                        diction = data_list[i+1]
                        item_Xpath =f"""
                                string(.//{diction['tag']}[@{diction['elem_attr']}="{diction['attr_value']}"])
                                """.strip()      #*2
                        
                        result = ''.join(parent.xpath(item_Xpath).get())
                        print(result)
                        i += 1      #*3

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

'''

#* The order of conditions:
NOTE we're checking the existence of i+1 before using it as index to aviod IndexError

#*2 We have to reassign the value of the xpath selector as the variable holds older one

#*3 Note +1 to pass the next list item, that will be a sub_item for surprise.


"""