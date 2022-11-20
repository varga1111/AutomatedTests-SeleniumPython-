from selenium.webdriver.common.by import By
from basemethods import Base_methods


class Locators(Base_methods):
    '''MainPage '''
    main_page_button = (By.XPATH, '//*[@id="navbar"]/div[1]/a/img')
    popup_close_btn = (By.ID,'NewsletterModalCloseButton')
    ''' NavBar Locators(By.)'''
    # Main Nav Bar Buttons
    nav_bar_trainings = (By.ID, 'PrimaryNavTraining')
    nav_bar_e_learning = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[2]/a')
    nav_bar_it_courses = (By.ID, 'PrimaryNavCourses')
    nav_bar_course_schedules = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[5]/a')
    nav_bar_discounts = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[6]/a')
    nav_bar_discounts_2 = (By.XPATH,'//a[contains(@href,"/akciok")]')
    nav_bar_contacts = (By.XPATH,'//*[@id="PrimaryNavMainMenu"]/li[7]/a')
    nav_bar_cart = (By.XPATH, '//*[@id="navbar"]/div[3]/ul/li[2]/a')
    nav_bar_login = (By.XPATH, '//*[@id="navbar"]/div[3]/ul/li[3]/a/i')

    '''Footer Locators'''
    # 1st Column
    btn_apply = (By.XPATH, '/html/body/footer/nav/div/div/div[1]/ul/li[1]/a/span')
    btn_gen_course_grt_cond = (By.XPATH, '/html/body/footer/nav/div/div/div[1]/ul/li[2]/a/span')
    btn_online_service_cond = (By.XPATH, '/html/body/footer/nav/div/div/div[1]/ul/li[3]/a/span')
    btn_proms_and_discounts = (By.XPATH, '/html/body/footer/nav/div/div/div[1]/ul/li[4]/a/span')
    # 2nd Column
    btn_news = (By.XPATH, '/html/body/footer/nav/div/div/div[2]/ul/li[1]/a/span')
    btn_careers = (By.XPATH, '/html/body/footer/nav/div/div/div[2]/ul/li[2]/a/span')
    btn_about_us = (By.XPATH, '/html/body/footer/nav/div/div/div[2]/ul/li[3]/a/span')
    btn_impressum = (By.XPATH, '/html/body/footer/nav/div/div/div[2]/ul/li[4]/a/span')
    # 3rd Column
    btn_lvc = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[1]/a/span')
    btn_mentored_courses = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[2]/a/span')
    btn_edu_advice = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[3]/a/span')
    btn_pre_asess = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[4]/a/span')
    btn_unique_edu_services = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[5]/a/span')
    btn_accomodations = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[6]/a/span')
    # 4th Column
    btn_privacy_inf = (By.XPATH, '/html/body/footer/nav/div/div/div[4]/ul/li[1]/a/span')
    btn_busn_policies = (By.XPATH, '/html/body/footer/nav/div/div/div[4]/ul/li[2]/a/span')
    btn_adult_tutor_laws = (By.XPATH, '/html/body/footer/nav/div/div/div[4]/ul/li[3]/a/span')
    btn_about_tenders = (By.XPATH, '/html/body/footer/nav/div/div/div[4]/ul/li[4]/a/span')
    # 5th Column
    btn_phone_skype = (By.XPATH, '/html/body/footer/nav/div/div/div[5]/ul/li[1]/a/span[2]')
    btn_email = (By.XPATH, '/html/body/footer/nav/div/div/div[5]/ul/li[2]/a/span[2]')
    btn_map_addr = (By.XPATH, '/html/body/footer/nav/div/div/div[5]/ul/li[4]/a/address')
    # 6th Column
    btn_fb = (By.XPATH, '')
    btn_linkedin = (By.XPATH, '')
    btn_spotify = (By.XPATH, '')
    btn_callback = (By.XPATH, '')
    btn_subscribe = (By.XPATH, '')
    # The Bottom Bottom
    btn_certificate1 = (By.XPATH, '')
    btn_certificate2 = (By.XPATH, '')
################################################################################################################################################
    '''Trainings_Projectmanagement'''
    btn_projectmanagement_traditional = (By.XPATH, '//*[@id="pagecontent"]/div/div[1]/div/div[2]/div/a')
    btn_projectmanagement_agile = (By.XPATH, '//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/a/i')
    btn_projectmanagement_lean = (By.XPATH, '//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/a')

    hyper_link_projectmanagement_traditional = (By.LINK_TEXT, 'Hagyományos projekt­menedzsment tréningek')
    hyper_link_projectmanagement_agile = (By.XPATH, '//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/h2/a')
    hyper_link_projectmanagement_lean = (By.XPATH, '//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/h2/a')

    image_projectmanagement_traditional = (By.XPATH, '//*[@id="pagecontent"]/div/div[1]/div/div[1]/a')
    image_projectmanagement_agile = (By.XPATH, '//*[@id="pagecontent"]/div/div[2]/div/div[1]/a')
    image_projectmanagement_lean = (By.XPATH, '//*[@id="pagecontent"]/div/div[3]/div/div[1]/a')
################################################################################################################################################
    '''E_Learning'''
    hyper_link_owndev = (By.LINK_TEXT, 'Ismerje meg saját fejlesztésű e-learning tananyagainkat!')
    hyper_link_e_learning_lessons = (By.LINK_TEXT, 'Ismerje meg az E-learningtárat!')
    hyper_link_official = (By.LINK_TEXT, 'Ismerje meg hivatalos e-learning tananyagainkat!')
    hyper_link_mentored = (By.LINK_TEXT, 'Ismerje meg induló mentorált képzéseinket!')
    hyper_link_unique = (By.LINK_TEXT, 'Tudjon meg többet egyedi e-learning megoldásainkról!')

    hyper_link_owndev2 = (By.XPATH, '/html/body/main/div/p[2]/a[1]')
    hyper_link_e_learning_lessons2 = (By.XPATH, '/html/body/main/div/p[2]/a[2]')
    hyper_link_official2 = (By.XPATH, '/html/body/main/div/p[4]/a')
    hyper_link_mentored2 = (By.XPATH, '/html/body/main/div/p[6]/a')
    hyper_link_unique2 = (By.XPATH, '/html/body/main/div/p[8]/a')
################################################################################################################################################
    '''Login'''
    to_close_popup = (By.ID,'NewsletterModalCloseButton')
    nav_login_button = (By.XPATH, '//*[@id="navbar"]/div[3]/ul/li[3]')
    email = (By.ID,'Username')
    password = (By.ID,'Password')
    login_button = (By.ID,'LoginButton')
    signup_link = (By.LINK_TEXT,'Regisztráció')
    nav_bar_contacts = (By.XPATH,'//*[@id="PrimaryNavMainMenu"]/li[7]/a')
    message_btn1 = (By.XPATH,'//*[@id="sendMessage_submit"]')
################################################################################################################################################
    '''Mainpage_It_Courses_Dropdown'''
        # From IT Courses Dropdown Buttons
    btn_it_courses = (By.ID, 'MegaMenuIT') # 1
    btn_it_courses_xpath = (By.XPATH, '//*[@id="MegaMenuIT"]')
    btn_it_courses_admin = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/h4/a') # 1/a
    btn_it_courses_dev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/h4/a')   # 1/b
    btn_leader_courses = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[3]/h4/a')   # 1/c
    btn_creating_value = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[4]/h4/a')   # 1/d
    btn_office = (By.ID, 'MegaMenuOffice')        # 2
    btn_comp_man = (By.ID, 'MegaMenuERP')         # 3
    btn_car_start_p = (By.ID, 'MegaMenuKSP')      # 4/a
    btn_car_fy = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/h4/a')           
    btn_for_emp = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/h4/a')           # 4/b
    # 1/a
    btn_it_courses_admin_aws = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[1]')
    btn_it_courses_admin_microsoft = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[2]')
    btn_it_courses_admin_cisco = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[3]')
    btn_it_courses_admin_oracle = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[4]')
    btn_it_courses_admin_vmware = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[5]')
    btn_it_courses_admin_ibm = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[6]')
    btn_it_courses_admin_linux = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[7]')
    btn_it_courses_admin_other = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[8]')
    # 1/b
    btn_it_courses_dev_aws = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[1]')
    btn_it_courses_dev_micr = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[2]')
    btn_it_courses_dev_java = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[3]')
    btn_it_courses_dev_webdev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[4]')
    btn_it_courses_dev_mobdev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[5]')
    btn_it_courses_dev_pyth = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[6]')
    btn_it_courses_dev_other = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[7]')
    # 1/c
    btn_leader_courses_itil = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[3]/a[1]')
    btn_leader_courses_risk = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[3]/a[2]')
    btn_leader_courses_busn_an = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[3]/a[3]')
    # 1/d
    btn_creating_value_agile = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[4]/a[1]')
    btn_creating_value_devops = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[4]/a[2]')
    # 2
    btn_office_mo = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[2]/div/div/a[1]')
    btn_office_mo365 = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[2]/div/div/a[2]')
    btn_office_da = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[2]/div/div/a[3]')
    btn_office_gwc = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[2]/div/div/a[4]')
    # 3
    btn_comp_man_sap = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[3]/div/div/a[1]')
    btn_comp_man_sfc = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[3]/div/div/a[2]')
    # 4/a
    btn_car_fy_jun_dev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[1]')
    btn_car_fy_app_ad = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[2]')
    btn_car_fy_soft_test = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[3]')
    btn_car_fy_hir_proc = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[4]')
    btn_car_fy_apply = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[5]')
    btn_car_fy_faq = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[6]')
    # 4/b
    btn_for_emp_prog = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[1]')
    btn_for_emp_jun_dev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[2]')
    btn_for_emp_fin = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[3]')
    btn_for_emp_select = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[4]')
    btn_for_emp_grnt = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[5]')
################################################################################################################################################
    '''Mainpage_Trainings_Dropdown'''
    # From Trainings Dropdown Buttons
    btn_trainings = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[3]/h4[1]/a')
    btn_open_training_schedule = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[3]/h4[2]/a')
    btn_training_catalogue = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[3]/h4[3]/a')

    btn_project_management = (By.LINK_TEXT, 'Projektmenedzsment')
    btn_traditional_pm = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[2]/a[1]')
    btn_agile_pm = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[2]/a[2]')
    btn_lean = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[2]/a[3]')

    btn_soft_skill = (By.LINK_TEXT, 'Soft skill')
    btn_leader_training = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[1]/a[1]')
    btn_salesforce_training = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[1]/a[2]')
    btn_competence_training = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[1]/a[3]')
    btn_coaching_dropdown = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[1]/a[4]')
################################################################################################################################################
    '''Contact_Popupobj'''
    name_input = (By.XPATH,'/html/body/main/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div/input')
    email_input = (By.ID,'Email')
    msg_box_input = (By.ID,'Message')
    ticker = (By.XPATH,'//*[@id="MessageSendingForm"]/div[4]/label')
    message_btn1 = (By.XPATH,'//*[@id="sendMessage_submit"]')
################################################################################################################################################
    '''It_Courses'''
    btn_it_courses = (By.ID, 'PrimaryNavCourses')
################################################################################################################################################
    '''Trainings_Softskill'''
    btn_leader_trainings =(By.XPATH, '//*[@id="pagecontent"]/div/div[1]/div/div[2]/div/a')
    btn_salesforce_trainings = (By.XPATH, '//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/a')
    btn_competence_improvement_trainings = (By.XPATH, '//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/a')
    btn_coaching = (By.XPATH, '//*[@id="pagecontent"]/div/div[4]/div/div[2]/div/a')
################################################################################################################################################
    '''Trainings_Trainings'''
    btn_soft_skill_trainings = (By.XPATH, '//*[@id="pagecontent"]/div/div[1]/div/div[2]/div/a')
    btn_projectmanagement = (By.XPATH, '//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/a')
    btn_trainings_open_trainings_schedule = (By.XPATH, '//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/a')
    btn_trainings_catalogue = (By.XPATH, '//*[@id="pagecontent"]/div/div[4]/div/div[2]/div/a')

    hyper_link_soft_skill_trainings = (By.XPATH, '//*[@id="pagecontent"]/div/div[1]/div/div[2]/div/h2/a')
    hyper_link_projectmanagement = (By.XPATH, '//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/h2/a')
    hyper_link_trainings_open_trainings_schedule = (By.XPATH, '//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/h2/a')
    hyper_link_trainings_catalogue = (By.XPATH, '//*[@id="pagecontent"]/div/div[4]/div/div[2]/div/h2/a')

    image_soft_skill_trainings = (By.XPATH, '//*[@id="pagecontent"]/div/div[1]/div/div[1]/a')
    image_projectmanagement = (By.XPATH, '//*[@id="pagecontent"]/div/div[2]/div/div[1]/a')
    image_trainings_open_trainings_schedule = (By.XPATH, '//*[@id="pagecontent"]/div/div[3]/div/div[1]/a')
    image_trainings_catalogue = (By.XPATH, '//*[@id="pagecontent"]/div/div[4]/div/div[1]/a')