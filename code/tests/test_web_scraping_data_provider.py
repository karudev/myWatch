'''
Created on 22 nov. 2017

@author: Karudev
'''
from data_provider.web_scraping_data_provider import WebScrapingDataProvider
import unittest


class TestWebScrapingDataProvider(unittest.TestCase):


    def setUp(self):
        
        self.web_scraping_data_provider = WebScrapingDataProvider('Karudev Website',['http://karudev.fr'])
        


    def tearDown(self):
        pass

    
    
    def test_parse(self):
        self.assertEqual("Karudev", self.web_scraping_data_provider.title)
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()