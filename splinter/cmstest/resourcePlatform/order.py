# -*- coding:utf-8 -*-
import init_env
import time
from splinter import Browser


class Order:
    """创建订单
    """

    def __init__(self, browser=None):
        self.browser = browser
        # 1.创建订单
        self.create()
        # 2.提交订单并生效
        self.active()

    def create(self):
        """创建订单
        """
        browser = self.browser
        # 进入订单管理页面
        browser.visit(
            'https://rastest9.zhixueyun.com/admin/#/order/order-manage')
        time.sleep(1)

        # 5.点开新增订单页面
        add_order = browser.find_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div')
        add_order.click()
        time.sleep(0.5)

        # 5.1.1.点开客户方选择器
        company_name = browser.find_by_name('company_name')
        time.sleep(0.5)
        company_name.click()
        time.sleep(1)

        # 5.1.2.过滤客户方
        username_input = browser.find_by_name('fullName')
        username_input.fill('kedong')
        searchbtn = browser.find_by_text('查询').last
        time.sleep(0.5)
        searchbtn.click()
        time.sleep(0.5)

        # 5.1.3.选择客户方 (选择列表中的第一个)
        user_list = browser.find_by_name('memberId')
        user_list.click()
        # 5.1.4.确定
        confirmbtn = browser.find_by_text('确定').last
        time.sleep(0.5)
        confirmbtn.click()
        time.sleep(0.5)

        # 5.2.1.选择订单类型
        browser.find_by_css(
            'selectize-input items has-options full has-items').last.click()
        # 5.2.2.选择资源订单类型
        browser.find_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div/div[2]/div/div/form/div/div[3]/div[2]/div/div[2]/div/div[2]').click()

        # 5.3.1.设置订单有效期——开始时间
        browser.find_by_xpath('//*[@id="D449start-time"]').click()
        browser.find_by_css_selector(
            'div.dayContainer > span.today').click()
        # 5.3.2.设置订单有效期——结束时间
        browser.find_by_xpath('//*[@id="D449start-time"]').click()
        # browser.find_by_css_selector('div.dayContainer > span.today + span').click()

        print('创建订单')
        time.sleep(5)

    def active(self):
        """提交订单并生效
        """
        print('提交订单并生效')

        time.sleep(5)
