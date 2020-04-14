# -*- coding:utf-8 -*-
import time
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
        findXpath = self.findByXpath
        try:
            driver.get("https://kedong.zhixueyun.com")
        except:
            print("加载页面太慢，停止加载，继续下一步操作")
            driver.execute_script("window.stop()")
        driver.maximize_window()
        print('打开url')
        sleep(2)

        longin_link = driver.find_element_by_link_text("登录")
        print('获取登录按钮')
        longin_link.click()
        print('点击登录按钮')
        sleep(1)

        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('pword')
        username.send_keys('admin' + Keys.ESCAPE)
        print('设置用户名')
        password.send_keys('zxy123456' + Keys.RETURN)
        print('设置密码')
        sleep(2)


def sleep(s=.5) -> None:
    time.sleep(s)


if __name__ == "__main__":
    main(verbosity=2)
