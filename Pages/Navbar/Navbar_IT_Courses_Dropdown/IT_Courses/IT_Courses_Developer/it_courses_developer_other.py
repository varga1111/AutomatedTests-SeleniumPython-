import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class It_Courses_Developer_Other(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.IT_COURSES_DEVELOPER_OTHER_URL)