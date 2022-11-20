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


class Test_Nav_Trainings_Projectmanagement(Parent_test):


    ''' Test Navigations'''
        # Trainings Dropdown
        # Navigate to Projectmanagement/Traditional Page
    def test_nav_to_projectmanagement_traditional(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek/projektmenedzsment')
        self.browser = Trainings_Projectmanagement(self.browser)
        Base_methods.step_report('step 2: navigate to Projectmanagement_Traditional page')
        self.browser.nav_to_projectmanagement_traditional()
        Base_methods.step_report('step 3: verify Trainings_Projectmanagement_Traditional page title')
        title = self.browser.get_trainings_projectmanagement_traditional_title(Testdata.TRAININGS_PROJECTMANAGEMENT_TRADITIONAL_TITLE)
        assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_TRADITIONAL_TITLE


        # Navigate to Projectmanagement/Agile Page
    def test_nav_to_projectmanagement_agile(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek/projektmenedzsment')
        self.browser = Trainings_Projectmanagement(self.browser)
        Base_methods.step_report('step 2: navigate to Projectmanagement_Agile page')
        self.browser.nav_to_projectmanagement_agile()
        Base_methods.step_report('step 3: verify Trainings_Projectmanagement_Agile page title')
        title = self.browser.get_trainings_projectmanagement_agile_title(Testdata.TRAININGS_PROJECTMANAGEMENT_AGILE_TITLE)
        assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_AGILE_TITLE


        # Navigate to Projectmanagement/Lean Page
    def test_nav_to_projectmanagement_lean(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/treningek/projektmenedzsment')
        self.browser = Trainings_Projectmanagement(self.browser)
        Base_methods.step_report('step 2: navigate to Projectmanagement_Lean page')
        self.browser.nav_to_projectmanagement_lean()
        Base_methods.step_report('step 3: verify Trainings_Projectmanagement_lean title')
        title = self.browser.get_trainings_projectmanagement_lean_title(Testdata.TRAININGS_PROJECTMANAGEMENT_LEAN_TITLE)
        assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_LEAN_TITLE


        
