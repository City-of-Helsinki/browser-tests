import pytest
import settings

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    if settings.SAUCELABS_USERNAME:
        if settings.BROWSER == 'ie11':
            desired_cap = {
                'platform': "Windows 10",
                'browserName': "internet explorer",
                'version': "11.103",
            }
        elif settings.BROWSER == 'ie10':
            desired_cap = {
                'platform': "Windows 7",
                'browserName': "internet explorer",
                'version': "10.0",
            }
        else:
            desired_cap = {
                'platform': "Mac OS X 10.9",
                'browserName': "chrome",
                'version': "31",
            }
        driver = webdriver.Remote(
           command_executor=f'http://{settings.SAUCELABS_USERNAME}:{settings.SAUCELABS_ACCESS_KEY}@ondemand.saucelabs.com:80/wd/hub',
           desired_capabilities=desired_cap)
    else:
        chrome_options = Options()
        if settings.HEADLESS:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=512,512')
        driver = webdriver.Chrome(chrome_options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def driver_with_page(request, driver):
    service = getattr(request.module, 'service')
    url = settings.SERVICES[service]['URL']
    driver.get(url)
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
