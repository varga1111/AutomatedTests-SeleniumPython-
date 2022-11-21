import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from conftest import init_driver
#from conftest import failed_check

import allure

from test_parent import Parent_test
from testdata import Testdata
from basemethods import Base_methods

from contact import Contact
from contact_popupobj import Contact_Popupobj


class Test_msg_to_comp(Parent_test):

        # This will be Contact page Unit Test
    '''def test_get_contacts_page_title(self):
        self.browser = Contact(self.browser)
        title = self.browser.get_contacts_page_title(Testdata.CONTACTS_TITLE)
        assert title == Testdata.CONTACTS_TITLE'''
        
    def test_fill_dataform(self):

        def nav_to_message_form(self):
            self.browser = Contact(self.browser)
            self.browser.nav_to_message_form()

        def fill_dataform(self):
            self.browser = Contact_Popupobj(self.browser)
            self.browser.fill_data_form(Testdata.NAME, Testdata.EMAIL, Testdata.MESSAGE)

            
    def test_nav_to_message_form(self):
        self.browser = Contact(self.browser)
        self.browser.nav_to_message_form()

    def test_fill_dataform(self): # This would be send message in real life and would be clicked send and checked in database and in receivers email
        self.browser = Contact_Popupobj(self.browser)
        self.browser.fill_data_form(Testdata.NAME, Testdata.EMAIL, Testdata.MESSAGE)
