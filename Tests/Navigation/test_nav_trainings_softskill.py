import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown/Trainings_Softskill')

from conftest import init_driver
#from conftest import failed_check

import allure

from testdata import Testdata
from test_parent import Parent_test
from basemethods import Base_methods

from trainings_softskill import Trainings_Softskill
from trainings_softskill_leader_trainings import Trainings_Softskill_Leader_Trainings
from trainings_softskill_salesforce_trainings import Trainings_Softskill_Salesforce_Trainings
from trainings_softskill_competence_improvement_trainings import Trainings_Softskill_Competence_Improvement_Trainings
from trainings_softskill_coaching import Trainings_Softskill_Coaching

class Test_Nav_Trainings_Softskill(Parent_test):
  
    ''' Test Navigations'''
        # Trainings Dropdown
        # Navigate to Leader Trainings
    def test_nav_to_leader_trainings(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek/soft-skill')
        self.browser = Trainings_Softskill(self.browser)
        Base_methods.step_report('step 2: navigate to Leader_trainings page ')
        self.browser.nav_to_leader_trainings()
        Base_methods.step_report('step 3: verify Leader_trainings page title')
        title = self.browser.get_trainings_softskill_leader_trainings_title(Testdata.TRAININGS_SOFTSKILL_LEADER_TITLE)
        assert title == Testdata.TRAININGS_SOFTSKILL_LEADER_TITLE

        # Navigate to Salesforce Trainings
    def test_nav_to_salesforce_trainings(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek/soft-skill')
        self.browser = Trainings_Softskill(self.browser)
        Base_methods.step_report('step 2: navigate to Salesforce_training page ')
        self.browser.nav_to_salesforce_trainings()
        Base_methods.step_report('step 3: verify Salesforce_training page title')
        title = self.browser.get_trainings_softskill_salesforce_trainings_title(Testdata.TRAININGS_SOFTSKILL_SALESFORCE_TITLE)
        assert title == Testdata.TRAININGS_SOFTSKILL_SALESFORCE_TITLE

        # Navigate to Competence Improvement Trainings
    def test_nav_to_competence_improvement_trainings(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek/soft-skill')
        self.browser = Trainings_Softskill(self.browser)
        Base_methods.step_report('step 2: navigate to Competence_improvement_trainings page ')
        self.browser.nav_to_competence_improvement_trainings()
        Base_methods.step_report('step 3: verify Competence_improvement_trainings page title')
        title = self.browser.get_trainings_softskill_competence_improvement_trainings_title(Testdata.TRAININGS_SOFTSKILL_COMPETENCE_TITLE)
        assert title == Testdata.TRAININGS_SOFTSKILL_COMPETENCE_TITLE

        # Navigate to Coaching
    def test_nav_to_coaching(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek/soft-skill')
        self.browser = Trainings_Softskill(self.browser)
        Base_methods.step_report('step 2: navigate to Coaching page ')
        self.browser.nav_to_coaching()
        Base_methods.step_report('step 3: verify Coaching page title')
        title = self.browser.get_trainings_softskill_coaching_title(Testdata.TRAININGS_SOFTSKILL_COACHING_TITLE)
        assert title == Testdata.TRAININGS_SOFTSKILL_COACHING_TITLE