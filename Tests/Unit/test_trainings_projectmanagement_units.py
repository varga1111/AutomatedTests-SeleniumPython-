import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown/Trainings_ProjectManagement')

from conftest import init_driver
#from conftest import failed_check

import allure

from testdata import Testdata
from test_parent import Parent_test
from basemethods import Base_methods

from trainings_projectmanagement import Trainings_Projectmanagement
from trainings_projectmanagement_traditional import Trainings_Projectmanagement_Traditional
from trainings_projectmanagement_agile import Trainings_Projectmanagement_Agile
from trainings_projectmanagement_lean import Trainings_Projectmanagement_Lean


class Test_Trainings_Projectmanagement_Units(Parent_test):

    def test_get_trainings_projectmanagement_title(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek/projektmenedzsment')
        self.browser = Trainings_Projectmanagement(self.browser)
        Base_methods.step_report('step 2: verify Trainings_Projectmanagement page title')
        title = self.browser.get_trainings_projectmanagement_title(Testdata.TRAININGS_PROJECTMANAGEMENT_TITLE)
        assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_TITLE


    '''Test Units (Elements exist)'''
    def test_btn_projectmanagement_traditional_exists(self):
        self.browser = Trainings_Projectmanagement(self.browser)
        self.browser.btn_projectmanagement_traditional_exists()
        
    def test_btn_projectmanagement_agile_exists(self):
        self.browser = Trainings_Projectmanagement(self.browser)
        self.browser.btn_projectmanagement_agile_exists()

    def test_btn_projectmanagement_lean_exists(self):
        self.browser = Trainings_Projectmanagement(self.browser)
        self.browser.btn_projectmanagement_lean_exists()


