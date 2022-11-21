import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from testdata import Testdata
from locators import Locators
from basemethods import Base_methods
from mainp_after_login import Mainp_after_login

from selenium.webdriver.common.by import By
import pytest

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


    ''' Units (Elements exist)''' 
    def signup_link_exists(self):
        assert True
        return self.is_visible(Locators.signup_link)


        


    





        


