from logging import raiseExceptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException 

#Configs
from testdata import Testdata
from locators import Locators
from basemethods import Base_methods

#Pages
from course_schedules import Course_Schedules
from discounts import Discounts
from contact import Contact
from cart import Cart
from login import Login
#from mainpage_it_courses_dropdown import Mainpage_It_Courses_Dropdown


class MainPage(Base_methods):

    '''Constructor of the Parent class'''
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.URL)
        
        '''Get Titles'''
        # Main Page
    def get_main_page_title(self, title):
        return self.get_title(title)

        # Discounts Page
    def get_discount_page_title(self, title):
        return self.get_title(title)

        # Course_Schedule Page
    def get_course_schedules_page_title(self, title):
        return self.get_title(title)

        # Contact Page
    def get_contacts_page_title(self, title):
        return self.get_title(title)


    '''Page actions'''
    def close_popup(self):
        try:
            self.do_click(Locators.popup_close_btn)

        except TimeoutException:
            print('No popup found.')
            pass


    def search_from_main(self):
        pass


    ''' Units (Elements exist)''' 
    def main_page_button_exists(self):
        assert True
        return self.is_visible(Locators.main_page_button)

    def nav_bar_trainings_exists(self):
        assert True
        return self.is_visible(Locators.nav_bar_trainings)

    def nav_bar_e_learning_exists(self):
        assert True
        return self.is_visible(Locators.nav_bar_e_learning)

    def nav_bar_it_courses_exists(self):
        assert True
        return self.is_visible(Locators.nav_bar_it_courses)

    def nav_bar_course_schedules_exists(self):
        assert True
        return self.is_visible(Locators.nav_bar_course_schedules)

    def nav_bar_discounts_exists(self):
        assert True
        return self.is_visible(Locators.nav_bar_discounts_2)

    def nav_bar_contacts_exists(self):
        assert True
        return self.is_visible(Locators.nav_bar_contacts)

    def nav_bar_cart_exists(self):
        assert True
        return self.is_visible(Locators.nav_bar_cart)

    def nav_bar_login_exists(self):
        assert True
        return self.is_visible(Locators.nav_bar_login)
        

    '''Navigations'''
    '''Navigations from Navbar'''
    # Course Schedules
    def nav_to_course_schedules(self):
        self.do_click(Locators.nav_bar_course_schedules)
        return Course_Schedules(self.browser)

    # Discounts
    def nav_to_discounts(self):
        self.do_click(Locators.nav_bar_discounts)
        #return Discounts(self.browser)
    
    # Contacts
    def nav_to_contacts(self):      
        self.do_click(Locators.nav_bar_contacts)
        #return Contact(self.browser) 

    # Cart
    def nav_to_cart(self):
        self.do_click(Locators.nav_bar_cart)
        #return Cart(self.browser)
    
    # Login
    def nav_to_login(self):
        self.do_click(Locators.nav_bar_login)
        #return Login(self.browser)


    ''' Navigation from Trainings Dropdown Bar'''
    # Click on Trainings Dropdown
    def click_on_trainings_dropdown(self):
        self.do_click(Locators.nav_bar_trainings)

    def nav_to_trainings_open_trainings_schedule(self):
        self.do_click(Locators.nav_bar_trainings)
        pass

    def nav_to_trainings_training_catalogue(self):
        self.do_click(Locators.nav_bar_trainings)
        pass

    # Project Management
    def nav_to_trainings_projectmanagement(self):
        self.do_click(Locators.nav_bar_trainings)
        pass

    def nav_to_trainings_projectmanagement_traditional(self):
        self.do_click(Locators.nav_bar_trainings)
        pass

    def nav_to_trainings_projectmanagement_agile(self):
        self.do_click(Locators.nav_bar_trainings)
        pass

    def nav_to_trainings_projectmanagement_lean(self):
        self.do_click(Locators.nav_bar_trainings)
        pass

    # Soft Skill
    def nav_to_softskill(self):
        self.do_click(Locators.nav_bar_trainings)
        pass
    
    def nav_to_softskill_leader_trainings(self):
        self.do_click(Locators.nav_bar_trainings)
        pass

    def nav_to_softskill_salesforce_trainings(self):
        self.do_click(Locators.nav_bar_trainings)
        pass

    def nav_to_softskill_competence_improvement(self):
        self.do_click(Locators.nav_bar_trainings)
        pass

    def nav_to_softskill_coaching(self):
        self.do_click(Locators.nav_bar_trainings)
        pass


    '''Navigation from IT Courses Dropdown'''
    # IT Courses
    def click_on_it_courses_dropdown(self):
        self.do_click(Locators.nav_bar_it_courses)


    '''Other Navigations from Main Page'''



    '''Footer Navigations (Tests/Navigation)'''
    def nav_to_news(self):
        self.do_click(Locators.nav_bar_news)
        #return News(self.browser)


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass

    '''Elements Exist (For Unit Testing)'''


    '''def nav_to_message_form(self):
        
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/div[1]/div/div[1]/div[2]/button'))

        return Popupobj(self.browser)
        #self.do_click(self.message_btn1)

        button = self.browser.find_element_by_xpath('//*[@id="sendMessage_submit"]')

        ActionChains(self.browser).move_to_element(button).click(button).perform()
        
        
    def fill_data_form(self, name, email, message):
        
        self.do_send_keys(Locators.name_input, name)
        
        self.do_send_keys(self.email_input, email)
        
        self.do_send_keys(self.msg_box_input, message)

        self.do_click(self.ticker)'''
