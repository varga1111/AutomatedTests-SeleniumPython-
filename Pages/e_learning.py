import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from testdata import Testdata
from locators import Locators
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class E_Learning(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.E_LEARNING_URL)


        ''' Get Titles'''
    def get_e_learning_title(self, title):
        return self.get_title(title)

    def get_e_learning_owndev_title(self, title):
        return self.get_title(title)

    def get_e_learning_official_title(self, title):
        return self.get_title(title)

    def get_mentored_courses_title(self, title):
        return self.get_title(title)

    def get_e_learning_unique_title(self, title):
        return self.get_title(title)


    '''Page actions'''


    ''' Units (Elements exist)''' 
    def hyper_link_owndev_exists(self):
        assert True
        return self.is_visible(Locators.hyper_link_owndev)

    def hyper_link_e_learning_lessons_exists(self):
        assert True
        return self.is_visible(Locators.hyper_link_e_learning_lessons)

    def hyper_link_official_exists(self):
        assert True
        return self.is_visible(Locators.hyper_link_official)

    def hyper_link_mentored_exists(self):
        assert True
        return self.is_visible(Locators.hyper_link_mentored)
    
    def hyper_link_unique_exists(self):
        assert True
        #assert True
        return self.is_visible(Locators.btn_it_courses_dev)

    def hyper_link_e_learning_lessons_exists(self):
        #assert True
        return self.is_visible(Locators.hyper_link_e_learning_lessons)

    def hyper_link_official_exists(self):
        #assert True
        return self.is_visible(Locators.hyper_link_official)

    def hyper_link_mentored_exists(self):
        #assert True
        return self.is_visible(Locators.hyper_link_mentored)
    
    def hyper_link_unique_exists(self):
        #assert True
        return self.is_visible(Locators.hyper_link_unique)


    '''Navigations'''
    def nav_to_elearning_owndev(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[2]/a[1]'))
    
    def nav_to_e_learning_lessons(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[2]/a[2]'))

    def nav_to_e_learning_official(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[4]/a'))

    def nav_to_mentored_courses(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[6]/a'))

    def nav_to_e_learning_unique(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[8]/a'))

    




#self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('//*[@id="sendMessage_submit"]'))
    