import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Trainings_Softskill_Competence_Improvement_Trainings(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.TRAININGS_SOFTSKILL_COMPETENCE_IMPROVEMENT_TRAININGS_URL)


    ''' Get Title '''
    def get_trainings_softskill_competence_improvement_trainings_title(self, title):
        return self.get_title(title)


    ''' Navigations '''
    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")