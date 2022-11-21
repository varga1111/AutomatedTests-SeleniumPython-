from selenium import webdriver

PATH = '/Users/openmindschooling/MyStuff/Web/Chrome_webdriver/chromedriver'
    
driver= webdriver.Chrome(PATH)

driver.get('https://www.training360.com')

driver.maximize_window()

image_elements = driver.find_elements_by_xpath("//img")

for image in image_elements:
    img_src = image.get_attribute("src")
    img_name = image.get_attribute("alt")

    print(img_name)
    print(img_src, '\n')



for image in range(0, len(image_elements)):

    image += 1

print('Total images: ', image)


driver.quit()