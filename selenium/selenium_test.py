# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()

browser.get('https://www.baidu.com/')
assert '百度一下，你就知道' in browser.title

elem = browser.find_element_by_id('kw')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()
