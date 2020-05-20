# -*- coding:utf-8 -*-
import init_env
import time
from splinter import Browser

class Loginzxy:
    def __init__(self,browser=None, url=None, username=None, password=None):
        self.browser = browser
        self.url = url
        self.username = username
        self.password = password

    def login(self) -> Browser:
        browser = self.browser
        browser.visit(self.url)
        print('打开url')
        sleep(2)
        return self.loginAction(browser, self.username, self.password)

    def loginAction(self, browser=None, username=None, password=None) -> Browser:
        longin_link = browser.find_link_by_text("登录")
        print('获取登录按钮')
        longin_link.click()
        print('点击登录按钮')
        sleep(2)

        usernameEle = browser.find_by_name('username')[0]
        passwordEle = browser.find_by_name('pword')[0]
        usernameEle.fill(username)
        print('设置用户名')
        passwordEle.fill(password)
        print('设置密码')
        browser.find_by_value('登录').click()
        return browser


def sleep(s=.5) -> None:
    time.sleep(s)


if __name__ == "__main__":
    browser = Browser("chrome")
    zxy = Loginzxy(browser,"https://rastest9.zhixueyun.com", "admin", "zxy123456")
    browser = zxy.login()
    time.sleep(10)
    browser.quit()
