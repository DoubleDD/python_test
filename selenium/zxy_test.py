# -*- coding:utf-8 -*-
import init_env
import time
from cmstest.login_web import LoginWeb
from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ZxyTestCase(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def findByXpath(self, xpath=None):
        if xpath:
            return self.driver.find_element_by_xpath(xpath)
        else:
            return None

    def testLogin(self):
        driver = self.driver
        url = "https://kedong.zhixueyun.com"
        username = 'kedong01'
        password = '123kedong01'
        LoginWeb(driver, url, username, password)


def sleep(s=.5) -> None:
    time.sleep(s)


if __name__ == "__main__":
    main(verbosity=2)
