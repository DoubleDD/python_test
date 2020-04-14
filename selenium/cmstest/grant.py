# -*- coding:utf-8 -*-
import init_env
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from customCompany.resource import Resource
from resourcePlatform.order import Order
from login_web import LoginWeb


class Grant:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def destroy(self) -> None:
        self.driver.quit()

    def loginNewTable(self, url=None, username=None, password=None):
        js = f'window.open("{url}")'
        self.driver.execute_script(js)
        time.sleep(1.5)
        self.login.loginAction(self.driver, username, password)

    def create(self):
        """资源授权
        """
        driver = self.driver
        # 1.登录rastest9
        self.login = LoginWeb(driver, "https://rastest9.zhixueyun.com", "admin", "zxy123456")

        # 2.创建订单
        Order(driver)

        # 3.登录 kedong.zhixueyun.com
        self.login = LoginWeb(driver, "https://kedong.zhixueyun.com", "admin", "zxy123456")

        # 4.获取资源
        Resource(driver)



if __name__ == "__main__":
    Grant().create()
