import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
sys.path.insert(0,'/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Login')

import allure
from conftest import init_driver
from testdata import Testdata
from test_parent import Parent_test
from basemethods import Base_methods

from login import Login
from test_parent import Parent_test

import pytest

class Test_login(Parent_test):

        # This is for test_registration
    '''def test_signup_link_exists(self):
        self.browser = Login(self.browser)
        visible = self.browser.signup_link_exists()
        assert visible'''


    def test_login(self):
        Base_methods.step_report('step 1: open browser at https://login.training360.com/Account/Login')
        self.browser = Login(self.browser)
        Base_methods.step_report('step 2: verify Login page title match')
        title = self.browser.get_page_title(Testdata.LOGIN_PAGE_TITLE)
        assert title == Testdata.LOGIN_PAGE_TITLE
        # step_report 3, 4, 5 provided on Login page
        self.browser.do_login(Testdata.USERNAME, Testdata.PASSWORD)
        #Base_methods.step_report('step  6: verify logged in: check Bejelentkezve text & provided username is displayed')
        #Base_methods.step_report('step 7: check Kijelentkezés, E-learningtár, Training360 weboldal buttons exist')

    #@pytest.mark.usefixtures('log_wrong_email')
    def test_log_wrong_email(self):
        self.browser = Login(self.browser)
        self.browser.log_wrong_email(Testdata.wrong_email, Testdata.PASSWORD)

    def test_log_empty_inputs(self):
        self.browser = Login(self.browser)
        self.browser.log_empty_inputs(Testdata.empty_input, Testdata.empty_input)

    def test_log_wrong_password(self):
        self.browser = Login(self.browser)
        self.browser.log_wrong_password(Testdata.USERNAME, Testdata.wrong_password)
        

