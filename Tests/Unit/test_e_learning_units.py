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

    def test_get_e_learning_page_title(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/e-learning')
        self.browser = E_Learning(self.browser)
        Base_methods.step_report('step 2: verify E_Learning page title')
        title = self.browser.get_e_learning_title(Testdata.E_LEARNING_TITLE)
        assert title == Testdata.E_LEARNING_TITLE


        ''' Test Units (Elements exist)'''
    def test_hyper_link_owndev_exists(self):
        self.browser = E_Learning(self.browser)
        self.browser.hyper_link_owndev_exists()

    def test_hyper_link_e_learning_lessons_exists(self):
        self.browser = E_Learning(self.browser)
        self.browser.hyper_link_e_learning_lessons_exists()

    def test_hyper_link_official_exists(self):
        self.browser = E_Learning(self.browser)
        self.browser.hyper_link_official_exists()

    def test_hyper_link_mentored_exists(self):
        self.browser = E_Learning(self.browser)
        self.browser.hyper_link_mentored_exists()

    def test_hyper_link_unique_exists(self):
        self.browser = E_Learning(self.browser)
        self.browser.hyper_link_unique_exists()


