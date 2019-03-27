#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac") # executable_path来指定chromedirver路路径
browser.implicitly_wait(10)
browser.get("https://www.douban.com")
print(browser.get_window_size())
print(browser.get_window_position())
print(browser.get_cookies())
print(browser.title)
# print(browser.page_source)
print(browser.current_url)
browser.set_window_size(300,300)
time.sleep(5)
