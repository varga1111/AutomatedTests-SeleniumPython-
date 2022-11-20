import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown/Trainings_Trainings')

from conftest import init_driver
#from conftest import failed_check

import allure

from testdata import Testdata
from test_parent import Parent_test
from basemethods import Base_methods

from trainings_trainings import Trainings_Trainings
from trainings_softskill import Trainings_Softskill
from trainings_projectmanagement import Trainings_Projectmanagement
from trainings_trainings_open_trainings_schedule import Trainings_Trainings_Open_Trainings_Schedule
from trainings_trainings_catalogue import Trainings_Trainings_Catalogue


class Test_Nav_Trainings_Trainings(Parent_test):
    
    def test_get_trainings_trainings_title(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek')
        self.browser = Trainings_Trainings(self.browser)
        Base_methods.step_report('step 2: verify Trainings_Trainings page title')
        title = self.browser.get_trainings_trainings_title(Testdata.TRAININGS_TRAININGS_TITLE)
        assert title == Testdata.TRAININGS_TRAININGS_TITLE


    ''' Test Units (Elements exist)'''
    def test_btn_soft_skill_trainings_exists(self):
        self.browser = Trainings_Trainings(self.browser)
        self.browser.btn_softskill_trainings_exists()

    def test_btn_projectmanagement_exists(self):
        self.browser = Trainings_Trainings(self.browser)
        self.browser.btn_projectmanagement_exists()

    def test_btn_trainings_open_trainings_schedule_exists(self):
        self.browser = Trainings_Trainings(self.browser)
        self.browser.btn_trainings_open_trainings_schedule_exists()

    def test_btn_trainings_catalogue_exists(self):
        self.browser = Trainings_Trainings(self.browser)
        self.browser.btn_trainings_catalogue_exists()