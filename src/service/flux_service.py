
from lxml import etree
import pprint

class FluxService:
    
    
    def __init__(self, file):
        
        self.file = file
   
    
    def get_data(self, propertyPath):
        
        tree = etree.parse(self.file)
        
        for index,property in enumerate(tree.xpath(propertyPath)):
            print("{0}.{1} \n".format((index+1),property.text))
    
            
    def parseXML(self, item):

        context = etree.iterparse(self.file)
        for action, elem in context:
            if not elem.text:
                text = "None"
            else:
                if elem.tag != item:
                    print("{0} => {1}".format(elem.tag,elem.text))
                    #print(elem.tag + " => " + text)   
        