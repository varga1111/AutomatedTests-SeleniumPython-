from selenium import webdriver
import sys


class Testdata:

    PATH = '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Chrome_webdriver/chromedriver'

    to_print = 'setting up a test failed!'
    wrong_email = 'silvestr'
    empty_input = ""
    wrong_password = "sdfsd"
    
    #browser = webdriver.Chrome(PATH)
###################################################################################################################################################
   
    '''Page URLS (Body)'''
    # Main
    URL ='https://www.training360.com'
    # Login
    URL_LOGIN ='https://login.training360.com/Account/Login'
    # Trainings/
    TRAININGS_TRAININGS_URL = 'https://www.training360.com/treningek'
    TRAININGS_OPEN_TRAININGS_SCHEDULE_URL = 'https://www.training360.com/treningek/nyilt-trening-naptar'
    TRAININGS_TRAINING_CATALOGUE_URL = 'https://www.training360.com/treningek/katalogus'
    TRAININGS_SOFTSKILL_URL = 'https://www.training360.com/treningek/soft-skill'
    TRAININGS_SOFTSKILL_LEADER_TRAININGS_URL = 'https://www.training360.com/treningek/soft-skill/vezetoi'
    TRAININGS_SOFTSKILL_SALESFORCE_TRAININGS_URL = 'https://www.training360.com/treningek/soft-skill/ertekesitoi'
    TRAININGS_SOFTSKILL_COMPETENCE_IMPROVEMENT_TRAININGS_URL = 'https://www.training360.com/treningek/soft-skill/kompetenciafejleszto'
    TRAININGS_SOFTSKILL_COACHING_URL = 'https://www.training360.com/treningek/soft-skill/coaching'
    TRAININGS_PROJECTMANAGEMENT_URL = 'https://www.training360.com/treningek/projektmenedzsment'
    TRAININGS_PROJECTMANAGEMENT_TRADITIONAL_URL = 'https://www.training360.com/treningek/projektmenedzsment/hagyomanyos'
    TRAININGS_PROJECTMANAGEMENT_AGILE_URL = 'https://www.training360.com/treningek/projektmenedzsment/agilis'
    TRAININGS_PROJECTMANAGEMENT_LEAN_URL = 'https://www.training360.com/treningek/projektmenedzsment/lean'
    # E-Learning/
    E_LEARNING_URL = 'https://www.training360.com/e-learning'
    E_LEARNING_OWNDEV_URL = 'https://www.training360.com/e-learning/sajatfejlesztesu'
    E_LEARNING_OFFICIAL_URL = 'https://www.training360.com/e-learning/hivatalos'
    E_LEARNING_UNIQUE_URL = 'https://www.training360.com/e-learning/egyedi'
    MENTORED_COURSES_URL = 'https://www.training360.com/mentoralt-kepzesek'
    # E-Learning/Owndev/
    E_LEARNING_OWNDEV_OFFICE_URL = 'https://www.training360.com/e-learning/sajatfejlesztesu/office'
    E_LEARNING_OWNDEV_IT_AWARENESS_URL = 'https://www.training360.com/e-learning/sajatfejlesztesu/informatikai-tudatossag'
    E_LEARNING_OFFICIAL_URL = 'https://www.training360.com/e-learning/hivatalos'
    # IT Courses/
    IT_COURSES_URL = 'https://www.training360.com/informatikai-kepzesek'
    IT_COURSES_ADMIN_URL = 'https://www.training360.com/informatikai-kepzesek/uzemeltetoi'
    IT_COURSES_ADMIN_AWS_URL = 'https://www.training360.com/informatikai-kepzesek/uzemeltetoi/aws'
    IT_COURSES_ADMIN_MICROSOFT_URL = 'https://www.training360.com/informatikai-kepzesek/uzemeltetoi/microsoft'
    IT_COURSES_ADMIN_CISCO_URL = 'https://www.training360.com/informatikai-kepzesek/uzemeltetoi/cisco'
    IT_COURSES_ADMIN_ORACLE_URL = 'https://www.training360.com/informatikai-kepzesek/uzemeltetoi/oracle'
    IT_COURSES_ADMIN_VMWARE_URL = 'https://www.training360.com/informatikai-kepzesek/uzemeltetoi/vmware'
    IT_COURSES_ADMIN_IBM_URL = 'https://www.training360.com/informatikai-kepzesek/uzemeltetoi/ibm'
    IT_COURSES_ADMIN_LINUX_URL = 'https://www.training360.com/informatikai-kepzesek/uzemeltetoi/linux'
    IT_COURSES_ADMIN_OTHER_URL = 'https://www.training360.com/informatikai-kepzesek/uzemeltetoi/egyeb'
    
    IT_COURSES_DEVELOPER_URL = 'https://www.training360.com/informatikai-kepzesek/fejlesztoi'
    IT_COURSES_DEVELOPER_AWS_URL = 'https://www.training360.com/informatikai-kepzesek/fejlesztoi/aws'
    IT_COURSES_DEVELOPER_MICROSOFT_URL = 'https://www.training360.com/informatikai-kepzesek/fejlesztoi/microsoft'
    IT_COURSES_DEVELOPER_JAVA_URL = 'https://www.training360.com/informatikai-kepzesek/fejlesztoi/java'
    IT_COURSES_DEVELOPER_WEBDEV_URL = 'https://www.training360.com/informatikai-kepzesek/fejlesztoi/web'
    IT_COURSES_DEVELOPER_MOBILE_URL = 'https://www.training360.com/informatikai-kepzesek/fejlesztoi/mobil-alkalmazas'
    IT_COURSES_DEVELOPER_PYTHON_URL = 'https://www.training360.com/informatikai-kepzesek/fejlesztoi/python?sp=true'
    IT_COURSES_DEVELOPER_OTHER_URL = 'https://www.training360.com/informatikai-kepzesek/fejlesztoi/egyeb'
    
    IT_COURSES_LEADER_URL = 'https://www.training360.com/informatikai-kepzesek/vezetoi'
    IT_COURSES_LEADER_ITIL_PRINCE2_URL = 'https://www.training360.com/informatikai-kepzesek/vezetoi/itil-prince2'
    IT_COURSES_LEADER_RISK_MANAGEMENT_INF_SECURITY_IMPORTER_MANAGEMENT_URL = 'https://www.training360.com/informatikai-kepzesek/vezetoi/kockazatkezeles-informaciovedelem-beszallitokezeles'
    IT_COURSES_LEADER_BUSINESS_ANALYST_URL = 'https://www.training360.com/informatikai-kepzesek/vezetoi/business-analyst-uzleti-elemzo'
    
    IT_COURSES_CREATING_VALUE_URL = 'https://www.training360.com/informatikai-kepzesek/hatekony-ertekteremtes'
    IT_COURSES_CREATING_VALUE_AGILE_URL = 'https://www.training360.com/treningek/projektmenedzsment/agilis'
    IT_COURSES_CREATING_VALUE_DEVOPS_URL = 'https://www.training360.com/informatikai-kepzesek/hatekony-ertekteremtes/devops'
    
    OFFICE_IT_URL = 'https://www.training360.com/irodai-informatika'
    OFFICE_IT_MICROSOFT_OFFICE_URL = 'https://www.training360.com/irodai-informatika/office'
    OFFICE_IT_MICROSOFT_OFFICE_365_URL = 'https://www.training360.com/irodai-informatika/office-365'
    OFFICE_IT_DATAANALYST_COURSES_URL = 'https://www.training360.com/irodai-informatika/bi'
    OFFICE_IT_GOOGLE_WORKSPACE_COURSES_URL = 'https://www.training360.com/irodai-informatika/google-workspace'
    
    COMPANY_MANAGEMENT_URL = 'https://www.training360.com/vallalatiranyitasi-erp-tanfolyamok'
    COMPANY_MANAGEMENT_SAP_COURSES_URL = 'https://www.training360.com/vallalatiranyitasi-erp-tanfolyamok/sap'
    COMPANY_MANAGEMENT_SALESFORCE_COURSES_URL = 'https://www.training360.com/vallalatiranyitasi-erp-tanfolyamok'
    
    CAREER_START_PROGRAM_URL = 'https://karrier.training360.com'
    CAREER_START_PROGRAM_FOR_YOU_URL = 'https://karrierstart.training360.com'
    CAREER_START_PROGRAM_FOR_YOU_JUNIOR_DEV_COURSE_URL = 'https://karrierstart.training360.com/junior-fejleszto-kepzes/'
    CAREER_START_PROGRAM_FOR_YOU_APPLICATION_ADMIN_URL = 'https://karrierstart.training360.com/junior-alkalmazas-uzemelteto-kepzes-es-allaslehetoseg/'
    CAREER_START_PROGRAM_FOR_YOU_SOFTWARE_TESTER_URL = 'https://karrierstart.training360.com/szoftvertesztelo/'
    CAREER_START_PROGRAM_FOR_YOU_HIRING_PROCESS_URL = 'https://karrierstart.training360.com/felveteli/'
    CAREER_START_PROGRAM_FOR_YOU_APPYING_URL = 'https://karrierstart.training360.com/jelentkezes/'
    CAREER_START_PROGRAM_FOR_YOU_FAQ_URL = 'https://karrierstart.training360.com/gyakran-ismetelt-kerdesek/'
    
    CAREER_START_PROGRAM_FOR_EMPLOYERS_URL = 'https://karrierprogram.training360.com'
    CAREER_START_PROGRAM_FOR_EMPLOYERS_ABOUT_THE_PROGRAM_URL = 'https://karrierprogram.training360.com/informatikai-fejlesztoi-karrier-start-program/'
    CAREER_START_PROGRAM_FOR_EMPLOYERS_WHAT_A_JUNIOR_KNOWS_URL = 'https://karrierprogram.training360.com/mit-tud-egy-junior-fejleszto/'
    CAREER_START_PROGRAM_FOR_EMPLOYERS_FINANCING_AND_EMPLOYING_MODELL_URL = 'https://karrierprogram.training360.com/finanszirozasi-es-foglalkoztatasi-modell/'
    CAREER_START_PROGRAM_FOR_EMPLOYERS_GARENTEES_URL = 'https://karrierprogram.training360.com/garanciak/'
    
    # Course Schedules
    COURSE_SCHEDULES_URL = 'https://www.training360.com/tanfolyami-naptar'
    # Discounts/
    DISCOUNTS_URL = 'https://www.training360.com/akciok'
    DISCOUNTS_AZURE_URL = 'https://www.training360.com/akciok/azure-es-cisco-ccna-tanfolyam-ajandek-vizsga-gyakorloteszttel'
    DISCOUNTS_WINDOWS_SERVER_URL = 'https://www.training360.com/akciok/windows-server-2019-ujdonsagok-uzemeltetoknek-premium-videos-tananyaggal'
    # Contacts
    CONTACTS_URL = 'https://www.training360.com/kapcsolat'
    # Cart
    CART_URL = 'https://www.training360.com/kosar'


    '''Page URLS (Footer)'''
    # News
    NEWS_URL = 'https://www.training360.com/hirek'

#######################################################################################################################################################
    
    '''Page Titles'''
    MAIN_PAGE_TITLE = 'Training360 - Informatikai tanfolyamok, szervezetfejlesztési megoldások, vezetői és soft skill tréningek, irodai képzések, vizsgák - Training360'
    LOGIN_PAGE_TITLE = 'Bejelentkezés - Training360'
    AFTER_LOGIN_PAGE_TITLE = 'Az oldal nem található - Training360'

    # Trainings Dropdown Page Titles
    TRAININGS_SOFTSKILL_TITLE = 'Soft skill tréningek - Training360' 
    TRAININGS_PROJECTMANAGEMENT_TITLE = 'Projektmenedzsment tréningek - Training360' 
    TRAININGS_TRAININGS_TITLE = 'Tréningek - Training360'

    TRAININGS_SOFTSKILL_LEADER_TITLE = 'Vezetői tréningek - Training360'
    TRAININGS_SOFTSKILL_SALESFORCE_TITLE = 'Értékesítői tréningek - Training360'
    TRAININGS_SOFTSKILL_COMPETENCE_TITLE = 'Kompetenciafejlesztő tréningek - Training360'
    TRAININGS_SOFTSKILL_COACHING_TITLE = 'Coaching - Training360'

    TRAININGS_PROJECTMANAGEMENT_TRADITIONAL_TITLE = 'Hagyományos projektmenedzsment tréningek - Training360'
    TRAININGS_PROJECTMANAGEMENT_AGILE_TITLE = 'Agilis menedzsment és digitális üzlet akadémia - Training360'
    TRAININGS_PROJECTMANAGEMENT_LEAN_TITLE = 'LEAN képzések - Training360'

    TRAININGS_OPEN_SCHEDULE_TITLE = 'Nyílt tréning naptár - Training360'
    TRAININGS_CATALOGUE_TITLE = 'Tréning katalógus - Training360'

    # E-Learning/
    E_LEARNING_TITLE = 'E-learning - Training360'
    E_LEARNING_OWNDEV_TITLE = 'Saját fejlesztésű e-learning tananyagok - Training360'
    E_LEARNING_OFFICIAL_TITLE = 'Hivatalos e-learning tananyagok - Training360'
    E_LEARNING_UNIQUE_TITLE = 'Egyedi e-learning megoldások és szolgáltatások - Training360'
    MENTORED_COURSES_TITLE = 'Mentorált képzések - Training360'

    COURSE_SCHEDULES_TITLE ='Tanfolyami naptár - Training360'
    DISCOUNTS_TITLE = 'Akciók - Training360'
    NEWS_TITLE = 'Híreink - Training360'
    CONTACTS_TITLE = 'Kapcsolat - Training360'

    # IT_Courses
    IT_COURSES_TITLE = 'Informatikai képzések - Training360'

############################################################################################################################
    SUBJECTS_TOTAL = 408
########################################################################################################################################################
    
    '''Input Data'''

    #Login Page username
    USERNAME ='silvester.arpad.varga@gmail.com'
    INCORRECT_USERNAME = 'silvest'

    #Login Page password
    with open('/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Configs/password.txt', 'r') as file:
        for read in file:
            PASSWORD = read
            

    # Searchbar Queries | https://training360.com/(all pages with this root)
    SEARCHBAR_LESSON1 = 'Szoftvertesztelő'

    # Message to Company Inputs | https://www.training360.com/kapcsolat
    #name
    NAME = 'Varga Árpád Szilveszter'
    NAME = 'Varga Arpad Szilveszter'
    #emaiil
    EMAIL = 'silvester.arpad.varga@gmail.com'
    #textarea(message)
    MESSAGE = 'This is my message to the company. Thank you.'