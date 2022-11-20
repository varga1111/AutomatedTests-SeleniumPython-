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
    
    ''' Test Navigations'''
        # Trainings Dropdown
        # Navigate to Projectmanagement/Traditional Page
    def test_nav_to_softskill_trainings(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek')
        self.browser = Trainings_Trainings(self.browser)
        Base_methods.step_report('step 2: navigate to Softskill_trainings page')
        self.browser.nav_to_softskill_trainings()
        Base_methods.step_report('step 3: verify Softskill_trainings page title')
        title = self.browser.get_trainings_softskill_title(Testdata.TRAININGS_SOFTSKILL_TITLE)
        assert title == Testdata.TRAININGS_SOFTSKILL_TITLE

        # Navigate to Projectmanagement/Agile Page
    def test_nav_to_projectmanagement(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek')
        self.browser = Trainings_Trainings(self.browser)
        Base_methods.step_report('step 2: navigate to Projectmanagement page')
        self.browser.nav_to_projectmanagement()
        Base_methods.step_report('step 3: verify Projectmanagement page title')
        title = self.browser.get_trainings_projectmanagement_title(Testdata.TRAININGS_PROJECTMANAGEMENT_TITLE)
        assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_TITLE

        # Navigate to Projectmanagement/Lean Page
    def test_nav_to_trainings_open_trainings_schedule(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek')
        self.browser = Trainings_Trainings(self.browser)
        Base_methods.step_report('step 2: navigate to Trainings_open_trainings_schedule page')
        self.browser.nav_to_trainings_open_trainings_schedule()
        Base_methods.step_report('step 3: verify Trainings_open_trainings_schedule page title')
        title = self.browser.get_trainings_trainings_open_trainings_schedule_title(Testdata.TRAININGS_OPEN_SCHEDULE_TITLE)
        assert title == Testdata.TRAININGS_OPEN_SCHEDULE_TITLE

        # Navigate to Projectmanagement/Lean Page
    def test_nav_to_trainings_catalogue(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek')
        self.browser = Trainings_Trainings(self.browser)
        Base_methods.step_report('step 2: navigate to Trainings_catalogue page')
        self.browser.nav_to_trainings_catalogue()
        Base_methods.step_report('step 3: verify Trainings_catalogue page title')
        title = self.browser.get_trainings_trainings_catalogue_title(Testdata.TRAININGS_CATALOGUE_TITLE)
        assert title == Testdata.TRAININGS_CATALOGUE_TITLE