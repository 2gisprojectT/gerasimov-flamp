__author__ = 'vi.gerasimov'


from flamp_tests.components.search_rubric_bar import SearchRubricBar
from flamp_tests.components.catalog import Catalog


class CatPage():

    selectors = {
        'share_link': '.extras__share'
    }

    def __init__(self, driver):
        self.driver = driver

    @property
    def search_rubric_bar(self):
        return SearchRubricBar(self.driver, self.driver.find_element_by_css_selector(SearchRubricBar.selectors['self']))

    @property
    def catalog(self):
        return Catalog(self.driver, self.driver.find_element_by_css_selector(SearchRubricBar.selectors['self']))

    def open(self, url):
        self.driver.get(url)