import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from testdata import Testdata
from locators import Locators
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Trainings_Trainings(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.TRAININGS_TRAININGS_URL)


    ''' Get Title '''
    def get_trainings_trainings_title(self, title):
        return self.get_title(title)

    def get_trainings_softskill_title(self, title):
        return self.get_title(title)

    def get_trainings_projectmanagement_title(self, title):
        return self.get_title(title)

    def get_trainings_trainings_open_trainings_schedule_title(self, title):
        return self.get_title(title)

    def get_trainings_trainings_catalogue_title(self, title):
        return self.get_title(title)


    ''' Units (Elements exist)'''
    def btn_softskill_trainings_exists(self):
        return self.is_visible(Locators.btn_soft_skill_trainings)

    def btn_projectmanagement_exists(self):
        return self.is_visible(Locators.btn_projectmanagement)

    def btn_trainings_open_trainings_schedule_exists(self):
        return self.is_visible(Locators.btn_trainings_open_trainings_schedule)

    def btn_trainings_catalogue_exists(self):
        return self.is_visible(Locators.btn_trainings_catalogue)

    def hyper_link_soft_skill_trainings_exists(self):
        return self.is_visible(Locators.hyper_link_soft_skill_trainings)
    
    def hyper_link_projectmanagement_exists(self):
        return self.is_visible(Locators.hyper_link_projectmanagement)

    def hyper_link_trainings_open_trainings_schedule_exists(self):
        return self.is_visible(Locators.hyper_link_trainings_open_trainings_schedule)

    def hyper_link_trainings_catalogue_exists(self):
        return self.is_visible(Locators.hyper_link_trainings_catalogue)

    def image_soft_skill_trainings_exists(self):
        return self.is_visible(Locators.image_soft_skill_trainings)

    def image_projectmanagement_exists(self):
        return self.is_visible(Locators.image_projectmanagement)

    def image_trainings_open_trainings_schedule_exists(self):
        return self.is_visible(Locators.image_trainings_open_trainings_schedule)

    def image_trainings_catalogue_exists(self):
        return self.is_visible(Locators.image_trainings_catalogue)


    ''' Navigations '''
    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")

    def nav_to_softskill_trainings(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[1]/div/div[2]/div/a'))

    def nav_to_projectmanagement(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/a'))

    def nav_to_trainings_open_trainings_schedule(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/a'))

    def nav_to_trainings_catalogue(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[4]/div/div[2]/div/a'))