import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class Company_Management_Saleforce_Courses(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.COMPANY_MANAGEMENT_SALESFORCE_COURSES_URL)