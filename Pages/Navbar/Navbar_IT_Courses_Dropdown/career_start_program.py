import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Career_Start_Program(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.CAREER_START_PROGRAM_URL)