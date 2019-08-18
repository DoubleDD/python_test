#!/usr/bin/python
# -*- coding:utf-8 -*-
from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaiduTestCase(TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def tearDown(self) -> None:
        self.browser.close()

    def testPageTitle(self):
        browser = self.browser
        browser.get('https://www.baidu.com/')
        self.assertIn('百度一下，你就知道', browser.title)
        ele = browser.find_element_by_id('kw')
        ele.send_keys('selenium' + Keys.RETURN)
        assert 'no result found' not in browser.page_source

if __name__ == "__main__":
    main(verbosity=2)
