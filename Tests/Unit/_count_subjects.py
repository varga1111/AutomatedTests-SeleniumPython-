#from cgi import test
from selenium import webdriver
import pytest
import time
#from selenium.webdriver.support.ui import WebDriverWait as wait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from collections import Counter



PATH = '/Users/openmindschooling/MyStuff/Web/Chrome_webdriver/chromedriver'
    
driver= webdriver.Chrome(executable_path=PATH)

driver.get('https://training360.com/tanfolyami-naptar')

time.sleep(4)


def test_count_instances():
    a = driver.find_elements_by_class_name('co')
    time.sleep(3)
    total = len(a)

    assert total == 408
    print(bool(total))
    return bool(total)
        
test_count_instances()




