from selenium import webdriver

PATH = '/Users/openmindschooling/MyStuff/Web/Chrome_webdriver/chromedriver'
    
driver= webdriver.Chrome(PATH)

driver.get('https://www.training360.com')



a = driver.find_elements_by_tag_name('a')
for id_ in a:
    print(id_.get_attribute('id'))

driver.close()