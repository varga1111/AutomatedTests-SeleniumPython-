import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from locators import Locators
from basemethods import Base_methods

from selenium.webdriver.common.by import By

class Contact_Popupobj(Base_methods):

    def __init__(self, browser): 
        super().__init__(browser)

    
    def fill_data_form(self, name, email, message):
        self.do_send_keys(Locators.name_input, name)
        self.do_send_keys(Locators.email_input, email)
        self.do_send_keys(Locators.msg_box_input, message)
        self.do_click(Locators.ticker)

    
    def submit_message(self):
        self.do_click(Locators.message_btn1)

        