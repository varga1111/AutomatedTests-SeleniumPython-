import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_E_Learning')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from conftest import init_driver
#from conftest import failed_check

import allure

from testdata import Testdata
from test_parent import Parent_test
from basemethods import Base_methods

from e_learning import E_Learning
from e_learning_owndev import E_Learning_Owndev
from e_learning_official import E_Learning_Official
from e_learning_unique import E_Learning_Unique
from mentored_courses import Mentored_Courses

class Test_Nav_E_Learning(Parent_test):

    ''' Test Navigation '''
        # E-Learning/Owndev
    def test_nav_to_e_learning_owndev(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/e-learning')
        self.browser = E_Learning(self.browser)
        Base_methods.step_report('step 2: navigate to E_learning_owndev page')
        self.browser.nav_to_elearning_owndev()
        Base_methods.step_report('step 3: verify E_learning_owndev page title')
        title = self.browser.get_e_learning_owndev_title(Testdata.E_LEARNING_OWNDEV_TITLE)
        assert title == Testdata.E_LEARNING_OWNDEV_TITLE

        # E-Learning/Official
    def test_nav_to_e_learning_official(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/e-learning')
        self.browser = E_Learning(self.browser)
        Base_methods.step_report('step 2: navigate to E_learning_official page')
        self.browser.nav_to_e_learning_official()
        Base_methods.step_report('step 3: verify E_learning_official page title')
        title = self.browser.get_e_learning_official_title(Testdata.E_LEARNING_OFFICIAL_TITLE)
        assert title == Testdata.E_LEARNING_OFFICIAL_TITLE

        # Mentored Courses
    def test_nav_to_mentored_courses(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/e-learning')
        self.browser = E_Learning(self.browser)
        Base_methods.step_report('step 2: navigate to Mentored_course page')
        self.browser.nav_to_mentored_courses()
        Base_methods.step_report('step 3: verify Mentored_course page title')
        title = self.browser.get_mentored_courses_title(Testdata.MENTORED_COURSES_TITLE)
        assert title == Testdata.MENTORED_COURSES_TITLE

        # E-Learning/Unique
    def test_nav_to_e_learning_unique(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/e-learning')
        self.browser = E_Learning(self.browser)
        Base_methods.step_report('step 2: navigate to E_learning_unique page')
        self.browser.nav_to_e_learning_unique()
        Base_methods.step_report('step 3: verify E_learning_unique page title')
        title = self.browser.get_e_learning_unique_title(Testdata.E_LEARNING_UNIQUE_TITLE)
        assert title == Testdata.E_LEARNING_UNIQUE_TITLE