from selenium import webdriver
import pytest
from testdata import Testdata
import allure
import sys
import time


@pytest.mark.usefixtures("init_driver")
class Parent_test(Testdata):
    

    pass


