from selenium.webdriver.common.by import By
from basemethods import Base_methods


class Locators(Base_methods):
    '''MainPage '''
#URL Link Locators    (Link Buttons that navigate to new Pages, '#' Stays on same Page with new Page Object Probably)
#    Unit          Navigation
btn_xpath_unit1, btn_link_txt_1 = (By.XPATH,'//a[contains(@href,"/")]'),(By.XPATH,'/')#None - http://training360.com/
btn_xpath_unit2, btn_xpath_nav2 = (By.XPATH,'//a[contains(@href,"#")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/a')#Tréningek - http://training360.com
btn_xpath_unit3, btn_xpath_nav3 = (By.XPATH,'//a[contains(@href,"/treningek/soft-skill")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[1]/h4/a')#Soft skill - http://training360.com/treningek/soft-skill
btn_xpath_unit4, btn_xpath_nav4 = (By.XPATH,'//a[contains(@href,"/treningek/soft-skill/vezetoi")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[1]/a[1]')#Vezetői tréningek - http://training360.com/treningek/soft-skill/vezetoi
btn_xpath_unit5, btn_xpath_nav5 = (By.XPATH,'//a[contains(@href,"/treningek/soft-skill/ertekesitoi")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[1]/a[2]')#Értékesítői tréningek - http://training360.com/treningek/soft-skill/ertekesitoi
btn_xpath_unit6, btn_xpath_nav6 = (By.XPATH,'//a[contains(@href,"/treningek/soft-skill/kompetenciafejleszto")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[1]/a[3]')#Kompetencia­fejlesztő tréningek - http://training360.com/treningek/soft-skill/kompetenciafejleszto
btn_xpath_unit7, btn_xpath_nav7 = (By.XPATH,'//a[contains(@href,"/treningek/soft-skill/coaching")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[1]/a[4]')#Coaching - http://training360.com/treningek/soft-skill/coaching
btn_xpath_unit8, btn_xpath_nav8 = (By.XPATH,'//a[contains(@href,"/treningek/projektmenedzsment")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[2]/h4/a')#Projektmenedzsment - http://training360.com/treningek/projektmenedzsment
btn_xpath_unit9, btn_xpath_nav9 = (By.XPATH,'//a[contains(@href,"/treningek/projektmenedzsment/hagyomanyos")]'),(By.XPATH,'/')#None - http://training360.com/treningek/projektmenedzsment/hagyomanyos
btn_xpath_unit10, btn_xpath_nav10 = (By.XPATH,'//a[contains(@href,"/treningek/projektmenedzsment/agilis")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[2]/a[2]')#Agilis projekt­menedzsment - http://training360.com/treningek/projektmenedzsment/agilis
btn_xpath_unit11, btn_xpath_nav11 = (By.XPATH,'//a[contains(@href,"/treningek/projektmenedzsment/lean")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[2]/a[3]')#LEANhttp://training360.com/treningek/projektmenedzsment/lean
btn_xpath_unit12, btn_xpath_nav12 = (By.XPATH,'//a[contains(@href,"/treningek")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/a')#Tréningek - http://training360.com/treningek
btn_xpath_unit13, btn_xpath_nav13 = (By.XPATH,'//a[contains(@href,"/treningek/nyilt-trening-naptar")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[3]/h4[2]/a')#Nyílt tréning naptárhttp://training360.com/treningek/nyilt-trening-naptar
btn_xpath_unit14, btn_xpath_nav14 = (By.XPATH,'//a[contains(@href,"/treningek/katalogus")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[3]/h4[3]/a')#Tréning katalógus - http://training360.com/treningek/katalogus
btn_xpath_unit15, btn_xpath_nav15 = (By.XPATH,'//a[contains(@href,"/e-learning")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[2]/a')#E-learning - http://training360.com/e-learning
btn_xpath_unit16, btn_xpath_nav16 = (By.XPATH,'//a[contains(@href,"#")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/a')#IT Képzések - http://training360.com
btn_xpath_unit17, btn_xpath_nav17 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[1]/ul/li[1]/a')#Informatikai képzések - http://training360.com/informatikai-kepzesek
btn_xpath_unit18, btn_xpath_nav18 = (By.XPATH,'//a[contains(@href,"/irodai-informatika")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[1]/ul/li[2]/a')#Irodai informatika - http://training360.com/irodai-informatika
btn_xpath_unit19, btn_xpath_nav19 = (By.XPATH,'//a[contains(@href,"/vallalatiranyitasi-erp-tanfolyamok")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[1]/ul/li[3]/a')#Vállalatirányítás (ERP) - http://training360.com/vallalatiranyitasi-erp-tanfolyamok
btn_xpath_unit20, btn_xpath_nav20 = (By.XPATH,'//a[contains(@href,"https://karrier.training360.com/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[1]/ul/li[4]/a')#Karrier Start Programhttps://karrier.training360.com/
btn_xpath_unit21, btn_xpath_nav21 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/h4/a')#IT üzemeltetői képzések - http://training360.com/informatikai-kepzesek/uzemeltetoi
btn_xpath_unit22, btn_xpath_nav22 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/aws")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/a[1]')#Amazon Web Services (AWS) - http://training360.com/informatikai-kepzesek/uzemeltetoi/aws
btn_xpath_unit23, btn_xpath_nav23 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/microsoft")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/a[2]')#Microsoft - http://training360.com/informatikai-kepzesek/uzemeltetoi/microsoft
btn_xpath_unit24, btn_xpath_nav24 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/cisco")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/a[3]')#Cisco - http://training360.com/informatikai-kepzesek/uzemeltetoi/cisco
btn_xpath_unit25, btn_xpath_nav25 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/oracle")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/a[4]')#Oracle - http://training360.com/informatikai-kepzesek/uzemeltetoi/oracle
btn_xpath_unit26, btn_xpath_nav26 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/vmware")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/a[5]')#VMware - http://training360.com/informatikai-kepzesek/uzemeltetoi/vmware
btn_xpath_unit27, btn_xpath_nav27 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/ibm")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/a[6]')#IBM - http://training360.com/informatikai-kepzesek/uzemeltetoi/ibm
btn_xpath_unit28, btn_xpath_nav28 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/linux")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/a[7]')#Linux - http://training360.com/informatikai-kepzesek/uzemeltetoi/linux
btn_xpath_unit29, btn_xpath_nav29 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/egyeb")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/a[8]')#Egyéb (Grafana, Juniper, …) - http://training360.com/informatikai-kepzesek/uzemeltetoi/egyeb
btn_xpath_unit30, btn_xpath_nav30 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[2]/h4/a')#IT fejlesztői képzések - http://training360.com/informatikai-kepzesek/fejlesztoi
btn_xpath_unit31, btn_xpath_nav31 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi/aws")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[1]/a[1]')#Amazon Web Services (AWS) - http://training360.com/informatikai-kepzesek/fejlesztoi/aws
btn_xpath_unit32, btn_xpath_nav32 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi/microsoft")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[2]/a[2]')#Microsoft (C#, ASP.NET, stb.) - http://training360.com/informatikai-kepzesek/fejlesztoi/microsoft
btn_xpath_unit33, btn_xpath_nav33 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi/java")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[2]/a[3]')#Java - http://training360.com/informatikai-kepzesek/fejlesztoi/java
btn_xpath_unit34, btn_xpath_nav34 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi/web")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[2]/a[4]')#Webfejlesztés - http://training360.com/informatikai-kepzesek/fejlesztoi/web
btn_xpath_unit35, btn_xpath_nav35 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi/mobil-alkalmazas")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[2]/a[5]')#Mobil alkalmazás fejlesztés - http://training360.com/informatikai-kepzesek/fejlesztoi/mobil-alkalmazas
btn_xpath_unit36, btn_xpath_nav36 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi/python")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[2]/a[6]')#Python programozás - http://training360.com/informatikai-kepzesek/fejlesztoi/python
btn_xpath_unit37, btn_xpath_nav37 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi/egyeb")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[2]/a[7]')#Egyéb (Biztonság, tesztelés, Blockchain, UML) - http://training360.com/informatikai-kepzesek/fejlesztoi/egyeb
btn_xpath_unit38, btn_xpath_nav38 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/vezetoi")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[3]/h4/a')#IT vezetői képzések - http://training360.com/informatikai-kepzesek/vezetoi
btn_xpath_unit39, btn_xpath_nav39 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/vezetoi/itil-prince2")]'),(By.XPATH,'/')#None - http://training360.com/informatikai-kepzesek/vezetoi/itil-prince2
btn_xpath_unit40, btn_xpath_nav40 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/vezetoi/kockazatkezeles-informaciovedelem-beszallitokezeles")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[3]/a[2]')#Kockázatkezelés, információvédelem, beszállítókezelés - http://training360.com/informatikai-kepzesek/vezetoi/kockazatkezeles-informaciovedelem-beszallitokezeles
btn_xpath_unit41, btn_xpath_nav41 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/vezetoi/business-analyst-uzleti-elemzo")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[3]/a[3]')#Business Analyst (Üzleti Elemző) - http://training360.com/informatikai-kepzesek/vezetoi/business-analyst-uzleti-elemzo
btn_xpath_unit42, btn_xpath_nav42 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/hatekony-ertekteremtes")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[4]/h4/a')#Hatékony értékteremtés - http://training360.com/informatikai-kepzesek/hatekony-ertekteremtes
btn_xpath_unit43, btn_xpath_nav43 = (By.XPATH,'//a[contains(@href,"/treningek/projektmenedzsment/agilis")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[1]/div/div/div[2]/a[2]')#Agilis - http://training360.com/treningek/projektmenedzsment/agilis
btn_xpath_unit44, btn_xpath_nav44 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/hatekony-ertekteremtes/devops")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[1]/div/div[4]/a[2]')#DevOps - http://training360.com/informatikai-kepzesek/hatekony-ertekteremtes/devops
btn_xpath_unit45, btn_xpath_nav45 = (By.XPATH,'//a[contains(@href,"/irodai-informatika/office")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[2]/div/div/a[1]')#Microsoft Office - http://training360.com/irodai-informatika/office
btn_xpath_unit46, btn_xpath_nav46 = (By.XPATH,'//a[contains(@href,"/irodai-informatika/office-365")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[2]/div/div/a[2]')#Microsoft Office 365http://training360.com/irodai-informatika/office-365
btn_xpath_unit47, btn_xpath_nav47 = (By.XPATH,'//a[contains(@href,"/irodai-informatika/bi")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[2]/div/div/a[3]')#Adatelemző (BI) tanfolyamok - http://training360.com/irodai-informatika/bi
btn_xpath_unit48, btn_xpath_nav48 = (By.XPATH,'//a[contains(@href,"/irodai-informatika/google-workspace")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[2]/div/div/a[4]')#Google Workspace tanfolyamok - http://training360.com/irodai-informatika/google-workspace
btn_xpath_unit49, btn_xpath_nav49 = (By.XPATH,'//a[contains(@href,"/vallalatiranyitasi-erp-tanfolyamok/sap")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[3]/div/div/a[1]')#SAP tanfolyamok - http://training360.com/vallalatiranyitasi-erp-tanfolyamok/sap
btn_xpath_unit50, btn_xpath_nav50 = (By.XPATH,'//a[contains(@href,"/vallalatiranyitasi-erp-tanfolyamok")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[3]/div/div/a[2]')#Salesforce tanfolyamok - http://training360.com/vallalatiranyitasi-erp-tanfolyamok
btn_xpath_unit51, btn_xpath_nav51 = (By.XPATH,'//a[contains(@href,"https://karrierstart.training360.com/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[1]/h4/a')#Neked - https://karrierstart.training360.com/
btn_xpath_unit52, btn_xpath_nav52 = (By.XPATH,'//a[contains(@href,"https://karrierstart.training360.com/junior-fejlesztokepzes/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[1]/a[1]')#Junior fejlesztő képzés - https://karrierstart.training360.com/junior-fejlesztokepzes/
btn_xpath_unit53, btn_xpath_nav53 = (By.XPATH,'//a[contains(@href,"https://karrierstart.training360.com/junior-alkalmazas-uzemelteto-kepzes-es-allaslehetoseg/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[1]/a[2]')#Alkalmazás-üzemeltető - https://karrierstart.training360.com/junior-alkalmazas-uzemelteto-kepzes-es-allaslehetoseg/
btn_xpath_unit54, btn_xpath_nav54 = (By.XPATH,'//a[contains(@href,"https://karrierstart.training360.com/szoftvertesztelo/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[1]/a[3]')#Szoftvertesztelő - https://karrierstart.training360.com/szoftvertesztelo/
btn_xpath_unit55, btn_xpath_nav55 = (By.XPATH,'//a[contains(@href,"https://karrierstart.training360.com/felveteli/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[1]/a[4]')#Felvételi folyamat - https://karrierstart.training360.com/felveteli/
btn_xpath_unit56, btn_xpath_nav56 = (By.XPATH,'//a[contains(@href,"https://karrierstart.training360.com/jelentkezes/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[1]/a[5]')#Jelentkezés - https://karrierstart.training360.com/jelentkezes/
btn_xpath_unit57, btn_xpath_nav57 = (By.XPATH,'//a[contains(@href,"https://karrierstart.training360.com/gyakran-ismetelt-kerdesek/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[1]/a[6]')#GYIK - https://karrierstart.training360.com/gyakran-ismetelt-kerdesek/
btn_xpath_unit58, btn_xpath_nav58 = (By.XPATH,'//a[contains(@href,"https://karrierprogram.training360.com/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[2]/h4/a')#Munkáltatóknak - https://karrierprogram.training360.com/
btn_xpath_unit59, btn_xpath_nav59 = (By.XPATH,'//a[contains(@href,"https://karrierprogram.training360.com/informatikai-fejlesztoi-karrier-start-program/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[2]/a[1]')#A programról - https://karrierprogram.training360.com/informatikai-fejlesztoi-karrier-start-program/
btn_xpath_unit60, btn_xpath_nav60 = (By.XPATH,'//a[contains(@href,"https://karrierprogram.training360.com/mit-tud-egy-junior-fejleszto/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[2]/a[2]')#Mit tud egy junior fejlesztő? - https://karrierprogram.training360.com/mit-tud-egy-junior-fejleszto/
btn_xpath_unit61, btn_xpath_nav61 = (By.XPATH,'//a[contains(@href,"https://karrierprogram.training360.com/finanszirozasi-es-foglalkoztatasi-modell/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[2]/a[3]')#Finanszírozási és foglalkoztatási modell - https://karrierprogram.training360.com/finanszirozasi-es-foglalkoztatasi-modell/
btn_xpath_unit62, btn_xpath_nav62 = (By.XPATH,'//a[contains(@href,"https://karrierprogram.training360.com/hogyan-valasztjuk-ki-a-legjobbakat/")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[2]/a[4]')#Kiválasztási folyamat - https://karrierprogram.training360.com/hogyan-valasztjuk-ki-a-legjobbakat/
btn_xpath_unit63, btn_xpath_nav63 = (By.XPATH,'//a[contains(@href,"https://karrierprogram.training360.com/garanciak")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[2]/a[5]')#Garanciák - https://karrierprogram.training360.com/garanciak
btn_xpath_unit64, btn_xpath_nav64 = (By.XPATH,'//a[contains(@href,"#")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[4]/a')#Vizsgák - http://training360.com
btn_xpath_unit65, btn_xpath_nav65 = (By.XPATH,'//a[contains(@href,"/vizsgak")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[4]/div/a[1]')#Vizsgainformációk - http://training360.com/vizsgak
btn_xpath_unit66, btn_xpath_nav66 = (By.XPATH,'//a[contains(@href,"/vizsgak/jelentkezes")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[4]/div/a[2]')#Jelentkezés vizsgára - http://training360.com/vizsgak/jelentkezes
btn_xpath_unit67, btn_xpath_nav67 = (By.XPATH,'//a[contains(@href,"/vizsgak/gyakran-ismetelt-kerdesek")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[3]/div/div/div[2]/div[4]/div/div[1]/a[6]')#GYIK - http://training360.com/vizsgak/gyakran-ismetelt-kerdesek
btn_xpath_unit68, btn_xpath_nav68 = (By.XPATH,'//a[contains(@href,"/tanfolyami-naptar")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[5]/a')#Tanfolyami naptár - http://training360.com/tanfolyami-naptar
btn_xpath_unit69, btn_xpath_nav69 = (By.XPATH,'//a[contains(@href,"/akciok")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[6]/a')#Akciók - http://training360.com/akciok
btn_xpath_unit70, btn_xpath_nav70 = (By.XPATH,'//a[contains(@href,"/kapcsolat")]'),(By.XPATH,'/html/body/nav/div[2]/ul/li[7]/a')#Kapcsolat - http://training360.com/kapcsolat
btn_xpath_unit71, btn_xpath_nav71 = (By.XPATH,'//a[contains(@href,"#")]'),(By.XPATH,'/')#None - http://training360.com
btn_xpath_unit72, btn_xpath_nav72 = (By.XPATH,'//a[contains(@href,"/kosar")]'),(By.XPATH,'/')#None - http://training360.com/kosar
btn_xpath_unit73, btn_xpath_nav73 = (By.XPATH,'//a[contains(@href,"/login")]'),(By.XPATH,'/')#None - http://training360.com/login
btn_xpath_unit74, btn_xpath_nav74 = (By.XPATH,'//a[contains(@href,"#")]'),(By.XPATH,'/')#None - http://training360.com
btn_xpath_unit75, btn_xpath_nav75 = (By.XPATH,'//a[contains(@href,"/hirek/hivatalos-amazon-web-services-oktatokozpont-lett-a-training360")]'),(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div[2]/a')#Továbbhttp://training360.com/hirek/hivatalos-amazon-web-services-oktatokozpont-lett-a-training360
btn_xpath_unit76, btn_xpath_nav76 = (By.XPATH,'//a[contains(@href,"/tanfolyami-naptar?tocs=lvc")]'),(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/a[1]')#LVC tanfolyamok - http://training360.com/tanfolyami-naptar?tocs=lvc
btn_xpath_unit77, btn_xpath_nav77 = (By.XPATH,'//a[contains(@href,"/tanfolyami-naptar?tocs=lvc&sg=true")]'),(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/a[2]')#Biztosan indul - http://training360.com/tanfolyami-naptar?tocs=lvc&sg=true
btn_xpath_unit78, btn_xpath_nav78 = (By.XPATH,'//a[contains(@href,"/lvc")]'),(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/a[3]')#Ismertető - http://training360.com/lvc
btn_xpath_unit79, btn_xpath_nav79 = (By.XPATH,'//a[contains(@href,"/allasajanlatok")]'),(By.XPATH,'/html/body/div[2]/div/div[3]/div/div[2]/div[2]/a')#Állásajánlataink - http://training360.com/allasajanlatok
btn_xpath_unit80, btn_xpath_nav80 = (By.XPATH,'//a[contains(@href,"/letoltes/training360-ugyfeltajekoztato-2022-03-31.pdf")]'),(By.XPATH,'/')#None - http://training360.com/letoltes/training360-ugyfeltajekoztato-2022-03-31.pdf
btn_xpath_unit81, btn_xpath_nav81 = (By.XPATH,'//a[contains(@href,"/kepzes/ANS")]'),(By.XPATH,'/html/body/main/section[2]/div/div/div/div/div[6]/div/div/div/a')#Ansible - http://training360.com/kepzes/ANS
btn_xpath_unit82, btn_xpath_nav82 = (By.XPATH,'//a[contains(@href,"/kepzes/TRAZ-305-SA2")]'),(By.XPATH,'/html/body/main/section[2]/div/div/div/div/div[1]/div/div/div/a')#Azure Solution Architect megoldások tervezése - http://training360.com/kepzes/TRAZ-305-SA2
btn_xpath_unit83, btn_xpath_nav83 = (By.XPATH,'//a[contains(@href,"/kepzes/SHP16-20339-1")]'),(By.XPATH,'/html/body/main/section[2]/div/div/div/div/div[2]/div/div/div/a')#Microsoft SharePoint 2016 infrastruktúra tervezése és üzemeltetése - http://training360.com/kepzes/SHP16-20339-1
btn_xpath_unit84, btn_xpath_nav84 = (By.XPATH,'//a[contains(@href,"/kepzes/TRMS-040-ONE")]'),(By.XPATH,'/html/body/main/section[2]/div/div/div/div/div[3]/div/div/div/a')#SharePoint és OneDrive menedzselése Microsoft 365 platformonhttp://training360.com/kepzes/TRMS-040-ONE
btn_xpath_unit85, btn_xpath_nav85 = (By.XPATH,'//a[contains(@href,"/kepzes/JAVAX-CI")]'),(By.XPATH,'/html/body/main/section[2]/div/div/div/div/div[4]/div/div/div/a')#CI/CD implementálása Java projekten, Maven, Jenkins és Docker eszközökkel - http://training360.com/kepzes/JAVAX-CI
btn_xpath_unit86, btn_xpath_nav86 = (By.XPATH,'//a[contains(@href,"/kepzes/PBI-K")]'),(By.XPATH,'/html/body/main/section[2]/div/div/div/div/div[5]/div/div/div/a')#Kezdő Power BI - http://training360.com/kepzes/PBI-K
btn_xpath_unit87, btn_xpath_nav87 = (By.XPATH,'//a[contains(@href,"/hirek/amazon-web-services-training-partnerek-vagyunk")]'),(By.XPATH,'/html/body/main/section[3]/div/div/div[2]/div/div[2]/h3')#Amazon Web Services Training Partnerek vagyunk - http://training360.com/hirek/amazon-web-services-training-partnerek-vagyunk
btn_xpath_unit88, btn_xpath_nav88 = (By.XPATH,'//a[contains(@href,"/hirek/mit-rejt-a-microsoft-csodafegyvere-a-power-platform")]'),(By.XPATH,'/html/body/main/section[3]/div/div/div[3]/div/div[2]/h3')#Mit rejt a Microsoft csodafegyvere, a Power Platform?http://training360.com/hirek/mit-rejt-a-microsoft-csodafegyvere-a-power-platform
btn_xpath_unit89, btn_xpath_nav89 = (By.XPATH,'//a[contains(@href,"/hirek/itil4-everything-avagy-hova-tunt-a-v-betu-az-itil-bol")]'),(By.XPATH,'/html/body/main/section[3]/div/div/div[4]/div/div[2]/h3')#ITIL® 4 Everything – avagy hova tűnt a „v” betű az ITIL®-ből?http://training360.com/hirek/itil4-everything-avagy-hova-tunt-a-v-betu-az-itil-bol
btn_xpath_unit90, btn_xpath_nav90 = (By.XPATH,'//a[contains(@href,"/marslander")]'),(By.XPATH,'/')#None - http://training360.com/marslander
btn_xpath_unit91, btn_xpath_nav91 = (By.XPATH,'//a[contains(@href,"/hirek/a-nagy-vmware-vsphere-korhinta")]'),(By.XPATH,'/html/body/main/section[3]/div/div/div[5]/div/div[2]/h3')#A Nagy VMware vSphere Körhinta - http://training360.com/hirek/a-nagy-vmware-vsphere-korhinta
btn_xpath_unit92, btn_xpath_nav92 = (By.XPATH,'//a[contains(@href,"/hirek")]'),(By.XPATH,'/html/body/main/section[3]/div/div/div[6]/a')#Tovább a hírekhez - http://training360.com/hirek
btn_xpath_unit93, btn_xpath_nav93 = (By.XPATH,'//a[contains(@href,"/aws")]'),(By.XPATH,'/')#None - http://training360.com/aws
btn_xpath_unit94, btn_xpath_nav94 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/cisco")]'),(By.XPATH,'/')#None - http://training360.com/informatikai-kepzesek/uzemeltetoi/cisco
btn_xpath_unit95, btn_xpath_nav95 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/vmware")]'),(By.XPATH,'/')#None - http://training360.com/informatikai-kepzesek/uzemeltetoi/vmware
btn_xpath_unit96, btn_xpath_nav96 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/oracle")]'),(By.XPATH,'/')#None - http://training360.com/informatikai-kepzesek/uzemeltetoi/oracle
btn_xpath_unit97, btn_xpath_nav97 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/uzemeltetoi/ibm")]'),(By.XPATH,'/')#None - http://training360.com/informatikai-kepzesek/uzemeltetoi/ibm
btn_xpath_unit98, btn_xpath_nav98 = (By.XPATH,'//a[contains(@href,"/vizsgak/pearson-vue-vizsgakozpont")]'),(By.XPATH,'/')#None - http://training360.com/vizsgak/pearson-vue-vizsgakozpont
btn_xpath_unit99, btn_xpath_nav99 = (By.XPATH,'//a[contains(@href,"/vizsgak/certiport-vizsgakozpont")]'),(By.XPATH,'/')#None - http://training360.com/vizsgak/certiport-vizsgakozpont
btn_xpath_unit100, btn_xpath_nav100 = (By.XPATH,'//a[contains(@href,"/vizsgak/peoplecert-vizsgakozpont")]'),(By.XPATH,'/')#None - http://training360.com/vizsgak/peoplecert-vizsgakozpont
btn_xpath_unit101, btn_xpath_nav101 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi/egyeb")]'),(By.XPATH,'/')#None - http://training360.com/informatikai-kepzesek/fejlesztoi/egyeb
btn_xpath_unit102, btn_xpath_nav102 = (By.XPATH,'//a[contains(@href,"/informatikai-kepzesek/fejlesztoi/egyeb")]'),(By.XPATH,'/')#None - http://training360.com/informatikai-kepzesek/fejlesztoi/egyeb
btn_xpath_unit103, btn_xpath_nav103 = (By.XPATH,'//a[contains(@href,"/jelentkezes")]'),(By.XPATH,'/')#None - http://training360.com/jelentkezes
btn_xpath_unit104, btn_xpath_nav104 = (By.XPATH,'//a[contains(@href,"/altalanos-tanfolyami-es-garancialis-feltetelek")]'),(By.XPATH,'/')#None - http://training360.com/altalanos-tanfolyami-es-garancialis-feltetelek
btn_xpath_unit105, btn_xpath_nav105 = (By.XPATH,'//a[contains(@href,"/online-szolgaltatasok-aszf")]'),(By.XPATH,'/')#None - http://training360.com/online-szolgaltatasok-aszf
btn_xpath_unit106, btn_xpath_nav106 = (By.XPATH,'//a[contains(@href,"/utalvanyok-kedvezmenyek")]'),(By.XPATH,'/')#None - http://training360.com/utalvanyok-kedvezmenyek
btn_xpath_unit107, btn_xpath_nav107 = (By.XPATH,'//a[contains(@href,"/hirek")]'),(By.XPATH,'/')#None - http://training360.com/hirek
btn_xpath_unit108, btn_xpath_nav108 = (By.XPATH,'//a[contains(@href,"/allasajanlatok")]'),(By.XPATH,'/')#None - http://training360.com/allasajanlatok
btn_xpath_unit109, btn_xpath_nav109 = (By.XPATH,'//a[contains(@href,"/magunkrol")]'),(By.XPATH,'/')#None - http://training360.com/magunkrol
btn_xpath_unit110, btn_xpath_nav110 = (By.XPATH,'//a[contains(@href,"/impresszum")]'),(By.XPATH,'/')#None - http://training360.com/impresszum
btn_xpath_unit111, btn_xpath_nav111 = (By.XPATH,'//a[contains(@href,"/lvc")]'),(By.XPATH,'/')#None - http://training360.com/lvc
btn_xpath_unit112, btn_xpath_nav112 = (By.XPATH,'//a[contains(@href,"/mentoralt-kepzesek")]'),(By.XPATH,'/')#None - http://training360.com/mentoralt-kepzesek
btn_xpath_unit113, btn_xpath_nav113 = (By.XPATH,'//a[contains(@href,"/oktatasi-tanacsadas")]'),(By.XPATH,'/')#None - http://training360.com/oktatasi-tanacsadas
btn_xpath_unit114, btn_xpath_nav114 = (By.XPATH,'//a[contains(@href,"/szintfelmeres")]'),(By.XPATH,'/')#None - http://training360.com/szintfelmeres
btn_xpath_unit115, btn_xpath_nav115 = (By.XPATH,'//a[contains(@href,"/testreszabott-megoldasok")]'),(By.XPATH,'/')#None - http://training360.com/testreszabott-megoldasok
btn_xpath_unit116, btn_xpath_nav116 = (By.XPATH,'//a[contains(@href,"/szallaslehetoseg")]'),(By.XPATH,'/')#None - http://training360.com/szallaslehetoseg
btn_xpath_unit117, btn_xpath_nav117 = (By.XPATH,'//a[contains(@href,"/adatkezelesi-tajekoztato")]'),(By.XPATH,'/')#None - http://training360.com/adatkezelesi-tajekoztato
btn_xpath_unit118, btn_xpath_nav118 = (By.XPATH,'//a[contains(@href,"/letoltes/training360-etikai-es-uzleti-magatartasi-kodex.pdf")]'),(By.XPATH,'/')#None - http://training360.com/letoltes/training360-etikai-es-uzleti-magatartasi-kodex.pdf
btn_xpath_unit119, btn_xpath_nav119 = (By.XPATH,'//a[contains(@href,"/panaszkezeles-eljarasi-rend")]'),(By.XPATH,'/')#None - http://training360.com/panaszkezeles-eljarasi-rend
btn_xpath_unit120, btn_xpath_nav120 = (By.XPATH,'//a[contains(@href,"/letoltes/training360-informaciobiztonsagi-politika-tanusitvany.pdf")]'),(By.XPATH,'/')#None - http://training360.com/letoltes/training360-informaciobiztonsagi-politika-tanusitvany.pdf
btn_xpath_unit121, btn_xpath_nav121 = (By.XPATH,'//a[contains(@href,"/nyilvantartott-kepzesi-programjaink")]'),(By.XPATH,'/')#None - http://training360.com/nyilvantartott-kepzesi-programjaink
btn_xpath_unit122, btn_xpath_nav122 = (By.XPATH,'//a[contains(@href,"/tajekoztatas-palyazatban-valo-reszvetelrol")]'),(By.XPATH,'/')#None - http://training360.com/tajekoztatas-palyazatban-valo-reszvetelrol
btn_xpath_unit123, btn_xpath_nav123 = (By.XPATH,'//a[contains(@href,"https://goo.gl/maps/odq6L2A68poZDHsJ7")]'),(By.XPATH,'/')#None - https://goo.gl/maps/odq6L2A68poZDHsJ7
btn_xpath_unit124, btn_xpath_nav124 = (By.XPATH,'//a[contains(@href,"https://www.facebook.com/Training360/")]'),(By.XPATH,'/')#None - https://www.facebook.com/Training360/
btn_xpath_unit125, btn_xpath_nav125 = (By.XPATH,'//a[contains(@href,"https://www.linkedin.com/company/training360")]'),(By.XPATH,'/')#None - https://www.linkedin.com/company/training360
btn_xpath_unit126, btn_xpath_nav126 = (By.XPATH,'//a[contains(@href,"https://open.spotify.com/show/7rEAuTij5nZBwsszhqRntJ?si=6U7Ybt6uTc2OHfdsgCaeRA")]'),(By.XPATH,'/')#None - https://open.spotify.com/show/7rEAuTij5nZBwsszhqRntJ?si=6U7Ybt6uTc2OHfdsgCaeRA
btn_xpath_unit127, btn_xpath_nav127 = (By.XPATH,'//a[contains(@href,"/hirlevel")]'),(By.XPATH,'/html/body/footer/nav/div/div/div[6]/div[2]/a')#Hírlevél feliratkozás - http://training360.com/hirlevel
btn_xpath_unit128, btn_xpath_nav128 = (By.XPATH,'//a[contains(@href,"/adatkezelesi-tajekoztato")]'),(By.XPATH,'/html/body/footer/div[1]/div/div/div[2]/form/div[5]/label/a')#Training360 adatvédelmi és adatkezelési tájékoztatóját - http://training360.com/adatkezelesi-tajekoztato
btn_xpath_unit138, btn_xpath_nav138 = (By.XPATH,'//a[contains(@href,"https://www.bisnode.hu/szolgaltatasok/bisnode-tanusitvany/")]'),(By.XPATH,'/')#None - https://www.bisnode.hu/szolgaltatasok/bisnode-tanusitvany/
btn_xpath_unit129, btn_xpath_nav129 = (By.XPATH,'//a[contains(@href,"https://www.nqa.com/en-gb/certification/standards/iso-27001")]'),(By.XPATH,'/')#None - https://www.nqa.com/en-gb/certification/standards/iso-27001
btn_xpath_unit130, btn_xpath_nav130 = (By.XPATH,'//a[contains(@href,"/letoltes/training360-adatkezelesi-tajekoztato-cookie.pdf")]'),(By.XPATH,'/html/body/div[3]/div/div/div[2]/a')#További információ...http://training360.com/letoltes/training360-adatkezelesi-tajekoztato-cookie.pdf
btn_xpath_unit131, btn_xpath_nav131 = (By.XPATH,'//a[contains(@data-href,"/treningek")]'),(By.XPATH,'/')#(data-href) - http://training360.com/treningek
btn_xpath_unit132, btn_xpath_nav132 = (By.XPATH,'//a[contains(@data-href,"/e-learning")]'),(By.XPATH,'/')#(data-href) - http://training360.com/e-learning
btn_xpath_unit133, btn_xpath_nav133 = (By.XPATH,'//a[contains(@data-href,"/informatikai-kepzesek")]'),(By.XPATH,'/')#(data-href) - http://training360.com/informatikai-kepzesek
btn_xpath_unit134, btn_xpath_nav134 = (By.XPATH,'//a[contains(@data-href,"/irodai-informatika")]'),(By.XPATH,'/')#(data-href) - http://training360.com/irodai-informatika
btn_xpath_unit135, btn_xpath_nav135 = (By.XPATH,'//a[contains(@data-href,"/vizsgak")]'),(By.XPATH,'/')#(data-href) - http://training360.com/vizsgak
btn_xpath_unit136, btn_xpath_nav136 = (By.XPATH,'//a[contains(@data-href,"https://roundme.com/embed/V9iCqXfR0iWmfPztCu2W")]'),(By.XPATH,'/')#(data-href) - https://roundme.com/embed/V9iCqXfR0iWmfPztCu2W
btn_xpath_unit137, btn_xpath_nav137 = (By.XPATH,'//a[contains(@data-href,"/bankkartyas-fizetes")]'),(By.XPATH,'/')#(data-href) - http://training360.com/bankkartyas-fizetes

#Non URL Link Locators
btn_xpath_unit139, btn_xpath_nav139 = (By.XPATH,'//a[contains(@href,"tel:+3618800040")]'),(By.XPATH,'/')#None - tel:+3618800040
btn_xpath_unit140, btn_xpath_nav140 = (By.XPATH,'//a[contains(@href,"mailto:info@training360.com")]'),(By.XPATH,'/')#None - mailto:info@training360.com
#Button tag Button Locators
btn_id_1 = (By.ID,'None')#submit
btn_id_2 = (By.ID,'PrimarySearchClose')#button
btn_id_3 = (By.ID,'callback_submit')#button
btn_id_4 = (By.ID,'CloseCallbackRequestModal')#button
btn_id_5 = (By.ID,'CallbackRequestSubmitButton')#submit
btn_id_6 = (By.ID,'None')#button
btn_id_7 = (By.ID,'None')#button

#Input Locators
input_id_1 = (By.ID,'PrimarySearchInput')#text
input_id_2 = (By.ID,'NameToCall')#text
input_id_3 = (By.ID,'PhoneToCall')#text
input_id_4 = (By.ID,'CallbackCategoryElearning')#checkbox
input_id_5 = (By.ID,'CallbackCategoryITcourseOperations')#checkbox
input_id_6 = (By.ID,'CallbackCategoryITcourseDevelopment')#checkbox
input_id_7 = (By.ID,'CallbackCategoryITcourseManagement')#checkbox
input_id_8 = (By.ID,'CallbackCategoryTrainingAndCoaching')#checkbox
input_id_9 = (By.ID,'CallbackCategoryInternationalExamCentre')#checkbox
input_id_10 = (By.ID,'CallbackCategoryOther')#checkbox
input_id_11 = (By.ID,'CallbackIsPrivacyPolicyAccepted')#checkbox
#Textarea Locators
text_id_1 = (By.ID,'CallbackMessage')#4000
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################
''''''
#URL Link Locators (These Navigate, except for #)
#    Unit          Navigation

#Non URL Link Locators

#Button tag Button Locators

#Input Locators

#Textarea Locators
######################################################################################################################################################