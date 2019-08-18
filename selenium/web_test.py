#!/usr/bin/python
# -*- coding:utf-8 -*-
from unittest import TestCase, main
from selenium import webdriver


class BaiduTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://www.baidu.com/')
        self.assertIn('百度一下，你就知道', self.browser.title)


if __name__ == "__main__":
    main(verbosity=2)
