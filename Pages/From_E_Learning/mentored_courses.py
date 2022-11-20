import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from locators import Locators
from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Mentored_Courses(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.MENTORED_COURSES_URL)


    ''' Get Title '''
    def get_mentored_courses_title(self, title):
        return self.get_title(title)
    

    ''' Navigations '''
    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")