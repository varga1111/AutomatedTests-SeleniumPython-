from selenium import webdriver

PATH = '/Users/openmindschooling/MyStuff/Web/Chrome_webdriver/chromedriver'
    
driver= webdriver.Chrome(PATH)

driver.get('https://www.training360.com')



images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))

driver.close()