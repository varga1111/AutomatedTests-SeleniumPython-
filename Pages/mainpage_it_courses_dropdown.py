import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs')
from locators import Locators
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Mainpage_It_Courses_Dropdown(Base_methods):
    
    def __init__(self, browser): 
        super().__init__(browser)
    
    ''' Hovers '''
    def hover_to_btn_it_courses(self):
        self.hover(self.browser.find_element_by_id('MegaMenuIT'))


    def hover_to_btn_office_it(self):
        self.hover(self.browser.find_element_by_id('MegaMenuOffice'))


    def hover_to_btn_to_comp_man(self):
        self.hover(self.browser.find_element_by_id('MegaMenuERP'))


    def hover_to_btn_career_start_programs(self):
        self.hover(self.browser.find_element_by_id('MegaMenuKSP'))


    ''' Units (Elements exist)''' 
    # 1st Column
    def btn_it_courses_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses)

    def btn_it_courses_admin_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_admin)

    def btn_it_courses_dev_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_dev)

    def btn_leader_courses_exists(self):
        assert True
        return self.is_visible(Locators.btn_leader_courses)

    def btn_creating_value_exists(self):
        assert True
        return self.is_visible(Locators.btn_creating_value)

    # Hover 1st Column
    # 1/a
    def btn_it_courses_admin_aws_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_admin_aws)
    
    def btn_it_courses_admin_microsoft_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_admin_microsoft)
     
    def btn_it_courses_admin_cisco_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_admin_cisco)
    
    def btn_it_courses_admin_oracle_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_admin_oracle)
    
    def btn_it_courses_admin_vmware_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_admin_vmware)

    def btn_it_courses_admin_ibm_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_admin_ibm)

    def btn_it_courses_admin_linux_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_admin_linux)
     
    def btn_it_courses_admin_other_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_admin_other)

    # 1/b
    def btn_it_courses_dev_aws_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_dev_aws)
    
    def btn_it_courses_dev_micr_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_dev_micr)
    
    def btn_it_courses_dev_java_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_dev_java)
    
    def btn_it_courses_dev_webdev_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_dev_webdev)
     
    def btn_it_courses_dev_mobdev_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_dev_mobdev)
    
    def btn_it_courses_dev_pyth_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_dev_pyth)
    
    def btn_it_courses_dev_other_exists(self):
        assert True
        return self.is_visible(Locators.btn_it_courses_dev_other)
    
    # 1/c
    def btn_leader_courses_itil_exists(self):
        assert True
        return self.is_visible(Locators.btn_leader_courses_itil)
    
    def btn_leader_courses_risk_exists(self):
        assert True
        return self.is_visible(Locators.btn_leader_courses_risk)
    
    def btn_leader_courses_busn_an_exists(self):
        assert True
        return self.is_visible(Locators.btn_leader_courses_busn_an)

    # 1/d
    def btn_creating_value_agile_exists(self):
        assert True
        return self.is_visible(Locators.btn_creating_value_agile)

    def btn_creating_value_devops_exists(self):
        assert True
        return self.is_visible(Locators.btn_creating_value_devops)
    
    #Hover 2nd Column
    def btn_office_exists(self):
        assert True
        return self.is_visible(Locators.btn_office)

    # 2
    def btn_office_mo_exists(self):
        assert True
        return self.is_visible(Locators.btn_office_mo)
    
    def btn_office_mo365_exists(self):
        assert True
        return self.is_visible(Locators.btn_office_mo365)
    
    def btn_office_da_exists(self):
        assert True
        return self.is_visible(Locators.btn_office_da)

    def btn_office_gwc_exists(self):
        return self.is_visible(Locators.btn_office_gwc)

    # Hover 3rd Column
    def btn_comp_man_exists(self):
        assert True
        return self.is_visible(Locators.btn_comp_man)

    def btn_comp_man_sap_exists(self):
        assert True
        return self.is_visible(Locators.btn_comp_man_sap)
    
    def btn_comp_man_sfc_exists(self):
        assert True
        return self.is_visible(Locators.btn_comp_man_sfc)
    
    # Hover 4th Column  
    def btn_car_start_p_exists(self):
        assert True
        return self.is_visible(Locators.btn_car_start_p)
    
    # 4/a
    def btn_car_fy_exists(self):
        assert True
        return self.is_visible(Locators.btn_car_fy)
    
    def btn_for_emp_exists(self):
        assert True
        return self.is_visible(Locators.btn_for_emp)
    
    # 4/a
    def btn_car_fy_jun_dev_exists(self):
        assert True
        return self.is_visible(Locators.btn_car_fy_jun_dev)
        
    def btn_car_fy_app_ad_exists(self):
        assert True
        return self.is_visible(Locators.btn_car_fy_app_ad)
    
    def btn_car_fy_soft_exists(self):
        assert True
        return self.is_visible(Locators.btn_car_fy_soft_test)
    
    def btn_car_fy_hir_proc_exists(self):
        assert True
        return self.is_visible(Locators.btn_car_fy_hir_proc)
    
    def btn_car_fy_apply_exists(self):
        assert True
        return self.is_visible(Locators.btn_car_fy_apply)
    
    def btn_car_fy_faq_exists(self):
        assert True
        return self.is_visible(Locators.btn_car_fy_faq)
    
    # 4/c
    def btn_for_emp_prog_exists(self):
        assert True
        return self.is_visible(Locators.btn_for_emp_prog)
    
    def btn_for_emp_jun_dev_exists(self):
        assert True
        return self.is_visible(Locators.btn_for_emp_jun_dev)
    
    def btn_for_emp_fin_exists(self):
        assert True
        return self.is_visible(Locators.btn_for_emp_fin)
    
    def btn_for_emp_select_exists(self):
        assert True
        return self.is_visible(Locators.btn_for_emp_select)
    
    def btn_for_emp_grnt_exists(self):
        assert True
        return self.is_visible(Locators.btn_for_emp_grnt)
    


    ''' Navigation from IT Courses Dropdown Navigation Bar'''
    # IT Courses/Admin
    def nav_to_it_courses_admin(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_aws(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass
    

    def nav_to_it_courses_admin_microsoft(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_cisco(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_oracle(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_vmware(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_ibm(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_linux(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_other(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass

    
    # IT Courses/Developer
    def nav_to_it_courses_developer(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_aws(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_microsoft(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_java(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_webdev(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_mobile(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_python(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_other(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    # IT Courses/Leader
    def nav_to_it_courses_leader(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_leader_itil_princ2(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_leader_risk_management_inf_security_importer_management(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_leader_business_analyst(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    # IT Courses/Creating Value
    def nav_to_it_courses_creating_value(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_creating_value_agile(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_it_courses_creating_value_devops(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    # Office IT
    def nav_to_office_it(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_office_it_microsoft_office(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_office_it_microsoft_office_365(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_office_it_dataanalyst_courses(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_office_it_workspace_courses(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    # Company Management
    def nav_to_company_management(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_company_management_sap_courses(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_company_management_salesforce_courses(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass

    
    # Career Start Program/For You
    def nav_to_career_start_program_for_you(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_junior_dev_course(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_application_admin(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_software_tester(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_hiring_process(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_applying(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_faq(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    # Career Start Program/For Employers
    def nav_to_career_start_program_for_employers(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_employers_about_the_program(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_employers_what_a_junior_knows(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_employers_fin_and_emp_modell(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_employers_guarantee(self):
        self.do_click(Locators.nav_bar_it_courses)
        pass

    