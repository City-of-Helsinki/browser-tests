from fixtures.common import *  # NOQA

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = 'servicemap'


class MainPage:
    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        '#search-region > div > form > span:nth-of-type(1) > input')
    BROWSE_BUTTON = (
        By.ID,
        'browse-region')
    SUGGESTIVE_SEARCH_RESULTS = (
        By.CSS_SELECTOR,
        '#search-region span.twitter-typeahead .tt-dataset-service')
    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        '#search-region > div > form > span.action-button.search-button > span')
    PERSONALISATION_BUTTON = (
        By.CSS_SELECTOR,
        '#personalisation .personalisation-button')
    COLORBLIND_BUTTON = (
        By.CSS_SELECTOR,
        '#personalisation .accessibility-personalisation ul.personalisations li[data-type="colour_blind"]')
    ACCESSIBLE_MAP_LAYER = (
        By.CLASS_NAME,
        'maplayer-accessible_map')
    FEATURE_TOUR_POPUP = (
        By.CSS_SELECTOR,
        '.popover.tour')


class ServiceTreePage:
    SERVICE_NAME = (
        By.CSS_SELECTOR,
        '#service-tree-container > ul > li .service-name')


class SearchResultPage:
    RESULT_LIST = (
        By.CSS_SELECTOR,
        'ul.search-result-list')


class TestBasicSanity:

    def test_site_title(self, driver_with_page):
        # TODO: translations in various languages
        assert driver_with_page.title == 'Pääkaupunkiseudun palvelukartta'

    def test_browse_button(self, wait_for):
        element = wait_for(EC.element_to_be_clickable,
                           MainPage.BROWSE_BUTTON)
        element.click()

        elements = wait_for(EC.presence_of_all_elements_located,
                            ServiceTreePage.SERVICE_NAME)

        assert len(elements) == 9

        # TODO: translations
        matches = set((e for e in elements if e.text == 'Terveys'))
        assert len(matches) == 1

        for e in elements:
            assert e.text != 'Sairaus'

    def test_suggestive_search(self, wait_for):
        search_text = 'kallion kirjasto'

        input_element = wait_for(EC.element_to_be_clickable,
                                 MainPage.SEARCH_INPUT)

        input_element.click()
        input_element.send_keys(search_text)

        wait_for(EC.text_to_be_present_in_element,
                 MainPage.SUGGESTIVE_SEARCH_RESULTS,
                 'Kallion kirjasto')

    def test_fulltext_search(self, wait_for):
        search_text = 'kallion kirjasto'

        input_element = wait_for(EC.element_to_be_clickable,
                                 MainPage.SEARCH_INPUT)

        input_element.click()
        input_element.send_keys(search_text)

        search_button = wait_for(EC.element_to_be_clickable,
                                 MainPage.SEARCH_BUTTON)
        search_button.click()

        wait_for(EC.text_to_be_present_in_element,
                 SearchResultPage.RESULT_LIST,
                 'Kallion kirjasto')
