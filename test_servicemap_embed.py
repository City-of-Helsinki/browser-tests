import pytest
import settings
from fixtures.common import *
from fixtures.servicemap import *

from test_servicemap import MainPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = 'servicemap'

SERVICEMAP_URL = settings.SERVICES['servicemap']['URL']


class EmbedPage(object):
    MAP = (By.ID, 'map')
    LEAFLET_MAP_PANE = (By.CLASS_NAME, 'leaflet-map-pane')
    POPUP_LABEL = (By.CSS_SELECTOR, '.leaflet-popup-content > .unit-name')
    UNIT_MARKER = (By.CSS_SELECTOR, '.leaflet-marker-pane > .leaflet-marker-icon')
    ACCESSIBLE_MAP = (By.CLASS_NAME, 'accessible_map')


def embed_url(path):
    return '{base}/embed/{path}'.format(base=SERVICEMAP_URL, path=path)


def get_js_script(script_name):
    f = open('js/{}.js'.format(script_name), 'r')
    return f.read()


def assert_javascript(driver, script_name, *args):
    assert driver.execute_script(get_js_script(script_name), *args)


class TestEmbedding:

    def common_checks(self, specs, wait_for, driver):
        specs.setdefault('map', 'servicemap')

        wait_for(EC.title_is, 'Pääkaupunkiseudun palvelukartta')
        wait_for(EC.presence_of_element_located, EmbedPage.MAP)
        wait_for(EC.presence_of_element_located, EmbedPage.LEAFLET_MAP_PANE)
        assert driver.find_element_by_id('navigation-region').is_displayed() == False
        assert driver.find_element_by_class_name('leaflet-control-zoom').is_displayed() == True
        assert driver.find_element_by_class_name('bottom-logo').is_displayed() == True

    def test_basic_embed(self, driver):
        wait_for = make_waiter(driver)

        driver.get(embed_url(''))
        self.common_checks({}, wait_for, driver)

    def test_address_embed(self, address_embed, driver):
        wait_for = make_waiter(driver)
        driver.get(embed_url(address_embed['path']))

        self.common_checks(address_embed, wait_for, driver)

        elements = wait_for(EC.presence_of_all_elements_located, EmbedPage.POPUP_LABEL)
        assert len(elements) == 1
        assert elements[0].text == address_embed['name']

        location = address_embed['location']
        assert_javascript(driver,
                           'isNearMapCenter',
                           location['lat'], location['lng'])

    def test_unit_embed(self, unit_embed, driver):
        wait_for = make_waiter(driver)
        driver.get(embed_url(unit_embed['path']))

        self.common_checks(unit_embed, wait_for, driver)

        elements = wait_for(EC.presence_of_all_elements_located, EmbedPage.UNIT_MARKER)
        assert len(elements) == 1

        bbox = unit_embed.get('bbox')
        location = unit_embed.get('location')
        if bbox:
            assert_javascript(driver,
                               'containsPoint',
                               location['lat'], location['lng'])

            # TODO: in the current version, the bbox
            # paremeters do not work correctly
            #
            # - fix in v2 embed?
            #
            # assert_javascript(driver,
            #                    'containsBbox',
            #                    bbox)
                                               
        else:
            assert_javascript(driver,
                               'isNearMapCenter',
                               location['lat'], location['lng'])

    def test_service_embed(self, service_embed, driver):
        wait_for = make_waiter(driver)
        driver.get(embed_url(service_embed['path']))

        self.common_checks(service_embed, wait_for, driver)

        elements = wait_for(EC.presence_of_all_elements_located, EmbedPage.UNIT_MARKER)
        assert len(elements) > 10

    @pytest.mark.xfail
    def test_personalization_settings(self, wait_for, driver):
        # Currently verifies that the user's map background settings
        # persist even for embedded views. TODO: is this the desired
        # behavior?

        button = wait_for(EC.element_to_be_clickable, MainPage.PERSONALISATION_BUTTON)
        button.click()

        button = wait_for(EC.element_to_be_clickable, MainPage.COLORBLIND_BUTTON)
        button.click()

        assert wait_for(EC.presence_of_element_located, MainPage.ACCESSIBLE_MAP_LAYER).is_displayed()

        driver.get(embed_url('address/helsinki/mannerheimintie/5'))
        
        assert wait_for(EC.presence_of_element_located, EmbedPage.ACCESSIBLE_MAP).is_displayed()        
