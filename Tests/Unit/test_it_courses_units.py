import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

import allure
from conftest import init_driver
from testdata import Testdata
from basemethods import Base_methods

from it_courses import  It_Courses
from test_parent import Parent_test

class Test_It_Courses(Parent_test):

    def test_it_courses_title(self):
        Base_methods.step_report('step 1: open browser at https://www.training360.com/informatikai-kepzesek')
        self.browser = It_Courses(self.browser)
        Base_methods.step_report('step 2: verify It_courses page title')
        title = self.browser.get_page_title(Testdata.IT_COURSES_TITLE)
        assert title == Testdata.IT_COURSES_TITLE

