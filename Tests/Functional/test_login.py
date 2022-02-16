import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

import allure
from allure import attachment_type

from conftest import init_driver
from testdata import Testdata
from login import Login
from test_parent import Parent_test
from mainp_after_login import Mainp_after_login

class Test_login(Parent_test):
    
    def test_loginpage_title(self):
        self.browser = Login(self.browser)
        try:
            title = self.browser.get_page_title(Testdata.LOGIN_PAGE_TITLE)
            assert title == Testdata.LOGIN_PAGE_TITLE


        except:
            screen_shot = 'test_loginpage_title.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_signup_link_visible(self):
        self.browser = Login(self.browser)
        try:
            visible = self.browser.is_signup_link_exist()
            assert visible  


        except:
            screen_shot = 'test_signup_link_visible.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_login(self):
        self.browser = Login(self.browser)
        try:
            self.browser.do_login(Testdata.USERNAME, Testdata.PASSWORD)
            title_after_login = self.browser.get_title_after_login(Testdata.AFTER_LOGIN_PAGE_TITLE)
            assert title_after_login == Testdata.AFTER_LOGIN_PAGE_TITLE


        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    '''def test_check_login_succesful(self):
        self.browser = Mainp_after_login(self.browser)
        
        title_after_login = self.browser.get_title_after_login(Testdata.AFTER_LOGIN_PAGE_TITLE)

        assert title_after_login == Testdata.AFTER_LOGIN_PAGE_TITLE'''
