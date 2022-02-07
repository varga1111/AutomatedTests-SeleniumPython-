import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_Softskill')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_ProjectManagement')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_Trainings')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/E_Learning')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/E_Learning/E_Learning_Owndev')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/Office_IT')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/Company_Management')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/Career_Start_Program')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Admin')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Developer')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Leader')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Creating_Value')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Exams')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Discounts')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/Career_Start_Program/For_You')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_IT_Courses_Dropdown/Career_Start_Program/For_Employers')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')

from conftest import init_driver

import allure

from testdata import Testdata
from test_parent import Parent_test

from mainpage import MainPage
from mainpage_it_courses_dropdown import Mainpage_It_Courses_Dropdown

class Test_Hover(Parent_test):

    def test_close_popup(self):
        self.browser = MainPage(self.browser)
    
        self.browser.close_popup()




    def test_get_main_page_title(self):
        self.browser = MainPage(self.browser)

        title = self.browser.get_main_page_title(Testdata.MAIN_PAGE_TITLE)

        assert title == Testdata.MAIN_PAGE_TITLE 


    

    def test_nav_to_btn_nav_bar_it_courses(self):
        self.browser = MainPage(self.browser)

        self.browser.nav_to_navbar_it_courses()


    def test_hover_to_btn_it_courses(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)

        self.browser.hover_to_btn_it_courses()


    def test_hover_to_btn_office_it(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)

        self.browser.hover_to_btn_office_it()


    def test_hover_to_btn_to_comp_man(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)

        self.browser.hover_to_btn_to_comp_man()


    def test_hover_to_btn_career_start_programs(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        
        self.browser.hover_to_btn_career_start_programs()