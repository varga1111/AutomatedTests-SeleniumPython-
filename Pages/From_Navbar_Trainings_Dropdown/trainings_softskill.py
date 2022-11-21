import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from testdata import Testdata
from locators import Locators
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Trainings_Softskill(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.TRAININGS_SOFTSKILL_URL)


    ''' Get Titles '''
    def get_trainings_softskill_title(self, title):
        return self.get_title(title)

    def get_trainings_softskill_leader_trainings_title(self, title):
        return self.get_title(title)
    
    def get_trainings_softskill_salesforce_trainings_title(self, title):
        return self.get_title(title)
    
    def get_trainings_softskill_competence_improvement_trainings_title(self, title):
        return self.get_title(title)

    def get_trainings_softskill_coaching_title(self, title):
        return self.get_title(title)


    ''' Units (Elements exist)'''
    def btn_leader_trainings_exists(self):
        assert True
        return self.is_visible(Locators.btn_leader_trainings)

    def btn_salesforce_trainings_exists(self):
        assert True
        return self.is_visible(Locators.btn_salesforce_trainings)

    def btn_competence_improvement_trainings_exists(self):
        assert True
        return self.is_visible(Locators.btn_competence_improvement_trainings)

    def btn_coaching_exists(self):
        assert True
        return self.is_visible(Locators.btn_coaching)
        

    ''' Navigations '''
    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")

    def nav_to_leader_trainings(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[1]/div/div[2]/div/a'))

    def nav_to_salesforce_trainings(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/a'))

    def nav_to_competence_improvement_trainings(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/a'))

    def nav_to_coaching(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[4]/div/div[2]/div/a'))