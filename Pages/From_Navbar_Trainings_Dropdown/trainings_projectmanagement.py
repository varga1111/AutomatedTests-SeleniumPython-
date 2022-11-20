import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from testdata import Testdata
from locators import Locators
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Trainings_Projectmanagement(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.TRAININGS_PROJECTMANAGEMENT_URL)

    ''' Get Titles '''
    def get_trainings_projectmanagement_title(self, title):
        return self.get_title(title)

    def get_trainings_projectmanagement_agile_title(self, title):
        return self.get_title(title)

    def get_trainings_projectmanagement_traditional_title(self, title):
        return self.get_title(title)

    def get_trainings_projectmanagement_lean_title(self, title):
        return self.get_title(title)


    ''' Units (Elements exist)'''
        # Buttons
    def btn_projectmanagement_traditional_exists(self):
        assert True
        return self.is_visible(Locators.btn_projectmanagement_traditional)

    def btn_projectmanagement_agile_exists(self):
        assert True
        return self.is_visible(Locators.btn_projectmanagement_agile)

    def btn_projectmanagement_lean_exists(self):
        assert True
        return self.is_visible(Locators.btn_projectmanagement_lean)

        # Hyper Links
    def hyper_link_projectmanagement_traditional_exists(self):
        assert True
        return self.is_visible(Locators.hyper_link_projectmanagement_traditional)

    def hyper_link_projectmanagement_agile_exists(self):
        assert True
        return self.is_visible(Locators.hyper_link_projectmanagement_agile)

    def hyper_link_projectmanagement_lean_exists(self):
        assert True
        return self.is_visible(Locators.hyper_link_projectmanagement_lean)

        # Images
    def image_projectmanagement_traditional_exists(self):
        assert True
        return self.is_visible(Locators.image_projectmanagement_traditional)

    def image_projectmanagement_agile_exists(self):
        assert True
        return self.is_visible(Locators.image_projectmanagement_agile)

    def image_projectmanagement_lean_exists(self):
        assert True
        return self.is_visible(Locators.image_projectmanagement_lean)


    ''' Navigations '''
    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")

    def nav_to_projectmanagement_traditional (self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[1]/div/div[2]/div/a'))

    def nav_to_projectmanagement_agile(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/a/i'))

    def nav_to_projectmanagement_lean(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/a'))