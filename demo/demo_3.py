#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac") # executable_path来指定chromedirver路路径
browser.implicitly_wait(10)
browser.get("https://www.douban.com")

print("登录douban")
browser.find_element_by_class_name("lnk-book").click()
print("点击读书")
handles_list = browser.window_handles
print(handles_list)
browser.switch_to.window(str(handles_list[-1]))
# print("切换窗⼝口")
# if browser.current_window_handle == str(handles_list[-1]):
#     print("切换窗⼝口成功...")

browser.find_element_by_name("search_text").send_keys("11111")
print("搜索1111")



WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "lnk-book"))).click()


WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.CLASS_NAME, "lnk-book"))).click()