# -*- coding: utf-8 -*-
__author__ = 'vi.gerasimov'


from unittest import TestCase
import unittest
from selenium import webdriver
from online.helpers.page import Page


class SeleniumTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.page = Page(self.driver)
        self.page.open("http://2gis.ru")

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        page = self.page
        page.search_bar.search(u'кафе')
        page.open(page.share_panel.link)
        self.assertEqual(u'кафе', page.search_bar.search_text)

    def test_way_search(self):
        page = self.page
        page.search_bar.way_search(u'Студенческая', u'Мега')
        self.assertTrue(page.way_panel.is_displayed, 'Not found way panel')

if __name__ == '__main__':
    unittest.main()