__author__ = 'vi.gerasimov'


from online.helpers.search_bar import SearchBar
from online.helpers.way_panel import WayPanel
from online.helpers.share_panel import SharePanel


class Page():

    selectors = {
        'share_link': '.extras__share'
    }

    def __init__(self, driver):
        self.driver = driver

    @property
    def search_bar(self):
        return SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))

    @property
    def way_panel(self):
        return WayPanel(self.driver, self.driver.find_element_by_css_selector(WayPanel.selectors['self']))

    @property
    def share_panel(self):
        self.driver.find_element_by_css_selector(self.selectors['share_link']).click()
        return SharePanel(self.driver, self.driver.find_element_by_css_selector(SharePanel.selectors['self']))

    def open(self, url):
        self.driver.get(url)