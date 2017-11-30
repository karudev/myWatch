'''
Created on 22 nov. 2017

@author: Karudev
'''
import scrapy

class BoursoramaSpider(scrapy.Spider):
    '''
    classdocs
    '''

    name = "Boursorama"
    start_urls = [
        'http://www.boursorama.com/',
    ]
        
     
    def parse(self, response):

       
        dict = {
            'title' : response.css('title::text').extract_first(),
            'top_funds': response.css('.bourse ul.accordion li.accordion-element a::text').extract(),
            'pts' : response.css('.bourse ul.accordion li.accordion-element span::text').extract() 
                          
                          
            }
        
        print(dict)
        
        
        
    
      
     
        
        