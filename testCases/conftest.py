from selenium import webdriver
import pytest
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def tc_setup(browser, request):
    global driver
    if browser == "chrome":
        print("Launching Chrome Browser")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        print("Launching Firefox Browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    else:
        print("Provide a valid Browser")

    driver.maximize_window()
    driver.get("https://e4a.alpha.egwhite.net/")

    request.cls.driver = driver
    yield
    driver.close()


def pytest_html_report_title(report):
    report.title = "Automation Report"


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        extra.append(pytest_html.extras.url("https://e4a.alpha.egwhite.net/"))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
