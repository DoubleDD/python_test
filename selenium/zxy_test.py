#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ZxyTestCase(unittest.TestCase):
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
        driver.get("https://dev9.zhixueyun.com")
        driver.maximize_window()
        print('打开url')
        sleep(2)

        longin_link = driver.find_element_by_link_text("登录")
        print('获取登录按钮')
        longin_link.click()
        print('点击登录按钮')
        sleep(1)

        username = findXpath('//*[@id="D35username"]')
        password = findXpath('//*[@id="D35pword"]')
        username.send_keys('admin' + Keys.ESCAPE)
        print('设置用户名')
        password.send_keys('zxy123456' + Keys.RETURN)
        print('设置密码')
        sleep(2)

        # 设置按钮
        setting_btn = findXpath('//*[@id="D17top-content"]/div[2]/div[2]/div[3]/a/i')
        setting_btn.click()
        print('打开后台页面')
        sleep(1)

        # 系统管理
        system_manage_btn = findXpath('//*[@id="D23menu-007"]')
        system_manage_btn.click()
        sleep()

        # 系统配置
        system_config = findXpath('//*[@id="D32menu-007003"]')
        system_config.click()
        rule_config_memu = findXpath('//*[@id="D32sub-menu-007003001"]')
        rule_config_memu.click()
        sleep(1)

        # 游戏设置
        game_config_trs = driver.find_elements_by_tag_name('tr')
        for tr in game_config_trs:
            tds = tr.find_elements_by_tag_name('td')
            if tds:
                desc = tds[1].text
                if '游戏等级设置' == desc:
                    setting_link = tds[3].find_element_by_link_text('设置')
                    setting_link.click()
                    break
        sleep()
        add_btn = findXpath('//*[@id="D414add-game-settings"]')
        add_btn.click()
        dialog = driver.find_element_by_class_name('dialog-content-main')
        trs = dialog.find_elements_by_tag_name('tr')
        last_tr = trs[len(trs)-1]
        level_tds = last_tr.find_elements_by_tag_name('td')
        level_name = level_tds[0]
        level_icon = level_tds[1]
        level_num = level_tds[2]
        done_btn = level_tds[3]
        level_name.find_element_by_tag_name('input').send_keys('test' + Keys.ESCAPE)
        level_num.find_element_by_tag_name('input').send_keys('80000' + Keys.ESCAPE)
        level_icon.find_element_by_link_text('上传图标（132*80）').click()
        done_btn.find_element_by_link_text('完成').click()
        print('done!')


def sleep(s=.5) -> None:
    time.sleep(s)

