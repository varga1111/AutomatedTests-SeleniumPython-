import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from testdata import Testdata
from locators import Locators
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Course_Schedules(Base_methods):

    def __init__(self, browser):    
        super().__init__(browser)
        self.browser.get(Testdata.COURSE_SCHEDULES_URL)


        '''Get Titles'''
    def get_course_schedules_page_title(self, title):
        return self.get_title(title)


    '''Page actions'''
    def save_screenshot(self, name):
        self.browser.save_screenshot(name)


    ''' Units (Elements exist)''' 


    '''Navigations'''
    def nav_to_mainpage(self):
        self.do_click(Locators.main_page_button)


