import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests(SeleniumPython)/Configs')

from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Trainings_Trainings_Open_Trainings_Schedule(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.TRAININGS_OPEN_TRAININGS_SCHEDULE_URL)


    
        ''' Get Title '''
    def get_trainings_trainings_open_trainings_schedule_title(self, title):
        return self.get_title(title)


    ''' Navigations '''
    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")