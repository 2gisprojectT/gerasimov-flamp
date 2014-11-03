__author__ = 'vi.gerasimov'


# -*- coding: utf-8 -*-
from online.helpers.base_component import BaseComponent


class WayPanel(BaseComponent):

    selectors = {
        'self': '.routeResults'
    }

    @property
    def is_displayed(self):
        return self.driver.find_element_by_css_selector(self.selectors['self']).is_displayed()