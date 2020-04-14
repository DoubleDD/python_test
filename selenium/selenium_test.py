# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
assert '百度一下，你就知道' in browser.title

baiduHandle = browser.current_window_handle

elem = browser.find_element_by_id('kw')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

js = 'window.open("https://bing.com");'
browser.execute_script(js)
time.sleep(2)
bingHandle = browser.current_window_handle

browser.switch_to_window(baiduHandle)
time.sleep(2)

browser.switch_to_window(bingHandle)
print("从百度切换到bing")
time.sleep(2)

