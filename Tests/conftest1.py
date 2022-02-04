import pytest
from datetime import datetime
from selenium import webdriver
import pytest_html

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    timestamp = datetime.now().strftime('%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser')
        driver.save_screenshot('Screenshots/scr' + timestamp + '.png')
        extra.append(pytest_html.extras.image('Screenshots/scr' + timestamp + '.png'))
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.image('Screenshots/scr.png'))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra

@pytest.fixture(scope='session')
def setup():
    print('Starting')
    url = 'https://www.google.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    return driver