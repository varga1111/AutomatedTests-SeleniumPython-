import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests(SeleniumPython)/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class It_Courses_Admin_Other(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.IT_COURSES_ADMIN_OTHER_URL)