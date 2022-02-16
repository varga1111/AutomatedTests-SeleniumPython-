import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from conftest import init_driver

import allure

from testdata import Testdata
from contact import Contact
from contact_popupobj import Contact_Popupobj
from test_parent import Parent_test


class Test_msg_to_comp(Parent_test):

    def test_get_contacts_page_title(self):
        self.browser = Contact(self.browser)
        try:
            title = self.browser.get_contacts_page_title(Testdata.CONTACTS_TITLE)
            assert title == Testdata.CONTACTS_TITLE
        

        except:
            screen_shot = 'test_get_contacts_page_title.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_nav_to_message_form(self):
        self.browser = Contact(self.browser)
        try:
            self.browser.nav_to_message_form()


        except:
            screen_shot = 'test_nav_to_message_form.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_fill_dataform(self):
        self.browser = Contact_Popupobj(self.browser)
        try:
            self.browser.fill_data_form(Testdata.NAME, Testdata.EMAIL, Testdata.MESSAGE)


        except:
            screen_shot = 'test_fill_dataform.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False