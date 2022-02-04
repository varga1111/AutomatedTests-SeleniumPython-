import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class Office_It_Microsoft_Office(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.OFFICE_IT_MICROSOFT_OFFICE_URL)