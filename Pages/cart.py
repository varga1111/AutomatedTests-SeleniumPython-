import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from testdata import Testdata
from locators import Locators
from basemethods import Base_methods

from selenium.webdriver.common.by import By

class Cart(Base_methods):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.CART_URL)


        '''Get Titles'''


        '''Page Actions'''


        ''' Units (Elements exist)''' 


        '''Navigations'''