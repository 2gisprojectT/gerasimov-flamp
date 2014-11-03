__author__ = 'vi.gerasimov'


from online.helpers.base_component import BaseComponent


class SearchBar(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'input': '#module-1-1-1 > div:nth-child(1) > input:nth-child(1)',
        'submit': 'button.searchBar__submit',
        'way_tab': 'div.searchBar__tab:nth-child(2)',
        'to': '#module-1-1-2 > div:nth-child(1) > input:nth-child(1)',
        'from': '#module-1-1-3 > div:nth-child(1) > input:nth-child(1)',
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def way_search(self, _to, _from):
        self.driver.find_element_by_css_selector(self.selectors['way_tab']).click()
        self.driver.find_element_by_css_selector(self.selectors['to']).send_keys(_to)
        self.driver.find_element_by_css_selector(self.selectors['from']).send_keys(_from)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    @property
    def search_text(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute('value')