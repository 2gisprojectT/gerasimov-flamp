# -*- coding: utf-8 -*-
__author__ = 'vi.gerasimov'

from unittest import TestCase
import unittest

from selenium import webdriver

from flamp_tests.pages.cat_page import CatPage


class SeleniumTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.page = CatPage(self.driver)
        self.page.open("http://novosibirsk.flamp.ru/cat")

    def tearDown(self):
        self.driver.close()

    def test_rubric_search(self):
        rubric = u'Университеты'
        page = self.page
        page.search_rubric_bar.search(rubric)
        self.assertEqual(page.search_rubric_bar.search_text, rubric)
        self.assertTrue(page.catalog.is_contain_link(rubric))

    def test_multi_rubric_search(self):
        rubric = u'Обучение за рубежом'
        page = self.page
        page.search_rubric_bar.search(rubric)
        self.assertEqual(page.search_rubric_bar.search_text, rubric)
        self.assertTrue(page.catalog.is_contain_link(rubric))

    def test_empty_rubric_search(self):
        page = self.page
        page.search_rubric_bar.search('')
        self.assertEqual(page.catalog.main_not_found_message, u'К сожалению, поиск по каталогу не дал результатов.')
        self.assertEqual(page.catalog.sub_not_found_message, u'Попробуйте использовать другие ключевые слова.')


if __name__ == '__main__':
    unittest.main()