import os

import pytest
import json
from selenium import webdriver


with open('browsers.json') as json_file:
    browsers = json.load (json_file)

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
