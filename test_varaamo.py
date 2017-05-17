from fixtures.common import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

service = 'varaamo'


class TestVaraamo:
    def test_site_title(self, driver_with_page):
        # TODO: translations in various languages
        assert driver_with_page.title == 'Varaamo'
