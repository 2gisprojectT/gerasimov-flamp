__author__ = 'vi.gerasimov'


from flamp_tests.components.base_component import BaseComponent


class Catalog(BaseComponent):

    selectors = {
        'self': '.catalog',
        'not_found_main_message': '#f-col1-holder > h3',
        'not_found_sub_message': '#f-col1-holder > p > em'
    }

    def is_contain_link(self, text):
        return self.driver.find_element_by_css_selector(self.selectors['self']).find_element_by_link_text(text)

    @property
    def main_not_found_message(self):
        return self.driver.find_element_by_css_selector(Catalog.selectors['not_found_main_message']).get_attribute('innerHTML')

    @property
    def sub_not_found_message(self):
        return self.driver.find_element_by_css_selector(Catalog.selectors['not_found_sub_message']).get_attribute('innerHTML')