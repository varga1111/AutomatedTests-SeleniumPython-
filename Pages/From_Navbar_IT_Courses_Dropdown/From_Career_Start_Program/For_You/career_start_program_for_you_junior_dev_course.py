import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class Career_Start_Prog_For_You_Junior_Dev(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.CAREER_START_PROGRAM_FOR_YOU_JUNIOR_DEV_COURSE_URL)