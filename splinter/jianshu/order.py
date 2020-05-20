# -*- coding:utf-8 -*-
import init_env
import time
from splinter import Browser


class Blog:
    def __init__(self, browser=None):
        self.browser = browser
        self.view()

    def view(self):
        """刷帖子
        """
        browser = self.browser
        # 打开帖子
        browser.visit('https://www.jianshu.com/p/e91ee83f2348')
        time.sleep(1)

        # 刷新
        while True:
            browser.reload()
            time.sleep(5)

if __name__ == "__main__":
    browser = Browser("chrome")
    Blog(browser)
