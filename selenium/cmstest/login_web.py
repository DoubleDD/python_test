# -*- coding:utf-8 -*-
import init_env
import time
from selenium.webdriver.common.keys import Keys


class LoginWeb:
    def __init__(self, driver=None, url=None, username=None, password=None):
        self.driver = driver
        self.url = url
        self.username = username
        self.password = password
        self.login()

    def login(self):
        driver = self.driver
        try:
            driver.get(self.url)
        except:
            print("加载页面太慢，停止加载，继续下一步操作")
            driver.execute_script("window.stop()")
        # driver.maximize_window()
        print('打开url')
        sleep(2)
        self.loginAction(driver,self.username, self.password)

    def loginAction(self, driver=None, username=None, password=None):
        longin_link = driver.find_element_by_link_text("登录")
        print('获取登录按钮')
        longin_link.click()
        print('点击登录按钮')
        sleep(2)

        usernameEle = driver.find_element_by_name('username')
        passwordEle = driver.find_element_by_name('pword')
        usernameEle.send_keys(username + Keys.ESCAPE)
        print('设置用户名')
        passwordEle.send_keys(password + Keys.RETURN)
        print('设置密码')
        sleep(2)


def sleep(s=.5) -> None:
    time.sleep(s)
