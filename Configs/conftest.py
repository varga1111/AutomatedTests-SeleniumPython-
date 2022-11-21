import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo
import allure
from allure_commons.types import AttachmentType
from testdata import Testdata


@pytest.fixture(params=['Chrome'], scope ='class')#, autouse=True)
def init_driver(request):
    global browser
    if request.param == 'Chrome':
        opt = Options()
        opt.add_argument("--window-size=1920,1080")
        opt.add_argument("--start-maximized")
        opt.add_argument("--headless")

        browser = webdriver.Chrome(executable_path=Testdata.PATH, chrome_options=opt)

    request.cls.browser = browser
    browser = request.cls.browser
    
    yield 
    browser.close()



'''@pytest.fixture(scope='class', autouse=True)
def failed_check():
    yield


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
     get the hook function for the state of each use case 
    :param item:  test case 
    :param call:  test procedure 
    :return:
    """
    #  get the result of the call to the hook method 
    out_come = yield
    rep = out_come.get_result()  #  get the test report from the result of the call to the hook method 
    # rep.when represents the test step and only gets the use case call  the result of the execution is a failure.   does not include setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write((rep.nodeid + extra + "\n"))
        #  add screenshot of allure report 
        driver = browser.get_driver()
        if hasattr(driver, "get_screenshot_as_png"):
                allure.attach(driver.get_screenshot_as_png(), " failed screenshot ", allure.attachment_type.PNG)
    
    failed_check()'''


'''@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # set up a hook to be able to check if a test has failed
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope='class', autouse=True)
def failed_check(request):  # check if a test has failed
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print(Testdata.to_print , request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.instance.webdriver
            take_screenshot(driver, request.node.nodeid)


def take_screenshot(driver, nodeid):  # make a screenshot with a name of the test, date and time
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H-%M")}.png'.replace("/", "_").replace("::", "__")
    screenshot_dir = os.path.join(os.path.dirname(__file__), 'screenshots')
    if not os.path.exists(screenshot_dir):
        os.mkdir(screenshot_dir)
    driver.save_screenshot(os.path.join(screenshot_dir, file_name))'''






'''
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope = 'class', autouse= True)
def tear_down(request):
    method_name = request.node.name
    if request.node.rep_call.failed:
        print('test {} failed :('.format(method_name))'''
        # do more stuff like take a selenium screenshot




'''@pytest.fixture(scope='class', autouse=True)
def failed_check():     
    outcum = 'izt'  



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if (rep.when == 'call' or rep.when == 'setup') and (rep.failed or rep.skipped):
        try:
            if 'init_driver' in item.fixturenames:
                web_driver = item.funcargs['init_driver']
                screen_shot = '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Tests/Navigation/Screenshots/test_get_e_learning_unique_title2.png'
                web_driver.save_screenshot(screen_shot)
                with open (screen_shot, mode= 'rb') as file:
                    f = file.read()
                allure.attach(f, 'screenshot', allure.attachment_type.PNG )
                
            else:
                print('Fail to take screenshot. no driver fixture found')
                return

        except Exception as e:
            print('Fail to take screenshot:' ,format(e))

    failed_check()'''


'''@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if (rep.when == 'call' or rep.when == 'setup') and (rep.failed or rep.skipped):
        try:
            if 'init_driver' in item.fixturenames:
                web_driver = item.funcargs['init_driver']
                allure.attach(
                    web_driver.get_screenshot_as_png(),
                    name=' !! Screenshot Captured !!',
                    attachment_type = allure.attachment_type.PNG)
                
            else:
                print('Fail to take screenshot. no driver fixture found')
                return

        except Exception as e:
            print('Fail to take screenshot:' ,format(e))

        failed_check()'''

'''def _fail_picture():     
    init_driver.fail_picture()    


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if (rep.when == 'call' or rep.when == 'setup') and (rep.failed or rep.skipped):
        try:
            if 'init_driver' in item.fixturenames:
                web_driver = item.funcargs['init_driver']
                screen_shot = '/Users/openmindschooling/MyStuff/Web/Training360/AutomatedTests/Screenshots/test_get_e_learning_unique_title.png'
                web_driver.save_screenshot(screen_shot)
                with open (screen_shot, mode= 'rb') as file:
                    f = file.read()
                allure.attach(f, 'screenshot', allure.attachment_type.PNG )
                
            else:
                print('Fail to take screenshot. no driver fixture found')
                return

        except Exception as e:
            print('Fail to take screenshot:' ,format(e))

    _fail_picture()'''

