"""资源授权
"""
# -*- coding:utf-8 -*-
#import init_env
import time
from splinter import Browser
from customCompany.resource import Resource
from resourcePlatform.order import Order
from login_web import Loginzxy


class Grant:
    """资源授权
    """

    def __init__(self):
        self.browser = Browser("chrome")

    def destroy(self) -> None:
        """销毁
        """
        self.browser.quit()

    def create(self):
        """资源授权
        """
        try:
            # 1.登录rastest9
            browser = self.login_rastest9()
            time.sleep(3)
            # 2.创建订单
            Order(browser)
            # 3.登录 kedong.zhixueyun.com
            browser = self.login_kedong()
            # 4.获取资源
            Resource(browser)
        finally:
            self.browser.quit()

    def login_rastest9(self) -> Browser:
        """登录到rastest9
        """
        rastest9 = Loginzxy(
            self.browser, "https://rastest9.zhixueyun.com", "admin", "zxy123456")
        return rastest9.login()

    def login_kedong(self) -> Browser:
        """登录到kedong.zhixueyun.com
        """
        kedong = Loginzxy(
            self.browser, "https://kedong.zhixueyun.com", "admin", "zxy123456")
        return kedong.login()


if __name__ == "__main__":
    Grant().create()
