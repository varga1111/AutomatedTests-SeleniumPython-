import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from testdata import Testdata
from locators import Locators
from basemethods import Base_methods
from mainp_after_login import Mainp_after_login

from selenium.webdriver.common.by import By
import pytest
import time


@pytest.mark.sanity
class Login(Base_methods):
    
    '''Constructor of the Parent class'''
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.URL_LOGIN)


        '''Get Titles'''
    def get_page_title(self, title):
        return self.get_title(title)


    '''Page actions'''
    def save_screenshot(self, name):
        self.browser.save_screenshot(name)

    # Login
    def do_login(self, username, password):
        Base_methods.step_report('step 3: type username')
        self.do_send_keys(Locators.email, username)

        Base_methods.step_report('step 4: type password')
        self.do_send_keys(Locators.password, password)

        Base_methods.step_report('step 5: click login button')
        self.do_click(Locators.login_button)
        #return Mainp_after_login(self.browser)
        return Login(self.browser)

    #@pytest.fixture
    def log_wrong_email(self, username, password):
        self.do_send_keys(Locators.email, username)
        self.do_send_keys(Locators.password, password)
        self.do_click(Locators.login_button)
        spans = self.browser.find_elements(By.CSS_SELECTOR,'span.text-danger')
        errs = []
        for el in spans:
            if el.is_displayed() == True:
                errs.append(el)
        assert len(errs) == 1

    def log_empty_inputs(self, username, password):
        self.do_send_keys(Locators.email, username)
        self.do_send_keys(Locators.password, password)
        self.do_click(Locators.login_button)
        spans = self.browser.find_elements(By.CSS_SELECTOR,'span.text-danger')
        errs = []
        for el in spans:
            if el.is_displayed() == True:
                errs.append(el)
        assert len(errs) == 2

    def log_wrong_password(self, username, password):
        self.do_send_keys(Locators.email, username)
        self.do_send_keys(Locators.password, password)
        self.do_click(Locators.login_button)
        span1 = self.browser.find_elements(By.CSS_SELECTOR,'div.response__title')
        span2 = self.browser.find_elements(By.CSS_SELECTOR,'div.response__message')
        errs = []
        for el in span1:
            if el.is_displayed() == True:
                errs.append(el)
        for el2 in span2:
            if el2.is_displayed() == True:
                errs.append(el2)
        assert len(errs) == 2




    ''' Units (Elements exist)''' 
    def signup_link_exists(self):
        assert True
        return self.is_visible(Locators.signup_link)


        


    





        


