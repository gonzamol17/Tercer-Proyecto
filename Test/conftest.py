import time
import warnings
import json
import pytest
from Utils import utils as utils
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def test_setup(request):
    global driver
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        option = webdriver.ChromeOptions()
        option.add_experimental_option("useAutomationExtension", False)
        option.add_experimental_option("excludeSwitches", ['enable-automation'])
        service_obj = Service("..\\Drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=option)
    elif browser == 'firefox':
        service_obj = Service("..\\Drivers\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    warnings.simplefilter('ignore', ResourceWarning)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    driver.get(utils.URL)
    yield
    driver.close()
    driver.quit()



#@pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        extra.append(pytest_html.extras.url("https://automationteststore.com/"))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
    #driver.get_screenshot_as_file(name)
    driver.get_screenshot_as_file("..\\Test\\Reports\\"+name)
