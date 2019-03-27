#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac")
# executable_path来指定chromedirver路径
browser.get("https://www.douban.com")
print("登录douban")
browser.implicitly_wait(10)

browser.find_element_by_class_name("lnk-book").click()
print("点击读书")
handles_list = browser.window_handles
print(handles_list)
browser.switch_to.window(str(handles_list[-1]))
print("切换窗口")
if browser.current_window_handle == str(handles_list[-1]):
    print("切换窗口成功...")
