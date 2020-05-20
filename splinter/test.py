import init_env
from splinter import Browser

browser = Browser("chrome")
browser.visit('https://www.baidu.com')
