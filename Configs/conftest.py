import pytest
from testdata import Testdata
from selenium import webdriver 
import allure
import os

@pytest.fixture(params=['Chrome'], scope ='class')
def init_driver(request):

    if request.param == 'Chrome':
        browser = webdriver.Chrome(executable_path=Testdata.PATH)
        browser.maximize_window()
    request.cls.browser = browser
    yield
    browser.close()

