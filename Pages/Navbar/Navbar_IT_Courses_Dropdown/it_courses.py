import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class It_Courses(Base_methods):
    
    ''' By Locators'''
    btn_it_courses = (By.ID, 'PrimaryNavCourses')
    

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.IT_COURSES_URL)

    ''' Elements Exist '''

    ''' Navigations '''
    