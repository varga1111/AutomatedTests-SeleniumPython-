import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from locators import Locators
from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class E_Learning_Owndev_Office(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.E_LEARNING_OWNDEV_OFFICE_URL)