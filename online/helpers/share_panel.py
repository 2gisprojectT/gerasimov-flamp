__author__ = 'vi.gerasimov'


# -*- coding: utf-8 -*-
from online.helpers.base_component import BaseComponent


class SharePanel(BaseComponent):

    selectors = {
        'self': '.share',
        'link': '.share__popupUrlInput'
    }

    @property
    def link(self):
        return self.driver.find_element_by_css_selector(self.selectors['link']).get_attribute('value')