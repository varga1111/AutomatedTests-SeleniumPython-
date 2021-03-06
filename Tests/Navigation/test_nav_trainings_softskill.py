import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_Softskill')

from conftest import init_driver

import allure

from testdata import Testdata
from test_parent import Parent_test

from trainings_softskill import Trainings_Softskill
from trainings_softskill_leader_trainings import Trainings_Softskill_Leader_Trainings
from trainings_softskill_salesforce_trainings import Trainings_Softskill_Salesforce_Trainings
from trainings_softskill_competence_improvement_trainings import Trainings_Softskill_Competence_Improvement_Trainings
from trainings_softskill_coaching import Trainings_Softskill_Coaching

class Test_Nav_Trainings_Softskill(Parent_test):
    
    def test_get_trainings_softskill_title(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            title = self.browser.get_trainings_softskill_title(Testdata.TRAININGS_SOFTSKILL_TITLE)
            assert title == Testdata.TRAININGS_SOFTSKILL_TITLE

        except:
            screen_shot = 'test_get_trainings_softskill_title.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


        # Check Trainings/Softskill Page Elements Exist
    def test_btn_leader_trainings_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            self.browser.btn_leader_trainings_exists()
        
        except:
            screen_shot = 'test_btn_leader_trainings_exists.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_btn_salesforce_trainings_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            self.browser.btn_salesforce_trainings_exists()

        except:
            screen_shot = 'test_btn_salesforce_trainings_exists.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_btn_competence_improvement_trainings_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            self.browser.btn_competence_improvement_trainings_exists()

        except:
            screen_shot = 'test_btn_competence_improvement_trainings_exists.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_btn_coaching_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            self.browser.btn_coaching_exists()

        except:
            screen_shot = 'test_btn_coaching_exists.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False




        ''' Test Navigations & Page Titles Match & Elements Exist'''
        # Trainings Dropdown
        # Navigate to Leader Trainings
    def test_nav_to_leader_trainings(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            self.browser.nav_to_leader_trainings()

        except:
            screen_shot = 'test_nav_to_leader_trainings.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_get_trainings_softskill_leader_trainings_title(self):
        self.browser = Trainings_Softskill_Leader_Trainings(self.browser)
        try:
            title = self.browser.get_trainings_softskill_leader_trainings_title(Testdata.TRAININGS_SOFTSKILL_LEADER_TITLE)
            assert title == Testdata.TRAININGS_SOFTSKILL_LEADER_TITLE

        except:
            screen_shot = 'test_get_trainings_softskill_leader_trainings_title.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_nav_back1(self):
        self.browser = Trainings_Softskill_Leader_Trainings(self.browser)
        self.browser.go_back()




        # Navigate to Salesforce Trainings
    def test_nav_to_salesforce_trainings(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            self.browser.nav_to_salesforce_trainings()

        except:
            screen_shot = 'test_nav_to_salesforce_trainings.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_get_trainings_softskill_salesforce_trainings_title(self):
        self.browser = Trainings_Softskill_Salesforce_Trainings(self.browser)
        try:
            title = self.browser.get_trainings_softskill_salesforce_trainings_title(Testdata.TRAININGS_SOFTSKILL_SALESFORCE_TITLE)
            assert title == Testdata.TRAININGS_SOFTSKILL_SALESFORCE_TITLE

        except:
            screen_shot = 'test_get_trainings_softskill_salesforce_trainings_title.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_nav_back2(self):
        self.browser = Trainings_Softskill_Salesforce_Trainings(self.browser)
        self.browser.go_back()




        # Navigate to Competence Improvement Trainings
    def test_nav_to_competence_improvement_trainings(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            self.browser.nav_to_competence_improvement_trainings()

        except:
            screen_shot = 'test_nav_to_competence_improvement_trainings.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_get_trainings_softskill_competenve_improvement_trainings_title(self):
        self.browser = Trainings_Softskill_Competence_Improvement_Trainings(self.browser)
        try:
            title = self.browser.get_trainings_softskill_competence_improvement_trainings_title(Testdata.TRAININGS_SOFTSKILL_COMPETENCE_TITLE)
            assert title == Testdata.TRAININGS_SOFTSKILL_COMPETENCE_TITLE

        except:
            screen_shot = 'test_get_trainings_softskill_competenve_improvement_trainings_title.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_nav_back3(self):
        self.browser = Trainings_Softskill_Competence_Improvement_Trainings(self.browser)
        self.browser.go_back()




        # Navigate to Coaching
    def test_nav_to_coaching(self):
        self.browser = Trainings_Softskill(self.browser)
        try:
            self.browser.nav_to_coaching()

        except:
            screen_shot = 'test_nav_to_coaching.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False


    def test_get_trainings_softskill_coaching_title(self):
        self.browser = Trainings_Softskill_Coaching(self.browser)
        try:
            title = self.browser.get_trainings_softskill_coaching_title(Testdata.TRAININGS_SOFTSKILL_COACHING_TITLE)
            assert title == Testdata.TRAININGS_SOFTSKILL_COACHING_TITLE

        except:
            screen_shot = 'test_get_trainings_softskill_coaching_title.png'
            self.browser.save_screenshot(screen_shot)
            with open (screen_shot, mode= 'rb') as file:
                f = file.read()
            allure.attach(f, 'screenshot', allure.attachment_type.PNG )
            assert False