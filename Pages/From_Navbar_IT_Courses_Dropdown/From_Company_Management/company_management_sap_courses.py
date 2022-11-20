import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class Company_Management_Sap_Courses(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.COMPANY_MANAGEMENT_SAP_COURSES_URL)