import os

import pytest
from selenium import webdriver

browsers = {'EI - 10': {
    "os": "Windows",
    "os_version": "10",
    "browser": "IE",
    "browser_version": "11.0"
}, 'Iphone 8': {
    "os_version": "11",
    "device": "iPhone 8 Plus",
    "real_mobile": "true",
    "browserstack.local": "false"
}, 'Pixel 3a': {
    "os_version": "9.0",
    "device": "Google Pixel 3a",
    "real_mobile": "true",
    "browserstack.local": "false"
}, 'Pixel 4': {
    "os_version": "11.0",
    "device": "Google Pixel 4",
    "real_mobile": "true",
    "browserstack.local": "false"
}, 'Chrome': {
    "os": "Windows",
    "os_version": "8",
    "browser": "Chrome",
    "browser_version": "latest",
    "browserstack.local": "false",
    "browserstack.selenium_version": "3.14.0"
}
}


@pytest.fixture(scope="module", params=browsers)
def driver(request):
    username = os.getenv("BROWSERSTACK_USERNAME")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
    caps = browsers[request.param]
    caps["browserstack.user"] = username
    caps["browserstack.key"] = access_key
    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=caps)
    yield driver
    driver.quit()


def test_python(driver):
    driver.get("http://www.python.org")
    assert driver.title == "Welcome to Python.org"


def test_pharo(driver):
    driver.get("https://pharo.org")
    driver.find_element_by_link_text("Discover").click()
    assert driver.title == "Pharo - features"


def test_github(driver):
    driver.get("https://github.com/mattonem")
    assert driver.find_element_by_xpath("//span[@itemprop='name']").text == "maxmattone"
