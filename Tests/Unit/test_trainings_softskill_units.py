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
    
    def test_get_trainings_softskill_title(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek/soft-skill')
        self.browser = Trainings_Softskill(self.browser)
        Base_methods.step_report('step 2: verify Trainings_Softskill page title')
        title = self.browser.get_trainings_softskill_title(Testdata.TRAININGS_SOFTSKILL_TITLE)
        assert title == Testdata.TRAININGS_SOFTSKILL_TITLE

  
    ''' Test Units (Elements exist)'''
    def test_btn_leader_trainings_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        self.browser.btn_leader_trainings_exists()
        
    def test_btn_salesforce_trainings_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        self.browser.btn_salesforce_trainings_exists()

    def test_btn_competence_improvement_trainings_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        self.browser.btn_competence_improvement_trainings_exists()

    def test_btn_coaching_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        self.browser.btn_coaching_exists()
