__author__ = 'vi.gerasimov'


from flamp_tests.components.base_component import BaseComponent


class SearchRubricBar(BaseComponent):

    selectors = {
        'self': '.light-search',
        'input': '#f-col1-holder > form > div > input.textfield',
        'submit': '#f-col1-holder > form > div > input.submit',
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    @property
    def search_text(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute('value')