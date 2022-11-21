from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
<<<<<<< HEAD
import requests
=======
>>>>>>> b51427b22454e28c659cb0d0dd9fe07580f0fbf5
import allure

from testdata import Testdata


'''This class is the parent of all pages.'''
'''It contains all the generic methods and utilities for all pages.'''
class Base_methods(Testdata):

    def __init__(self, browser):
        self.browser = browser
        self.browser.maximize_window()


        # Check Title
    def get_title(self, title):
        wait(self.browser, 10).until(EC.title_is(title))
        return self.browser.title


         # Click
    def do_click(self, by_locator):
         wait(self.browser, 20).until(EC.element_to_be_clickable(by_locator)).click()


        #Type
    def do_send_keys(self, by_locator, text):
<<<<<<< HEAD
        wait(self.browser, 10).until(EC.element_to_be_clickable(by_locator)).send_keys(text)

=======
        wait(self.browser, 10).until(EC.presence_of_element_located(by_locator)).send_keys(text)
        
>>>>>>> b51427b22454e28c659cb0d0dd9fe07580f0fbf5

        # Hover (ex.: dropdown menus)
    def hover(self, element):
        actions = ActionChains(self.browser)
        actions.move_to_element(element)
        actions.perform()


        # Check visibility of element
    def is_visible(self, by_locator):
        element = wait(self.browser, 10).until(EC.element_to_be_clickable(by_locator))
<<<<<<< HEAD
        return bool(element)
=======
        return bool(element) # or element.is_displayed() --> returns bool and verifies the element is on the screen not just xml, but the expected condition in this instance already verifies that
>>>>>>> b51427b22454e28c659cb0d0dd9fe07580f0fbf5


        # Save screenshot (can't call the function in tests if not pre-defined)
    def save_screenshot(self, name):
        self.browser.save_screenshot(name)

        # Displaying test steps in allure when called
    def step_report(step_title):
        with allure.step(step_title):
            pass

    
    '''def go_back(self):
        self.browser.execute_script("window.history.go(-1)")'''
    
    '''def execute_script(self, by_locator):
        wait(self.browser, 10).until(EC.presence_of_element_located(by_locator))
        self.browser.execute_script('arguments[0].click();' , by_locator)'''


    '''def get_element_text(self, by_locator):
        element = wait(self.browser, 10).until(EC.presence_of_element_located(by_locator))
        
        return element.text'''