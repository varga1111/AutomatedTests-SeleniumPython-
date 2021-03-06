import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_Trainings')

from conftest import init_driver

import allure

from testdata import Testdata
from test_parent import Parent_test

from trainings_trainings import Trainings_Trainings
from trainings_softskill import Trainings_Softskill
from trainings_projectmanagement import Trainings_Projectmanagement
from trainings_trainings_open_trainings_schedule import Trainings_Trainings_Open_Trainings_Schedule
from trainings_trainings_catalogue import Trainings_Trainings_Catalogue


class Test_Nav_Trainings_Projectmanagement(Parent_test):
    
    def test_get_trainings_trainings_title(self):
        self.browser = Trainings_Trainings(self.browser)
        try:
            title = self.browser.get_trainings_trainings_title(Testdata.TRAININGS_TRAININGS_TITLE)
            assert title == Testdata.TRAININGS_TRAININGS_TITLE

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False




        # Check Trainings/Projectmanagement Page Elements Exist
    def test_btn_soft_skill_trainings_exists(self):
        self.browser = Trainings_Trainings(self.browser)
        try:
            self.browser.btn_softskill_trainings_exists()

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False
        

    def test_btn_projectmanagement_exists(self):
        self.browser = Trainings_Trainings(self.browser)
        try:
            self.browser.btn_projectmanagement_exists()

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_btn_trainings_open_trainings_schedule_exists(self):
        self.browser = Trainings_Trainings(self.browser)
        try:
            self.browser.btn_trainings_open_trainings_schedule_exists()

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_btn_trainings_catalogue_exists(self):
        self.browser = Trainings_Trainings(self.browser)
        try:
            self.browser.btn_trainings_catalogue_exists()

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False




        ''' Test Navigations & Page Titles Match & Elements Exist'''
        # Trainings Dropdown
        # Navigate to Projectmanagement/Traditional Page
    def test_nav_to_softskill_trainings(self):
        self.browser = Trainings_Trainings(self.browser)
        try:
            self.browser.nav_to_softskill_trainings()

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_get_trainings_softskill_title(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            title = self.browser.get_trainings_softskill_title(Testdata.TRAININGS_SOFTSKILL_TITLE)
            assert title == Testdata.TRAININGS_SOFTSKILL_TITLE

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_nav_back1(self):
        self.browser = Trainings_Softskill(self.browser)

        self.browser.go_back()




        # Navigate to Projectmanagement/Agile Page
    def test_nav_to_projectmanagement(self):
        self.browser = Trainings_Trainings(self.browser)
        try:
            self.browser.nav_to_projectmanagement()

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_get_projectmanagement_title(self):
        self.browser = Trainings_Projectmanagement(self.browser)
        try:
            title = self.browser.get_trainings_projectmanagement_title(Testdata.TRAININGS_PROJECTMANAGEMENT_TITLE)
            assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_TITLE

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_nav_back2(self):
        self.browser = Trainings_Projectmanagement(self.browser)
        
        self.browser.go_back()




        # Navigate to Projectmanagement/Lean Page
    def test_nav_to_trainings_open_trainings_schedule(self):
        self.browser = Trainings_Trainings(self.browser)
        try:
            self.browser.nav_to_trainings_open_trainings_schedule()

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_get_trainings_trainings_open_trainings_schedule(self):
        self.browser = Trainings_Trainings_Open_Trainings_Schedule(self.browser)
        try:
            title = self.browser.get_trainings_trainings_open_trainings_schedule_title(Testdata.TRAININGS_OPEN_SCHEDULE_TITLE)
            assert title == Testdata.TRAININGS_OPEN_SCHEDULE_TITLE

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False

    
    def test_nav_back3(self):
        self.browser = Trainings_Trainings_Open_Trainings_Schedule(self.browser)

        self.browser.go_back()




            # Navigate to Projectmanagement/Lean Page
    def test_nav_to_trainings_catalogue(self):
        self.browser = Trainings_Trainings(self.browser)
        try:
            self.browser.nav_to_trainings_catalogue()

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_get_trainings_trainings_catalogue_title(self):
        self.browser = Trainings_Trainings_Catalogue(self.browser)
        try:
            title = self.browser.get_trainings_trainings_catalogue_title(Testdata.TRAININGS_CATALOGUE_TITLE)
            assert title == Testdata.TRAININGS_CATALOGUE_TITLE

        except:
            screen_shot = 'test_login.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False
