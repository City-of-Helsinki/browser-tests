import pytest
import settings

# @pytest.fixture
# def driver():

#     driver = 
#     # yield driver
#     # driver.close()

from selenium import webdriver
_driver = webdriver.Chrome()

def get_driver():
    return _driver

@pytest.fixture
def driver_with_page():
    _driver.get(settings.SERVICEMAP_URL)
    return _driver

def wait(driver):
    from selenium.webdriver.support.ui import WebDriverWait
    return WebDriverWait(driver, settings.TIMEOUT)

def make_waiter(driver):
    def waiter(condition, *args):
        return wait(driver).until(condition(*args))
    return waiter

@pytest.fixture
def wait_for(driver_with_page):
    return make_waiter(driver_with_page)
