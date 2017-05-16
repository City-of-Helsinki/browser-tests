import pytest
import settings

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

HEADLESS = False


@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    if HEADLESS:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=512,512')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def driver_with_page(driver):
    driver.get(settings.SERVICEMAP_URL)
    return driver


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
