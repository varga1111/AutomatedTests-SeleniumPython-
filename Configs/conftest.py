import pytest
from selenium import webdriver
import allure
from testdata import Testdata
import time


@pytest.fixture(params=['Chrome'], scope ='class')
def init_driver(request):

    if request.param == 'Chrome':
        browser = webdriver.Chrome(executable_path=Testdata.PATH)
        browser.maximize_window()
    request.cls.browser = browser
    yield
    time.sleep(3)
    browser.close()



