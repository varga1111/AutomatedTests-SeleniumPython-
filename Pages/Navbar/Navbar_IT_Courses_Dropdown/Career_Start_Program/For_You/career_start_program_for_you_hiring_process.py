import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class Career_Start_Prog_For_You_Hiring_Process(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.CAREER_START_PROGRAM_FOR_YOU_HIRING_PROCESS_URL)