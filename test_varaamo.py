import settings
from fixtures.common import *  # NOQA

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = 'varaamo'


class MainPage:
    FIRST_PURPOSE = (
        By.CSS_SELECTOR,
        '.purpose-list .purpose-list-item:nth-of-type(1)'
    )
    NAVBAR_COLLAPSE_BUTTON = (
        By.CSS_SELECTOR,
        '.navbar .navbar-header button.navbar-toggle'
    )
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        '.navbar .navbar-right li a'
    )
    USER_DROPDOWN = (
        By.CSS_SELECTOR,
        '#user-dropdown'
    )


class TunnistamoLoginPage:
    LOGIN_TEXT = (
        By.CSS_SELECTOR,
        '.hel-login-box h2'
    )

    @staticmethod
    def login_method(method):
        return (By.CSS_SELECTOR, '.hel-login-methods .login-method-%s' % method)


class ADFSLoginPage:
    USERNAME_INPUT = (
        By.CSS_SELECTOR,
        '#userNameInput'
    )
    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        '#passwordInput'
    )
    SUBMIT_BUTTON = (
        By.CSS_SELECTOR,
        '#submitButton'
    )


class TestVaraamo:
    def test_site_title(self, driver_with_page):
        # TODO: translations in various languages
        assert driver_with_page.title == 'Varaamo'

    def test_purposes_anon(self, wait_for):
        element = wait_for(EC.element_to_be_clickable,
                           MainPage.FIRST_PURPOSE)
        assert element.text == 'Liikkua tai pelata'

    def perform_adfs_login(self, driver, wait_for):
        el = driver.find_element(*TunnistamoLoginPage.login_method('helsinki_adfs'))
        assert el is not None
        el.click()

        username_el = wait_for(EC.presence_of_element_located,
                               ADFSLoginPage.USERNAME_INPUT)
        password_el = driver.find_element(*ADFSLoginPage.PASSWORD_INPUT)
        assert password_el is not None
        submit_button_el = driver.find_element(*ADFSLoginPage.PASSWORD_INPUT)
        assert submit_button_el is not None
        username_el.send_keys(settings.HELSINKI_ADFS_USER)
        password_el.send_keys(settings.HELSINKI_ADFS_PASSWORD)
        submit_button_el.submit()

    def perform_facebook_login(self, driver, wait_for):
        el = driver.find_element(*TunnistamoLoginPage.login_method('facebook'))
        assert el is not None
        el.click()

        username_el = wait_for(EC.presence_of_element_located,
                               (By.CSS_SELECTOR, '#email'))
        password_el = driver.find_element(By.CSS_SELECTOR, '#pass')
        assert password_el is not None
        submit_button_el = driver.find_element(By.CSS_SELECTOR, '#loginbutton')
        assert submit_button_el is not None
        username_el.send_keys(settings.FACEBOOK_USER)
        password_el.send_keys(settings.FACEBOOK_PASSWORD)
        submit_button_el.submit()

    def test_login(self, driver_with_page, wait_for):
        el = wait_for(EC.element_to_be_clickable,
                      MainPage.NAVBAR_COLLAPSE_BUTTON)
        el.click()
        el = wait_for(EC.element_to_be_clickable,
                      MainPage.LOGIN_BUTTON)
        assert el.get_property('innerText') == 'Kirjaudu sisään'
        el.click()

        driver = driver_with_page
        el = wait_for(EC.presence_of_element_located,
                      TunnistamoLoginPage.LOGIN_TEXT)
        assert el.text == 'Kirjaudu sisään'

        self.perform_facebook_login(driver, wait_for)

        wait_for(EC.presence_of_element_located,
                 MainPage.USER_DROPDOWN)

        element = wait_for(EC.element_to_be_clickable,
                           MainPage.FIRST_PURPOSE)
        assert element.text == 'Liikkua tai pelata'
