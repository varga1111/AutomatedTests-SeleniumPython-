import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown/Trainings_Softskill')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown/Trainings_ProjectManagement')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_Trainings_Dropdown/Trainings_Trainings')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_E_Learning')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_E_Learning/E_Learning_Owndev')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/IT_Courses')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/Office_IT')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/Company_Management')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/Career_Start_Program')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Admin')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Developer')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Leader')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Creating_Value')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Exams')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Discounts')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/Career_Start_Program/For_You')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Navbar_IT_Courses_Dropdown/Career_Start_Program/For_Employers')
sys.path.insert(0,'/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/From_Login')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from conftest import init_driver
#from conftest import failed_verify

import allure

from testdata import Testdata
from test_parent import Parent_test
from basemethods import Base_methods

from mainpage import MainPage
from course_schedules import Course_Schedules
from discounts import Discounts
from contact import Contact


class Test_Nav_MainPage_Navbar(Parent_test):

    ''' Test Navigations & Page Titles'''
        # Trainings Dropdown
    '''    def test_nav_to_trainings_softskill(self):
        pass
    

    def test_nav_to_trainings_projectmanagement(self):
        pass


    def test_nav_to_trainings_trainings(self):
        pass

    
    def test_nav_to_trainings_softskill_leader_trainings(self):
        pass
    

    def test_nav_to_trainings_softskill_salesforce_trainings(self):
        pass


    def test_nav_to_trainings_softskill_competence_improvement_trainings(self):
        pass


    def test_nav_to_trainings_softskill_coaching(self):
        pass


    def test_nav_to_trainings_projectmanagement_traditional(self):
        pass


    def test_nav_to_trainings_projectmanagement_agile(self):
        pass


    def test_nav_to_trainings_projectmanagement_lean(self):
        pass

    
    def test_nav_to_trainings_trainings_open_trainings_schedule(self):
        pass
    

    def test_nav_to_trainings_trainings_catalogue(self):
        pass'''
    
        # E-Learning


        # IT-Courses Dropdown


        # Exams Dropdown


        # To Course Schedules
    def test_nav_to_course_schedules(self):
        Base_methods.step_report('step 1: open browser on https://training360.com')
        self.browser = MainPage(self.browser)
        Base_methods.step_report('step 2: navigate to Course_Schedules page')
        self.browser.nav_to_course_schedules()
        Base_methods.step_report('step 3: verify Course_Schedules page title')
        title = self.browser.get_course_schedules_page_title(Testdata.COURSE_SCHEDULES_TITLE)
        assert title == Testdata.COURSE_SCHEDULES_TITLE

        # To Discounts
    def test_nav_to_discounts(self):
        Base_methods.step_report('step 1: open browser on https://training360.com')
        self.browser = MainPage(self.browser)
        Base_methods.step_report('step 2: navigate to Discounts page')
        self.browser.nav_to_discounts()
        Base_methods.step_report('step 3: verify Discounts page title')
        title = self.browser.get_discount_page_title(Testdata.DISCOUNTS_TITLE)
        assert title == Testdata.DISCOUNTS_TITLE

        # To Contacts
    def test_nav_to_contacts(self):
        Base_methods.step_report('step 1: open browser on https://training360.com')
        self.browser = MainPage(self.browser)
        Base_methods.step_report('step 2: navigate to Contact page')
        self.browser.nav_to_contacts()
        Base_methods.step_report('step 3: verify Contact page title')
        title = self.browser.get_contacts_page_title(Testdata.CONTACTS_TITLE)
        assert title == Testdata.CONTACTS_TITLE



    