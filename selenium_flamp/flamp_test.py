__author__ = 'vi.gerasimov'
# -*- coding: utf-8 -*-

from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class FlampTest(TestCase):
    def test_rubric_search(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get("http://flamp.ru/")
        assert u"Фламп — отзывы покупателей о компаниях вашего города" in driver.title
        wait.until(lambda _: driver.find_element_by_id("nav-tab-companies")).click()
        wait.until(lambda _: driver.find_element_by_css_selector("a[href*='/cat']")).click()
        wait.until(lambda _: driver.find_element_by_name("Rubric[what]")).send_keys(u"Университеты")
        wait.until(lambda _: driver.find_element_by_css_selector("input[value='Найти рубрику']")).click()
        elem = ".catalog-item > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)"
        assert wait.until(lambda _: driver.find_element_by_css_selector(elem)).text == u"Университеты"
        driver.quit()

if __name__ == '__main__':
    unittest.main()
