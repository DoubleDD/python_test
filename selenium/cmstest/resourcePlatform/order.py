# -*- coding:utf-8 -*-
import init_env
import time
from selenium.webdriver.common.keys import Keys


class Order:
    """创建订单
    """

    def __init__(self, driver=None):
        self.driver = driver
        # 1.创建订单
        self.create()
        # 2.提交订单并生效
        self.active()

    def create(self):
        """创建订单
        """
        driver = self.driver
        # 1.进入管理后台
        # driver.find_element_by_xpath(
        #     '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[4]/a').click()
        # time.sleep(1.5)

        # # 2.打开运营管理菜单
        # driver.find_element_by_link_text('运营管理').click()
        # time.sleep(0.5)

        # # 3.展开订单管理菜单
        # driver.find_element_by_xpath(
        #     '/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[2]/span').click()
        # # 4.点开订单管理页面
        # driver.find_element_by_xpath(
        #     '/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[2]/ul/li[1]/span').click()
        # time.sleep(1.5)

        driver.get('https://rastest9.zhixueyun.com/admin/#/order/order-manage')
        time.sleep(1)

        # 5.点开新增订单页面
        add_order = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div')
        add_order.click()

        # 5.1.1.点开客户方选择器
        companyName = driver.find_element_by_name('companyName')
        time.sleep(2)
        companyName.click()
        time.sleep(3)
        # 5.1.2.过滤客户方
        userNameInput = driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[3]/div/div/div[2]/div/div[1]/div/form/div/div/div/div[1]/input')
        userNameInput.send_keys('kedong' + Keys.RETURN)
        time.sleep(1)
        # 5.1.3.选择客户方 (选择列表中的第一个)
        userList = driver.find_element_by_name('memberId')
        userList[0].click()
        # 5.1.4.确定
        driver.find_element_by_xpath('//*[@id="D500btn-0"]')

        # 5.2.1.选择订单类型
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div/div[1]').click()
        # 5.2.2.选择资源订单类型
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div/div[2]/div/div[2]').click()

        # 5.3.1.设置订单有效期——开始时间
        driver.find_element_by_xpath('//*[@id="D449start-time"]').click()
        driver.find_element_by_css_selector(
            'div.dayContainer > span.today').click()
        # 5.3.2.设置订单有效期——结束时间
        driver.find_element_by_xpath('//*[@id="D449start-time"]').click()
        # driver.find_element_by_css_selector('div.dayContainer > span.today + span').click()

        print('创建订单')

        time.sleep(5)
        pass

    def active(self):
        """提交订单并生效
        """
        print('提交订单并生效')

        time.sleep(5)
        pass
