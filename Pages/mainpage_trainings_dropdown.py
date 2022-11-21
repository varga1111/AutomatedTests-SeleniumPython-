import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from locators import Locators
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Mainpage_Trainings_Dropdown(Base_methods):
    
    def __init__(self, browser): 
        super().__init__(browser)


    ''' Units (Elements exist)''' 
    def btn_trainings_exists(self):
        assert True
        return self.is_visible(Locators.btn_trainings)

    def btn_open_training_schedule_exists(self):
        assert True
        return self.is_visible(Locators.btn_open_training_schedule)

    def btn_training_catalogue_exists(self):
        assert True
        return self.is_visible(Locators.btn_training_catalogue)

    def btn_project_management_exists(self):
        assert True
        return self.is_visible(Locators.btn_project_management)

    def btn_traditional_pm_exists(self):
        assert True
        return self.is_visible(Locators.btn_traditional_pm)

    def btn_agile_pm_exists(self):
        assert True
        return self.is_visible(Locators.btn_agile_pm)

    def btn_lean_exists(self):
        assert True
        return self.is_visible(Locators.btn_lean)

    def btn_soft_skill_exists(self):
        assert True
        return self.is_visible(Locators.btn_soft_skill)

    def btn_leader_training_exists(self):
        assert True
        return self.is_visible(Locators.btn_leader_training)

    def btn_salesforce_training_exists(self):
        assert True
        return self.is_visible(Locators.btn_salesforce_training)

    def btn_competence_training_exists(self):
        assert True
        return self.is_visible(Locators.btn_competence_training)

    def btn_coaching_exists(self):
        assert True
        return self.is_visible(Locators.btn_coaching_dropdown)


