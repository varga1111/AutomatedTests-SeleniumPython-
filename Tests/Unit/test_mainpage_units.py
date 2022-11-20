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
#from conftest import failed_check

import allure

from testdata import Testdata
from test_parent import Parent_test
from basemethods import Base_methods

from mainpage import MainPage
from mainpage_it_courses_dropdown import Mainpage_It_Courses_Dropdown
from mainpage_trainings_dropdown import Mainpage_Trainings_Dropdown
from course_schedules import Course_Schedules
from discounts import Discounts
from contact import Contact

class Test_MainPage_Units(Parent_test):
    
    def test_get_main_page_title(self):
        Base_methods.step_report('step 1: open browser on https://training360.com')
        self.browser = MainPage(self.browser)
        Base_methods.step_report('step 2: verify Mainpage page title')
        title = self.browser.get_main_page_title(Testdata.MAIN_PAGE_TITLE)
        assert title == Testdata.MAIN_PAGE_TITLE

    
    ''' Main Nav Bar Buttons'''
    def test_main_page_button_exists(self):
        self.browser = MainPage(self.browser)
        visible = self.browser.main_page_button_exists()
        assert visible

    def test_nav_bar_trainings_exists(self):
        self.browser = MainPage(self.browser)
        visible = self.browser.nav_bar_trainings_exists()
        assert visible

    def test_nav_bar_e_learning_exists(self):
        self.browser = MainPage(self.browser)
        visible = self.browser.nav_bar_e_learning_exists()
        assert visible

    def test_nav_bar_it_courses_exists(self):
        self.browser = MainPage(self.browser)
        visible = self.browser.nav_bar_it_courses_exists()
        assert visible

    def test_nav_bar_course_schedules_exists(self):
        self.browser = MainPage(self.browser)
        visible = self.browser.nav_bar_course_schedules_exists()
        assert visible

    def test_nav_bar_discounts_exists(self):
        self.browser = MainPage(self.browser)
        visible = self.browser.nav_bar_discounts_exists()
        assert visible

    def test_nav_bar_contacts_exists(self):
        self.browser = MainPage(self.browser)
        visible = self.browser.nav_bar_contacts_exists()
        assert visible

    def test_nav_bar_cart_exists(self):
        self.browser = MainPage(self.browser)
        visible = self.browser.nav_bar_cart_exists()
        assert visible

    def test_nav_bar_login_exists(self):
        self.browser = MainPage(self.browser)
        visible = self.browser.nav_bar_login_exists()
        assert visible


    ''' Mainpage Trainings Dropdown Buttons'''
        #Click on Trainings dropdown button
    def test_click_on_trainings_dropdown(self):
        self.browser = MainPage(self.browser)
        self.browser.click_on_trainings_dropdown()

    def test_btn_trainings_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_trainings_exists()
        assert visible

    def test_btn_open_training_schedule_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_open_training_schedule_exists()
        assert visible

    def test_btn_training_catalogue_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_training_catalogue_exists()
        assert visible

    def test_btn_project_management_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_project_management_exists()
        assert visible

    def test_btn_traditional_pm_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_traditional_pm_exists()
        assert visible

    def test_btn_agile_pm_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_agile_pm_exists()
        assert visible

    def test_btn_lean_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_lean_exists()
        assert visible

    def test_btn_soft_skill_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_soft_skill_exists()
        assert visible

    def test_btn_leader_training_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_leader_training_exists()
        assert visible

    def test_btn_salesforce_training_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_salesforce_training_exists()
        assert visible

    def test_btn_competence_training_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_competence_training_exists()
        assert visible

    def test_btn_coaching_exists(self):
        self.browser = Mainpage_Trainings_Dropdown(self.browser)
        visible = self.browser.btn_coaching_exists()
        assert visible


    ''' IT Courses Dropdown Buttons/IT Courses'''
    # Click on IT Courses dropdown button
    def test_click_on_it_courses_dropdown(self):
        self.browser = MainPage(self.browser)
        self.browser.click_on_it_courses_dropdown()

    # Hover 1st Column
    def test_btn_it_courses_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_exists()
        assert visible
        self.browser.hover_to_btn_it_courses()
        
    def test_btn_it_courses_admin_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_admin_exists()
        assert visible

    def test_btn_it_courses_dev_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_dev_exists()
        assert visible

    def test_btn_leader_courses_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_leader_courses_exists()
        assert visible
    
    def test_btn_creating_value_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_creating_value_exists()
        assert visible

    # 1/a
    def test_btn_it_courses_admin_aws_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_admin_aws_exists()
        assert visible
     
    def test_btn_it_courses_admin_microsoft_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_admin_microsoft_exists()
        assert visible

    def test_btn_it_courses_admin_cisco_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_admin_cisco_exists()
        assert visible
     
    def test_btn_it_courses_admin_oracle_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_admin_oracle_exists()
        assert visible
     
    def test_btn_it_courses_admin_vmware_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_admin_vmware_exists()
        assert visible
    
    def test_btn_it_courses_admin_ibm_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_admin_ibm_exists()
        assert visible
    
    def test_btn_it_courses_admin_linux_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_admin_linux_exists()
        assert visible

    def test_btn_it_courses_admin_other_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_admin_other_exists()
        assert visible
     
    # 1/b
    def test_btn_it_courses_dev_aws_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_dev_aws_exists()
        assert visible

    def test_btn_it_courses_dev_micr_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_dev_micr_exists()
        assert visible
     
    def test_btn_it_courses_dev_java_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_dev_java_exists()
        assert visible
     
    def test_btn_it_courses_dev_webdev_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_dev_webdev_exists()
        assert visible

    def test_btn_it_courses_dev_mobdev_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_dev_mobdev_exists()
        assert visible
     
    def test_btn_it_courses_dev_pyth_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_dev_pyth_exists()
        assert visible
     
    def test_btn_it_courses_dev_other_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_it_courses_dev_other_exists()
        assert visible
     
    # 1/c
    def test_btn_leader_courses_itil_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_leader_courses_itil_exists()
        assert visible
     
    def test_btn_leader_courses_risk_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_leader_courses_risk_exists()
        assert visible

    def test_btn_leader_courses_busn_an_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_leader_courses_busn_an_exists()
        assert visible

    # 1/d
    def test_btn_creating_value_agile_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_creating_value_agile_exists()
        assert visible

    def test_btn_creating_value_devops_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_creating_value_devops_exists()
        assert visible

    # Hover 2nd Column
    def test_btn_office_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_office_exists()
        assert visible
        self.browser.hover_to_btn_office_it()

    # 2
    def test_btn_office_mo_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_office_mo_exists()
        assert visible

    def test_btn_office_mo365_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_office_mo365_exists()
        assert visible
     
    def test_btn_office_da_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_office_da_exists()
        assert visible
    
    def test_btn_office_gwc_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_office_gwc_exists()
        assert visible

    # Hover to 3rd Column
    def test_btn_comp_man_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_comp_man_exists()
        assert visible
        self.browser.hover_to_btn_to_comp_man()
    
    def test_btn_comp_man_sap_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_comp_man_sap_exists()
        assert visible

    def test_btn_comp_man_sfc_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_comp_man_sfc_exists()
        assert visible

    # Hover to 4th Column
    def test_btn_car_start_p_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_car_start_p_exists()
        assert visible
        self.browser.hover_to_btn_career_start_programs()

        # 4/a
    def test_btn_car_fy_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_car_fy_exists()
        assert visible
   
    def test_btn_for_emp_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_for_emp_exists()
        assert visible

    # 4/a
    def test_btn_car_fy_jun_dev_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_car_fy_jun_dev_exists()
        assert visible

    def test_btn_car_fy_app_ad_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_car_fy_app_ad_exists()
        assert visible

    def test_btn_car_fy_soft_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_car_fy_soft_exists()
        assert visible
     
    def test_btn_car_fy_hir_proc_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_car_fy_hir_proc_exists()
        assert visible
     
    def test_btn_car_fy_apply_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_car_fy_apply_exists()
        assert visible

    def test_btn_car_fy_faq_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_car_fy_faq_exists()
        assert visible
    
    # 4/b
    def test_btn_for_emp_prog_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_for_emp_prog_exists()
        assert visible
     
    def test_btn_for_emp_jun_dev_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_for_emp_jun_dev_exists()
        assert visible

    def test_btn_for_emp_fin_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_for_emp_fin_exists()
        assert visible
     
    def test_btn_for_emp_select_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_for_emp_select_exists()
        assert visible

    def test_btn_for_emp_grnt_exists(self):
        self.browser = Mainpage_It_Courses_Dropdown(self.browser)
        visible = self.browser.btn_for_emp_grnt_exists()
        assert visible
     

    '''Footer Buttons'''
    # 1st Column
'''    def test_btn_apply_exists(self):
        pass
    
     
    def test_btn_gen_course_grt_cond_exists(self):
        pass
    
     
    def test_btn_online_service_cond_exists(self):
        pass
    
     
    def test_btn_proms_and_discounts_exists(self):
        pass
    
     
    # 2nd Column
    def test_btn_news_exists(self):
        pass
    
     
    def test_btn_careers_exists(self):
        pass
    
     
    def test_btn_about_us_exists(self):
        pass
    
     
    def test_btn_impressum_exists(self):
        pass
    
     
    # 3rd Column
    def test_btn_lvc_exists(self):
        pass
    
     
    def test_btn_mentored_courses_exists(self):
        pass
    
     
    def test_btn_edu_advice_exists(self):
        pass
    
     
    def test_btn_pre_asess_exists(self):
        pass
    
     
    def test_btn_unique_edu_services_exists(self):
        pass
    
     
    def test_btn_accomodations_exists(self):
        pass
    
     
    # 4th Column
    def test_btn_privacy_inf_exists(self):
        pass
    
     
    def test_btn_busn_policies_exists(self):
        pass
    
     
    def test_btn_adult_tutor_laws_exists(self):
        pass
    
     
    def test_btn_about_tenders_exists(self):
        pass
    
     
    # 5th Column
    def test_btn_phone_skype_exists(self):
        pass
    
     
    def test_btn_email_exists(self):
        pass
    
     
    def test_btn_map_addr_exists(self):
        pass
    
     
    # 6th Column
    def test_btn_fb_exists(self):
        pass
    
     
    def test_btn_linkedin_exists(self):
        pass
    
     
    def test_btn_spotify_exists(self):
        pass
    
     
    def test_btn_callback_exists(self):
        pass
    
     
    def test_btn_subscribe_exists(self):
        pass
    
     
    # The Bottom Bottom
    def test_btn_certificate1_exists(self):
        pass
    
     
    def test_btn_certificate2_exists(self):
        pass
    
     

   '''