import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Discounts(Base_methods):

    '''Locators'''
    main_page_button =(By.XPATH, '//*[@id="navbar"]/div[1]/a/img')

    
    def __init__(self, browser):
        
        super().__init__(browser)
        self.browser.get(Testdata.DISCOUNTS_URL)


    def get_discount_page_title(self, title):
        return self.get_title(title)


    def nav_to_mainpage(self):
        self.do_click(self.main_page_button)
