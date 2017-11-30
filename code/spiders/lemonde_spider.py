'''
Created on 22 nov. 2017

@author: Karudev
'''
from scrapy.spiders import XMLFeedSpider


class LemondeSpider(XMLFeedSpider):
    '''
    classdocs
    '''
    name = 'Le Monde'
    allowed_domains = ['example.com']
    start_urls = ['http://www.lemonde.fr/technologies/rss_full.xml']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        #self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))
        #titles = node.xpath('//item/title/text()').extract_first()
        
        #print(titles)
        
        news = {}
        news['id'] = node.xpath('guid/text()').extract_first()
        news['link'] = node.xpath('link/text()').extract_first()
        news['title'] = node.xpath('title/text()').extract_first()
        news['description'] = node.xpath('description/text()').extract_first()
        news['date'] = node.xpath('pubDate/text()').extract_first()
        news['image'] = node.xpath('enclosure/@url').extract_first()
      
        #yield {'title': node.xpath('title/text()').extract()}
        return news
        
        
        
    
      
     
        
        