import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class Career_Start_Prog_For_Employers_Guarantee(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.CAREER_START_PROGRAM_FOR_EMPLOYERS_GARENTEES_URL)
    