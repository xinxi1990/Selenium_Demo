#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac") # executable_path来指定chromedirver路路径
browser.get("https://www.douban.com")
print("登录douban")

# browser.switch_to.frame(browser.find_elements_by_tag_name("iframe")[0])
browser.switch_to.frame(0)
print("切换frame")
browser.find_element_by_class_name('account-tab-account').click()
print("点击密码登录")


# 切到指定的frame->定位元素
